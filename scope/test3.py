class TestClass(object):
    common_var = []
    def get_variable(self):
        return self.common_var
    def set_variable(self, value):
        self.common_var.append(value)

tc1 = TestClass()
tc2 = TestClass()
tc1.set_variable("Set Variable")
print(tc2.common_var)

#['Set Variable']