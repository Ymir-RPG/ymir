import json

from flask import request, abort
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound

from ymir.models import World, Character, Place
from ymir.db import session
from ymir import app


@app.route("/worlds", methods=["GET"])
def worlds_get():
    return json.dumps([i.to_dict() for i in session.query(World).all()])


@app.route("/worlds", methods=["POST"])
def worlds_post():
    name = request.args["name"]
    session.add(World(name=name))
    session.commit()
    return ('', 204)


@app.route("/worlds/<world_id>", methods=["GET"])
def world_id_get(world_id):
    try:
        return json.dumps(session.query(
            World).filter(World.id == world_id).one().to_dict())
    except NoResultFound:
        abort(404)


@app.route("/worlds/<world_id>", methods=["PUT"])
def world_id_put(world_id):
    name = request.args["name"]
    world = session.query(World).filter(World.id == world_id).one()
    world.name = name
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
    try:
        return json.dumps([i.to_dict() for i in session.query(
            Character).filter(Character.world_id == world_id).all()])
    except NoResultFound:
        abort(404)


@app.route("/worlds/<world_id>/characters", methods=["POST"])
def characters_post(world_id):
    name = request.args["name"]
    character = Character(name=name, world_id=world_id)
    session.add(character)
    session.commit()
    return json.dumps(character.to_dict())


@app.route("/worlds/<world_id>/characters/<character_id>", methods=["GET"])
def character_id_get(world_id, character_id):
    try:
        return json.dumps(session.query(Character).filter(and_(
            Character.world_id == world_id, Character.id == character_id)).one().to_dict())
    except NoResultFound:
        abort(404)


@app.route("/worlds/<world_id>/characters/<character_id>", methods=["PUT"])
def character_name_put(world_id, character_id):
    try:
        character = session.query(Character).filter(
            and_(Character.world_id == world_id, Character.id == character_id)).one()
    except NoResultFound:
        abort(404)
    if request.args["name"]:
        character.name = request.args["name"]
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
