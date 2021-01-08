from flask import Blueprint, jsonify, request

from service import RecordNotFoundError, UnprocessableEntityError

BaseController = Blueprint('base', __name__)


@BaseController.route('/')
def index():
    return 'Hello'


@BaseController.app_errorhandler(RecordNotFoundError)
def handle_not_found(e):
    return jsonify(error=str(e)), 404


@BaseController.app_errorhandler(UnprocessableEntityError)
def handle_not_found(e):
    return jsonify(error=str(e)), 422


def serialize(model, serializer):
    if isinstance(model, list):
        return jsonify(list(map(
            lambda x: serializer.serialize(x),
            model
        )))
    else:
        return jsonify(serializer.serialize(model))
