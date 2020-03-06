class Group:
    nums = []
    def __init__(self, nums):
        self.nums = nums
    def merge(self, group):
        newnums = []
        for num in self.nums:
            if not num in newnums:
                newnums.append(num)
        for num in group.nums:
            if not num in newnums:
                newnums.append(num)
        self.nums = newnums
    def mergeCreate(self, group):
        newnums = []
        for num in self.nums:
            if not num in newnums:
                newnums.append(num)
        for num in group.nums:
            if not num in newnums:
                newnums.append(num)
        return Group(newnums)
        self.nums = newnums
    def intersect(self, group):
        newnums = []
        for num in self.nums:
            if num in group.nums:
                newnums.append(num)
        self.nums = newnums
    def intersectCreate(self, group):
        newnums = []
        for num in self.nums:
            if num in group.nums:
                newnums.append(num)
        return Group(newnums)

def test():
    g1 = Group({11, 22, 33, 44, 55})
    g2 = Group({33, 44, 55, 66, 77})
    g1.merge(g2)
    g1.intersect(g2)
    g3 = g1.mergeCreate(g2)
    g4 = g1.intersectCreate(g2)
    print(g1.nums)
    print(g2.nums)
    print(g3.nums)
    print(g4.nums)

test()