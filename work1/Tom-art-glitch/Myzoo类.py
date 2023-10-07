class Myzoo(object):
    def __init__(self,d):
        self.animals = {} if len(d)==0 else d
        print("My zoo!")
    def print(self):
        for i in self.animals:
            print(f'{i}:', self.animals[i])

    def __eq__(self, other):
        return self.animals.keys()==other.animals.keys()
    def len(self):
        s = sum(self.animals[i] for i in self.animals)
        print(s)
myzoo1 = Myzoo({'pig':1})
myzoo2 = Myzoo({'pig':5})
print(myzoo1==myzoo2)
myzoo1.print()
myzoo2.len()


