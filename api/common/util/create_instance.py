
class CreateInstance(object):
    def __init__(self, test_data_path="api.project_1.test_data.", class_name=()):
        self.test_data_path = test_data_path
        self.class_name = class_name

    def get_test_data(self, data_name):
        test_data_path = self.test_data_path + data_name
        data_meta = __import__(test_data_path, globals(), locals(), [data_name])
        return getattr(data_meta, data_name)

    def create(self, class_path="", class_name=None):
        class_path = class_path
        module_meta = __import__(class_path, globals(), locals(), [class_name])
        return getattr(module_meta, class_name)


if __name__ == '__main__':
    a = CreateInstance().get_test_data("driver_test_data")
    b = CreateInstance().create("api.project_1.interface.login.B", "B")
    print(type(a))
    print(a)
    getattr(b(), "test")()
    # a["C"]()
