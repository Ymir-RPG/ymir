"""
Integration tests for Ymir API.
"""

import unittest
import json
from os import remove
from uuid import uuid4
import time

from ymir import api
from ymir import app

api.set_session("sqlite:///tests.sqlite")


class TestApi(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.db_file = str(uuid4())
        self.db = "sqlite:///" + self.db_file
        api.set_session(self.db)

    def test_get_no_world(self):
        result = json.loads(self.client.get("/worlds").get_data())
        self.assertEqual([], result)

    def test_worlds(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        result = json.loads(self.client.get("/worlds").get_data())
        self.assertEqual(1, result[0]["id"])
        self.assertEqual("middle-earth", result[0]["name"])
        self.assertNotEqual(None, result[0]["lastUpdated"])

    def test_chronological(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds", data=json.dumps({"name": "edge-earth"}))
        result = json.loads(self.client.get(
            "/worlds", data=json.dumps({"chronological": True})).get_data())
        self.assertEqual(2, result[0]["id"])
        self.assertEqual(1, result[1]["id"])
        self.client.put("/worlds/1", data=json.dumps({"name": "earth2"}))
        result = json.loads(self.client.get(
            "/worlds", data=json.dumps({"chronological": True})).get_data())
        self.assertEqual(1, result[0]["id"])
        self.assertEqual(2, result[1]["id"])

    def test_get_world_by_id(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        result = json.loads(self.client.get("/worlds/1").get_data())
        self.assertEqual(1, result["id"])
        self.assertEqual("middle-earth", result["name"])
        self.assertIn("lastUpdated", result)

    def test_update_world(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.put("/worlds/1", data=json.dumps({"name": "edge-earth"}))
        result = json.loads(self.client.get("/worlds/1").get_data())
        self.assertEqual(1, result["id"])
        self.assertEqual("edge-earth", result["name"])

    def test_last_updated(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        original = json.loads(self.client.get("/worlds/1").get_data())
        time.sleep(1)
        self.client.put("/worlds/1", data=json.dumps({"name": "edge-earth"}))
        result = json.loads(self.client.get("/worlds/1").get_data())
        self.assertNotEqual(original["lastUpdated"], result["lastUpdated"])

    def test_delete_world(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.delete("/worlds/1")
        result = self.client.get("/worlds/1")
        self.assertEqual(404, result.status_code)

    def test_get_characters_empty(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        result = json.loads(self.client.get("/worlds/1/characters").get_data())
        self.assertEqual([], result)

    def test_post_characters(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/characters", data=json.dumps({"name": "Donald Trump"}))
        result = json.loads(self.client.get("/worlds/1/characters").get_data())
        self.assertEqual("Donald Trump", result[0]["name"])
        self.assertEqual(1, result[0]["worldId"])
        self.assertEqual(None, result[0]["placeId"])
        self.assertIn("lastUpdated", result[0])

    def test_get_character(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/characters", data=json.dumps({"name": "Donald Trump"}))
        result = json.loads(self.client.get("/worlds/1/characters/1").get_data())
        self.assertEqual("Donald Trump", result["name"])
        self.assertEqual(1, result["worldId"])
        self.assertEqual(None, result["placeId"])
        self.assertIn("lastUpdated", result)

    def test_put_character(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/characters", data=json.dumps({"name": "Donald Trump"}))
        result = json.loads(self.client.put("/worlds/1/characters/1", data=json.dumps({"name": "Barack Obama"})).get_data())
        self.assertEqual("Barack Obama", result["name"])
        self.assertEqual(1, result["worldId"])
        self.assertEqual(None, result["placeId"])
        self.assertIn("lastUpdated", result)

    def test_delete_character(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/characters", data=json.dumps({"name": "Donald Trump"}))
        self.client.delete("/worlds/1/characters/1")
        result = self.client.get("/worlds/1/characters/1")
        self.assertEqual(404, result.status_code)

    def test_get_places_empty(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        result = json.loads(self.client.get("/worlds/1/places").get_data())
        self.assertEqual([], result)

    def test_post_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({"name": "uo"}))
        result = json.loads(self.client.get("/worlds/1/places").get_data())
        self.assertEqual("uo", result[0]["name"])
        self.assertEqual(1, result[0]["worldId"])
        self.assertIn("lastUpdated", result[0])

    def test_get_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({"name": "uo"}))
        result = json.loads(self.client.get("/worlds/1/places/1").get_data())
        self.assertEqual("uo", result["name"])
        self.assertEqual(1, result["worldId"])
        self.assertIn("lastUpdated", result)

    def test_put_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({"name": "uo"}))
        result = json.loads(self.client.put("/worlds/1/places/1", data=json.dumps({"name": "UO"})).get_data())
        self.assertEqual("UO", result["name"])
        self.assertEqual(1, result["worldId"])
        self.assertIn("lastUpdated", result)

    def test_delete_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({"name": "uo"}))
        self.client.delete("/worlds/1/places/1")
        result = self.client.get("/worlds/1/places/1")
        self.assertEqual(404, result.status_code)

    def test_person_in_a_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({
            "name": "Whitehouse"}))
        self.client.post("/worlds/1/places", data=json.dumps({
            "name": "Mexico"}))
        self.client.post("/worlds/1/characters", data=json.dumps({
            "name": "Barack Obama",
            "placeId": 1}))
        self.client.post("/worlds/1/characters", data=json.dumps({
            "name": "Donald Trump",
            "placeId": 2}))
        result = json.loads(
            self.client.get(
                "/worlds/1/characters",
                data=json.dumps({"placeId": 1})).get_data())
        self.assertEqual(1, len(result))
        self.assertEqual("Barack Obama", result[0]["name"])
        result = json.loads(
            self.client.get(
                "/worlds/1/characters",
                data=json.dumps({"placeId": 2})).get_data())
        self.assertEqual(1, len(result))
        self.assertEqual("Donald Trump", result[0]["name"])

    def tearDown(self):
        remove(self.db_file)
