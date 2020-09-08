from abc import ABCMeta, abstractmethod

class Abst(metaclass=ABCMeta):

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass



class Impli(Abst):
#    def __next__(self):
#        return 1

    def methodImpli(self):
        print('hoge')

Impli().methodImpli()


#抽象クラスの__next__は、__がついているがオーバライドしなければエラーになる