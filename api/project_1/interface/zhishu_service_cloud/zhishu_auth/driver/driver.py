from api.project_1.interface.base.base import Base
from api.project_1.interface.util.database_util import DbUtil
from api.project_1.result.check_message_result import CheckMessageResult
import json


class Driver(Base):
    INSERT_CHECK_SQL = "SELECT * FROM `trans_res` WHERE VENDOR_CODE_COD = '{vendorCode}' AND " \
                       "NUMBER_PLATE_TXT = '{numberPlate}' AND DELETE_FG = '0'"

    def __init__(self):
        self.db_util = DbUtil()
        self.check_field_map = {"vendorCode": "VENDOR_CODE_COD",
                                "numberPlate": "NUMBER_PLATE_TXT"}
        self.instance_running_variables = {}

    def check_chain(self, outbound_parameter):
        self.check_database(outbound_parameter.get("payload"))
        return "后续验证通过" + str(outbound_parameter)

    def insert_check(self, outbound_parameter):
        payload = outbound_parameter.get("payload")
        check_field_list = ("vendorCode", "numberPlate")
        sql = Driver.INSERT_CHECK_SQL.format_map(payload)
        self.db_util.cursor.execute(sql)
        trans_data = self.db_util.cursor.fetchone()
        check_result = self.check_database(payload, trans_data, check_field_list)
        return CheckMessageResult.create_function_result_msg(check_result)

    def check_database(self, payload, data_base=None, check_field_list=None):
        check_message_map = {"result": True,
                             "result_msg": {}}
        for check_field in check_field_list:
            if not payload[check_field] == data_base[self.check_field_map[check_field]]:
                check_message_map["result"] = False
                check_message_map["result_msg"].setdefault(check_field, "比对失败，与预期不符，数据库存值：{}，前端传入值：{}"
                                                           .format(payload[check_field], data_base[self.check_field_map[check_field]]))
        check_message_map["result_msg"] = json.dumps(check_message_map["result_msg"])
        return check_message_map

    def before_process(self, before_process_function_parameter):
        sql = "UPDATE `trans_res` SET DELETE_FG = '1' WHERE VENDOR_CODE_COD = '{vendorCode}' AND NUMBER_PLATE_TXT = " \
              "'{numberPlate}' " \
            .format_map(before_process_function_parameter)
        try:
            self.db_util.cursor.execute(sql)
            item = self.db_util.cursor.fetchone()
            return item
        except Exception as e:
            print(e)
