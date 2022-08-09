from api.api_check.api_check_map import api_check_map
from api.common.util.create_instance import CreateInstance
from api.message_notify.server import result_message_notify


class ApiCheckService(object):
    def __init__(self, request_user=None):
        self.request_user = request_user
        self.notify_message = {}

    def data_check_process(self, request_uri, request_data):
        for check_url in api_check_map:
            if check_url in request_uri:
                class_path = api_check_map[check_url].get("class_path")
                class_name = api_check_map[check_url].get("class_name")
                class_instance = CreateInstance().create(class_path, class_name)()
                self.data_check(class_instance, request_data)
                if self.request_user and self.notify_message:
                    result_message_notify[self.request_user].put("接口：{} {}".format(check_url, str(self.notify_message)))

    def data_check(self, class_instance, request_data):
        for field in request_data:
            if field in class_instance.data:
                if not isinstance(field, type(class_instance.data[field]["field_type"])):
                    self.notify_message.setdefault("类型错误: " + field, "请确认前端该字段请求类型: " + type(field))
                if isinstance(request_data[field], str):
                    print(len(request_data[field]))
                    if not class_instance.data[field]["field_range"][0] <= len(request_data[field]) <= \
                           class_instance.data[field] \
                                   ["field_range"][1]:
                        self.notify_message.setdefault("传值范围错误: " + field, "请确认前端该字段请求请求范围操作: " + request_data[field])
                    if class_instance.data[field]["field_check_function"]:
                        if not getattr(class_instance, class_instance.data[field]["field_check_function"])(
                                **request_data):
                            self.notify_message.setdefault("后续验证错误: " + field,
                                                           "请确认前端该字段验证函数：" + class_instance.data[field]
                                                           ["field_check_function"])
                else:
                    res = getattr(class_instance, class_instance.data[field]["field_check_function"])(**request_data)
                    if not res["result"]:
                        self.notify_message.setdefault("验证函数错误: " + field,
                                                       "请确认前端该字段非str验证函数：" + class_instance.data[field]
                                                       ["field_check_function"] + res["result_message"])
                        print(res["result_message"])
