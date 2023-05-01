from flask import Blueprint

api = Blueprint('api', __name__)

from . import table
from . import data
from . import items