class TestClass(object):
    def __init__(self):
        self.common_var = None
    def set_variable(self, values=[]):
        print('set_variable1:', values)
        values.append("Set Variable")
        self.common_var = values
        print('set_variable2:', values)

tc1 = TestClass()
tc2 = TestClass()
tc1.set_variable()
tc2.set_variable()

#set_variable1: []
#set_variable2: ['Set Variable']
#set_variable1: ['Set Variable']
#set_variable2: ['Set Variable', 'Set Variable']


