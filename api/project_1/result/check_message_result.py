class CheckMessageResult(object):
    @staticmethod
    def create_result_msg(result_message):
        flag = "success" if result_message[0] else "error"
        result_message[1].setdefault("flag", flag)
        return "{flag}: url: {url}, id: {case_id}, code: {code},  result: {result}, check_function_result:{" \
               "check_function_result}". \
            format_map(result_message[1])

    @staticmethod
    def create_function_result_msg(result_message):
        return "验证结果：{result}，验证消息：{result_msg}".format_map(result_message)
