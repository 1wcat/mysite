def computeBMI(h, w):
    h = h/100
    return w / (h ** 2)

def getMemo(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 22.9:
        return 'normal'
    elif bmi < 27:
        return 'slightly overweight'
    elif bmi <30:
        return 'overweight'
    else:
        return 'obese'

def BMItable():
    with open('bmi.txt') as f:
        first = f.readline()
        hs = first.split()
        fmt = '{:>10}{:^10}{:^10}{:^10}{:^10}{:^10}'
        print(fmt.format(hs[0], hs[1], hs[2], hs[3], 'BMI', 'MEMO'))
        print('-' * 65)
        for line in f:
            tks = line.strip().split()
            name, gender, h, w = tks[0], tks[1], float(tks[2]), float(tks[3])
            bmi = round(computeBMI(h, w), 2)
            memo = getMemo(bmi)
            print(fmt.format(name, gender, h, w, bmi, memo))
            #print(type(name), type(gender), type(h), type(w))
BMItable()