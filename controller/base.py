from flask import Blueprint, jsonify, request

from service import RecordNotFoundError

base = Blueprint('base', __name__)


@base.app_errorhandler(RecordNotFoundError)
def handle_not_found(e):
    return jsonify(error=str(e)), 404
