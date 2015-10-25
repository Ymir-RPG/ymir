import json
from datetime import datetime

from flask import request, abort
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound

from ymir.models import World, Character, Place
from ymir.db import get_session
from ymir import app


session = get_session()


def set_session(db_conn_str):
    global session
    session = get_session(db_conn_str)


def _get_request_data(request):
    results = {}
    results.update(request.args)
    results.update(request.form)
    try:
        results.update(json.loads(request.get_data()))
    except ValueError:
        pass
    return results


@app.route("/worlds", methods=["GET"])
def worlds_get():
    data = _get_request_data(request)
    query = session.query(World)
    if data.get('chronological', False):
        query = query.order_by(World.last_updated.desc())
    return json.dumps([i.to_dict() for i in query.all()])


@app.route("/worlds", methods=["POST"])
def worlds_post():
    data = _get_request_data(request)
    name = data["name"]
    world = World(name=name, last_updated=datetime.now())
    session.add(world)
    session.commit()
    return json.dumps(world.to_dict())


@app.route("/worlds/<world_id>", methods=["GET"])
def world_id_get(world_id):
    try:
        return json.dumps(session.query(
            World).filter(World.id == world_id).one().to_dict())
    except NoResultFound:
        abort(404)


@app.route("/worlds/<world_id>", methods=["PUT"])
def world_id_put(world_id):
    data = _get_request_data(request)
    world = session.query(World).filter(World.id == world_id).one()
    world.name = data.get("name", world.name)
    world.last_updated = datetime.now()
    session.commit()
    return json.dumps(world.to_dict())


@app.route("/worlds/<world_id>", methods=["DELETE"])
def world_id_delete(world_id):
    try:
        world = session.query(World).filter(World.id == world_id).one()
    except NoResultFound:
        abort(404)
    session.delete(world)
    session.commit()
    return ('', 204)


@app.route("/worlds/<world_id>/characters", methods=["GET"])
def characters_get(world_id):
    data = _get_request_data(request)
    query = session.query(Character).filter(Character.world_id == world_id)
    if data.get('chronological', False):
        query = query.order_by(Character.last_updated.desc())
    if "placeId" in data:
        query = query.filter(Character.place_id == data["placeId"])
    return json.dumps([i.to_dict() for i in query.all()])


@app.route("/worlds/<world_id>/characters", methods=["POST"])
def characters_post(world_id):
    data = _get_request_data(request)
    name = data["name"]
    character = Character(name=name, world_id=world_id)
    if "placeId" in data:
        character.place_id = data["placeId"]
    character.last_updated = datetime.now()
    session.add(character)
    session.commit()
    return json.dumps(character.to_dict())


@app.route("/worlds/<world_id>/characters/<character_id>", methods=["GET"])
def character_id_get(world_id, character_id):
    try:
        return json.dumps(session.query(Character).filter(and_(
            Character.world_id == world_id,
            Character.id == character_id)).one().to_dict())
    except NoResultFound:
        abort(404)


@app.route("/worlds/<world_id>/characters/<character_id>", methods=["PUT"])
def character_name_put(world_id, character_id):
    data = _get_request_data(request)
    try:
        character = session.query(Character).filter(
            and_(Character.world_id == world_id, Character.id == character_id)).one()
    except NoResultFound:
        abort(404)
    character.name = data.get("name", character.name)
    character.place_id = data.get("place_id", character.place_id)
    character.last_updated = datetime.now()
    session.commit()
    # TODO(Skyler): If there is no change, we should return a different status
    return json.dumps(character.to_dict())


@app.route("/worlds/<world_id>/characters/<character_id>",
           methods=["DELETE"])
def character_name_delete(world_id, character_id):
    try:
        character = session.query(Character).filter(
            and_(Character.world_id == world_id, Character.id == character_id)).one()
    except NoResultFound:
        abort(404)
    session.delete(character)
    session.commit()
    return ('', 204)


@app.route("/worlds/<world_id>/places", methods=["GET"])
def places_get(world_id):
    data = _get_request_data(request)
    query = session.query(Place).filter(Place.world_id == world_id)
    if data.get('chronological', False):
        query = query.order_by(Place.last_updated.desc())
    return json.dumps([i.to_dict() for i in query.all()])


@app.route("/worlds/<world_id>/places", methods=["POST"])
def places_post(world_id):
    data = _get_request_data(request)
    name = data["name"]
    place = Place(name=name, world_id=world_id)
    place.last_updated = datetime.now()

    session.add(place)
    session.commit()
    return json.dumps(place.to_dict())


@app.route("/worlds/<world_id>/places/<places_id>", methods=["GET"])
def places_id_get(world_id, places_id):
    try:
        return json.dumps(session.query(Place).filter(and_(
            Place.world_id == world_id, Place.id == places_id)).one().to_dict())
    except NoResultFound:
        abort(404)


@app.route("/worlds/<world_id>/places/<place_id>", methods=["PUT"])
def places_name_put(world_id, place_id):
    data = _get_request_data(request)
    try:
        place = session.query(Place).filter(
            and_(Place.world_id == world_id, Place.id == place_id)).one()
    except NoResultFound:
        abort(404)
    place.name = data.get("name", place.name)
    place.last_updated = datetime.now()
    session.commit()
    # TODO(Skyler): If there is no change, we should return a different status
    return json.dumps(place.to_dict())


@app.route("/worlds/<world_id>/places/<place_id>",
           methods=["DELETE"])
def places_name_delete(world_id, place_id):
    try:
        place = session.query(Place).filter(
            and_(Place.world_id == world_id, Place.id == place_id)).one()
    except NoResultFound:
        abort(404)
    session.delete(place)
    session.commit()
    return ('', 204)
