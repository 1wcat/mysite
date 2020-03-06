class WorkRecord:
    name = 'unknown'
    week = None
    wage = 0
    def __init__(self, name):
        self.week = [0 for i in range(7)]
    def workHour(self, day, hours):
        self.week[day] = hours
    def setWage(self, wage):
        self.wage = wage
    def weekWage(self):
        dayWage = [self.wage * hours for hours in self.week]
        return sum(dayWage)

def read_file():
    with open('week.txt') as f:
        first = f.readline()
        for line in f:
            line = line.strip()
            tokens = line.split()
            wr = WorkRecord(tokens[0])
            for i in range(1, 7):
                wr.workHour(i, float(tokens[i]))
            wr.setWage(float(tokens[7]))
            print(wr.weekWage())

read_file()