from . import check_controller
from flask import request
from api.api_check.service.api_check_service import ApiCheckService


@check_controller.route('/api-check', methods=["GET", "POST", "PUT", "DELETE"])
def data_check(out_param=None):
    user = request.headers.get("token")
    request_uri = request.headers.get("HTTP_REFER_HOST")
    request_body = request.form
    ApiCheckService(user).data_check_process(request_uri, request_body)
    return ""
