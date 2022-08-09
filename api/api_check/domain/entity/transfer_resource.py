class TransferResource(object):
    def __init__(self):
        self.data = {
            "vendorCode": {
                "field_type": str(),
                "field_range": [0, 10],
                "field_check_function": "data_verify1"
            },
            "data": {
                "field_type": dict(),
                "field_check_function": "data_verify"
            }
        }

    def data_verify(self, **data_detail):
        data_detail.get("test")
        result = {"result": True,
                  "result_msg": ""}
        return result

    def data_verify1(self, **data_detail):
        data_detail.get("test")
        result = {"result": True,
                  "result_msg": ""}
        return result


if __name__ == '__main__':
    pass
