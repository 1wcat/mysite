'''
lst1 = [99, 66, 22]
lst2 = lst1
print('lst1:', lst1, 'lst2:', lst2)
lst2[0] = 777
print('lst1:', lst1, 'lst2:', lst2)
lst1[-1] = 333
print('lst1:', lst1, 'lst2:', lst2)

lst3 = [1, 2, 3]
lst4 = [4, 5, 6]
print['lst3:', lst3, 'lst4:', lst4]
lst4[0] = 777
print['lst3:', lst3, 'lst4:', lst4]
lst3[-1] = 333
print['lst3:', lst3, 'lst4:', lst4]
'''

class Thing:
    _name = 'unknown'
    def __init__(self, name):
        self._name = name
'''
def test():
    t1 = Thing('wood')
    t2 = Thing('iron') 
    print(t1._name, t2._name)
    t1._name = 'glass'
    print(t1._name, t2._name)
    t3 = t2
    t3._name = 'salt'
    print(t2._name, t3._name)
test()
'''

def change(t):
    t.name = 'air'

def test2():
    t1 = Thing('tissue')
    print(t1._name)
    change(t1)
    print(t1.name)

test2()