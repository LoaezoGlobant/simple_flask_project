from flask import Blueprint, jsonify, request
from app import db
from app.models import User

users_bp = Blueprint(name="users", import_name="users", url_prefix="/users")

@users_bp.route("/", methods=["GET"])
def get_users() -> str:
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int) -> str:
    user = User.query.get(user_id)
    return jsonify(user.to_dict())

@users_bp.route("/", methods=["POST"])
def create_user() -> str:
    data = request.get_json()
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id: int) -> str:
    user = User.query.get(user_id)
    data = request.get_json()
    user.username = data["username"]
    user.email = data["email"]
    db.session.commit()
    return jsonify(user.to_dict())

@users_bp.route("/<int_user_id>", methods=["DELETE"])
def delete_user(user_id: int) -> str:
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"id": user.id,
            "status_code": 204}