from abc import ABCMeta, abstractmethod

class Abst(metaclass=ABCMeta):
    __num = 10

class Impli(Abst):

    def methodImpli(self):
        print(self.__num)

Impli().methodImpli()
#抽象クラスの属性にはアクセスすることはできない(javaと同じ)