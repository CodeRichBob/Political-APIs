from flask import Blueprint
views = Blueprint('views',__name__, url_prefix="/api/v1")
bash = Blueprint('bash',__name__, url_prefix="/api/v1")
