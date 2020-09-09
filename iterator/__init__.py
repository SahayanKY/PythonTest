class Iterator:
    numbers = [1,2,3,4,5]
    index = 0

    def __init__(self):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.numbers):
            raise StopIteration
        print('__next__')
        value = self.numbers[self.index]
        self.index += 1
        return value

i = Iterator()
for num in i:
    print('for')
