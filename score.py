print('score')

def insert(tb, chi, eng, math):
    tb.append([chi, eng, math])

def pr_table(tb):
    n = 1
    for lst in tb:
        print('s{} '.format(n), end='')
        print(lst)
        n+=1

def test():
    table = []
    insert(table, 90, 80, 75)
    insert(table, 85, 88, 92) 
    insert(table, 89, 95, 97)
    pr_table(table)

test()