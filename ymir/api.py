import json

from flask import request

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
def worlds_world_name_get(world_name):
    return json.dumps(session.query(
        World).filter(World.name == world_name).one().to_dict())


@app.route("/worlds/<world_name>", methods=["PUT"])
def worlds_world_name_put(world_name):
    name = request.args["name"]
    world = session.query(World).filter(World.name == world_name).one()
    world.name = name
    session.commit()


@app.route("/worlds/<world_name>", methods=["DELETE"])
def worlds_world_name_delete(world_name):
    world = session.query(World).filter(World.name == world_name).one()
    session.delete(world)
    session.commit()
