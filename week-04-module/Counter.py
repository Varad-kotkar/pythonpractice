class Counter:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            num=self.num
            self.num+=1
            return num
        else:
            raise StopIteration


c = Counter()

for x in c:
    print(x)