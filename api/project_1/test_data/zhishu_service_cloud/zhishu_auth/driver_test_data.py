driver_test_data = {
    "class_path": "api.project_1.interface.driver.driver",  # 指定后续验证方法所在类
    "class_name": "Driver",
    "url": "http://192.168.124.200/neo-api/trans-res",
    "case": {
        1: {
            "path_variable": {},
            "url": "",
            "data": {
                "driverName": "王部为2",
                "numberPlate": "闽A33448",
                "mobileNumber": "13456789761",
                "identity": "120987198710053211",
                "regionCode": "HY09",
                "vendorCode": "V0000005955",
                "vendorName": "testmy070808",
                "motorcycleCategory": "2",
                "motorcycleType": "0",
                "regionName": "蓝天上海库"
            },
            "method": "put",  # 小写
            "except_code": 201,  # 数字
            "check_function": "insert_check",
            "check_function_parameter": {"name": "test"},
            "before_process_function": "before_process",
            "before_process_function_parameter": {"vendorCode": "V0000005955", "numberPlate": "闽A33448"},
            "after_process_function": "",
            "after_process_function_parameter": "",
        },
        2: {
            "path_variable": {"id": 105},
            "url": "http://192.168.124.200/neo-api/trans-res/{id}",
            "data": {
                "driverName": "王部为3",
                "numberPlate": "闽O33448",
                "mobileNumber": "13456789761",
                "identity": "120987198710053211",
                "regionCode": "HY09",
                "vendorCode": "V0000005955",
                "vendorName": "testmy070808",
                "motorcycleCategory": "2",
                "motorcycleType": "0",
                "regionName": "蓝天上海库"
            },
            "method": "post",  # 小写
            "except_code": 204,  # 数字
            "check_function": "insert_check",
            "check_function_parameter": {"name": "test"},
            "before_process_function": "",  # 无前置处理函数时，置空value，不要删除key
            "before_process_function_parameter": {}  # 无前置处理函数时，置空value，不要删除key
        },
        3: {
            "field_1": "",
            "field_2": "",
            "field_3": "",
            "field_4": "",
            "field_5": ""
        }
    }
}
