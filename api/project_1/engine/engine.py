import requests, json
from api.project_1.result.check_message_result import CheckMessageResult
from api.common.util.create_instance import CreateInstance
from api.project_1.config.config import Config

headers = {
    "content-type": "application/json",
    "zhishu-token-authorization": Config.zhishu_token_authorization,
    "token": "DNydwGOKWlefl3jgwveHHT1ABlDZqdQE"
}


class Interface(object):

    def __init__(self):
        self.response_dict = {}
        self.main_running_variables = {}

    def execute_process(self, test_task):
        for test_file in test_task:
            test_data_path = test_task[test_file].get("test_data_path")
            test_file_name = test_task[test_file].get("test_file_name")
            test_data_detail = CreateInstance(test_data_path).get_test_data(test_file_name)
            data_id_list = test_task[test_file].get("test_data_id_list")
            self.execute(data_id_list, test_data_detail)

    def execute(self, data_id_list, test_data_detail):
        for test_id in data_id_list:
            url = test_data_detail["case"][test_id].get("url") or test_data_detail.get("url")
            payload = test_data_detail.get("case").get(test_id).get("data")
            path_variable = test_data_detail.get("case").get(test_id).get("path_variable")
            except_code = test_data_detail.get("case").get(test_id).get("except_code")
            check_function_name = test_data_detail.get("case").get(test_id).get("check_function")
            outbound_parameter = test_data_detail.get("case").get(test_id).get("check_function_parameter")
            method_option = test_data_detail.get("case").get(test_id).get("method")
            before_function = test_data_detail.get("case").get(test_id).get("before_process_function")
            before_process_function_parameter = test_data_detail.get("case").get(test_id).get("before_process_function_parameter")
            after_function = test_data_detail.get("case").get(test_id).get("after_process_function")
            after_process_function_parameter = test_data_detail.get("case").get(test_id).get("after_process_function_parameter")
            class_path = test_data_detail.get("class_path")
            class_name = test_data_detail.get("class_name")
            outbound_parameter["payload"] = payload
            method = getattr(requests, method_option)
            class_instance = CreateInstance().create(class_path, class_name)
            if before_function:
                getattr(class_instance(), before_function)(before_process_function_parameter)
            if path_variable:
                url = url.format_map(path_variable)
            res = method(url=url, json=payload, headers=headers)
            res_result = {
                "url": url,
                "code": json.loads(res.text).get("code"),
                "result": json.loads(res.text) if res.text else "无返回数据",
                "except_code": except_code,
                "case_id": test_id,
                "check_function_result": "无后续验证"
            }
            outbound_parameter["res_result"] = res_result["result"]
            if res_result["code"] == except_code:
                if check_function_name:
                    check_function_result = getattr(class_instance(), check_function_name)(outbound_parameter)
                    res_result["check_function_result"] = check_function_result
                self.response_dict.setdefault("url:{} {}".format(url, test_id), CheckMessageResult.create_result_msg((True, res_result)))
            else:
                self.response_dict.setdefault("url:{} {}".format(url, test_id), CheckMessageResult.create_result_msg((False, res_result)))
            if after_function:
                getattr(class_instance(), after_function)(after_process_function_parameter)

    def result(self):
        for result in self.response_dict:
            print(self.response_dict[result])


if __name__ == '__main__':
    interface_instance = Interface()
    test_id_list = [1, 3, 5]
