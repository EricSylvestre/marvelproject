from flask import Blueprint, Flask
bp = Blueprint('api', __name__, url_prefix='/api/v1')

from .import routes

