from flask import Blueprint
check_controller = Blueprint('check_controller', __name__)

from . import views