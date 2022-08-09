class Base(object):
    @staticmethod
    def check_field(value, except_value):
        return "success" if value == except_value else "error"
