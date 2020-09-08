from abc import ABCMeta, abstractmethod

class Abst(metaclass=ABCMeta):

    @abstractmethod
    def __method(self):
        pass



class Impli(Abst):
#    def method(self):
#        pass
    def __method(self):
        pass

    def methodImpli(self):
        print('hoge')

Impli().methodImpli()

#抽象クラスのprivateメソッドはオーバーライドに失敗し、インスタンス化でエラーになる
#javaと同じ感じか