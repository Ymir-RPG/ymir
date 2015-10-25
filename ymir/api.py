import json

from flask import request
from sqlalchemy import and_

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


@app.route("/worlds/<world_name>", methods=["GET"])
def world_name_get(world_name):
    return json.dumps(session.query(
        World).filter(World.name == world_name).one().to_dict())


@app.route("/worlds/<world_name>", methods=["PUT"])
def world_name_put(world_name):
    name = request.args["name"]
    world = session.query(World).filter(World.name == world_name).one()
    world.name = name
    session.commit()


@app.route("/worlds/<world_name>", methods=["DELETE"])
def world_name_delete(world_name):
    world = session.query(World).filter(World.name == world_name).one()
    session.delete(world)
    session.commit()


@app.route("/worlds/<world_name>/characters", methods=["GET"])
def characters_get(world_name):
    world = session.query(World).filter(World.name == world_name).one()
    return json.dumps(
        [i.to_dict() for i in session.query(
            Character).filter(Character.world_id == world.id).all()])


@app.route("/worlds/<world_name>/characters", methods=["POST"])
def characters_post(world_name):
    world = session.query(World).filter(World.name == world_name).one()
    name = request.args["name"]
    session.add(Character(name=name, world_id=world.id))
    session.commit()


@app.route("/worlds/<world_name>/characters/<character_name>", methods=["GET"])
def character_name_get(world_name, character_name):
    world = session.query(World).filter(World.name == world_name).one()
    return json.dumps(session.query(
        Character).filter(and_(
            Character.world_id == world.id, Character.name == character_name)).one().to_dict())


@app.route("/worlds/<world_name>/characters/<character_name>", methods=["PUT"])
def character_name_put(world_name, character_name):
    world = session.query(World).filter(World.name == world_name).one()
    character = session.query(Character).filter(
        and_(World.name == world_name, Character.name == character_name)).one()
    if request.args["name"]:
        character.name = request.args["name"]
    session.commit()


@app.route("/worlds/<world_name>/characters/<character_name>",
           methods=["DELETE"])
def character_name_delete(world_name, character_name):
    world = session.query(World).filter(World.name == world_name).one()
    character = session.query(Character).filter(
        and_(Character.world_id == world.id, Character.name == character_name)).one()
    session.delete(character)
    session.commit()
