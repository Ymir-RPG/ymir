"""
Integration tests for Ymir API.
"""

import unittest
import json
from os import remove
from uuid import uuid4

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
        self.assertEqual([{"id": 1, "name": "middle-earth"}], result)

    def test_get_world_by_id(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        result = json.loads(self.client.get("/worlds/1").get_data())
        self.assertEqual({"id": 1, "name": "middle-earth"}, result)

    def test_update_world(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.put("/worlds/1", data=json.dumps({"name": "edge-earth"}))
        result = json.loads(self.client.get("/worlds/1").get_data())
        self.assertEqual({"id": 1, "name": "edge-earth"}, result)

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
        self.assertEqual([
            {"id": 1, "name": "Donald Trump", "world_id": 1, "place_id": None}],
            result)

    def test_get_character(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/characters", data=json.dumps({"name": "Donald Trump"}))
        result = json.loads(self.client.get("/worlds/1/characters/1").get_data())
        self.assertEqual(
            {"id": 1, "name": "Donald Trump", "world_id": 1, "place_id": None},
            result)

    def test_put_character(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/characters", data=json.dumps({"name": "Donald Trump"}))
        result = json.loads(self.client.put("/worlds/1/characters/1", data=json.dumps({"name": "Barack Obama"})).get_data())
        self.assertEqual(
            {"id": 1, "name": "Barack Obama", "world_id": 1, "place_id": None},
            result)

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
        self.assertEqual([{"id": 1, "name": "uo", "world_id": 1}], result)

    def test_get_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({"name": "uo"}))
        result = json.loads(self.client.get("/worlds/1/places/1").get_data())
        self.assertEqual({"id": 1, "name": "uo", "world_id": 1}, result)

    def test_put_place(self):
        self.client.post("/worlds", data=json.dumps({"name": "middle-earth"}))
        self.client.post("/worlds/1/places", data=json.dumps({"name": "uo"}))
        result = json.loads(self.client.put("/worlds/1/places/1", data=json.dumps({"name": "UO"})).get_data())
        self.assertEqual({"id": 1, "name": "UO", "world_id": 1}, result)

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
            "place_id": 1}))
        self.client.post("/worlds/1/characters", data=json.dumps({
            "name": "Donald Trump",
            "place_id": 2}))
        result = json.loads(
            self.client.get(
                "/worlds/1/characters",
                data=json.dumps({"place_id": 1})).get_data())
        self.assertEqual(1, len(result))
        self.assertEqual("Barack Obama", result[0]["name"])
        result = json.loads(
            self.client.get(
                "/worlds/1/characters",
                data=json.dumps({"place_id": 2})).get_data())
        self.assertEqual(1, len(result))
        self.assertEqual("Donald Trump", result[0]["name"])

    def tearDown(self):
        remove(self.db_file)
