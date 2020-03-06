class Student:
  sid = 'unknown'
  name = 'unknown'
  gender = 'unknown'
  height = 0
  weight = 0
  def __init__(self, sid, name, gender):
    self.sid = sid
    self.name = name
    self.gender = gender
  def set_height(self, h):
    self.height = h
  def set_weight(self, w):
    self.weight = w
  def bmi(self):
    return self.weight / ((self.height / 100) ** 2)
  def info(self):
    return '{:10}{:10}{:10}{:10}{:10}{:10}'.format(self.sid, self.name, self.gender, self.height, self.weight, round(self.bmi(), 2))

class BmiReport:
  name = 'unknown'
  sts = []
  def __init__(self, name):
    self.name = name
  def add_student(self, st):
    self.sts.append(st)
  def remove_student(self, sid):
    remove = None
    for st in self.sts:
      if st.sid == sid:
        remove = st
        break
    self.sts.remove(remove) 
  def save_file(self, filename):
    with open(filename, 'w') as f:
      f.write(self.name)
      f.write('\n')
      for st in self.sts:
        f.write(st.info())
        f.write('\n')
  def read_file(self, filename):
    with open(filename) as f:
      first = f.readline()
      self.name = first.strip()
      for line in f:
        ts = line.split(',')
        st = Student(ts[0], ts[1], ts[2])
        st.set_height(float(ts[3]))
        st.set_weight(float(ts[4]))
        #print(st.info())
        self.add_student(st)
  def print_report(self):
    print(self.name)
    for st in self.sts:
        print(st.info())

def test2():
  report = BmiReport('')
  report.read_file('students.txt')
  report.print_report()
#test2()

report = None
print('BMI app')
def run_app():
    while (True):
        line = input('>')
        print('Your input:', line)
        if(line == 'exit'):
            break
        if(line == 'help'):
            print('Avalible commands: <...> within brackets [...]leave out')
            print('blank <name>               -- create a <name> class')
            print('open <file>                -- open class file')
            print('save [file]                -- save file')
            print('import [file]              -- import student profile')
            print('list [from [to]]           -- print students')
            print('add <id> [name]            -- add student')
            print('update <id> <field> <val>  -- Change student profile')
            print('exit                       -- leave')
        if line.startswith('blank'):
            print(line)
            tokens = line.split()
            report = BmiReport(tokens[1])
        if line.startswith('list'):
            report.print_report()
        if line.startswith('import'):
            tokens = line.split()
            if not report:
                report = BmiReport('dummy')
            report.read_file(tokens[1])
        if line.startswith('add'):
            tokens = line.split()
            st = Student(tokens[1], tokens[2], tokens[3])
            st.set_height(float(tokens[4]))
            st.set_weight(float(tokens[5]))
            report.add_student(st)
        if line.startswith('save'):
            tokens = line.split()
            report.save_file(tokens[1])

    print('Bye')

run_app()