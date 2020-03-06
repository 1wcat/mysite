class Student:
  def __init__(self, name, math, eng, chi, bio):
    self.name = name
    self.math = math
    self.eng = eng
    self.chi = chi
    self.bio = bio
  def info(self):
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    return fmt.format(self.name, self.math, self.eng, self.chi, self.bio)
  def total(self):
    return self.math + self.eng + self.chi + self.bio

def print_students(sts):
  for st in sts:
    print(st.info())

def select_math_larger_equal(sts, score):
  chosen = []
  for student in sts:
      if student.math >= score:
        chosen.append(student)
  return chosen

def select_chinese_less(sts, score):
  chosen = []
  for student in sts:
      if student.chi < score:
        chosen.append(student)
  return chosen

def select_biology_higher_avg(sts):
  chosen = []
  avg = sum([st.bio for st in sts]) / len(sts)
  for student in sts:
    if student.bio > avg:
      chosen.append(student)
  return chosen

def select_english_lowest(sts):
  lowest = sts[0]
  for student in sts:
    if student.eng < lowest.eng:
      lowest = st
  return lowest

def select_avg_highest(sts):
  highest = sts[0]
  for st in sts:
    if st.total() > highest.total():
      highest = st
  return highest
    


def read_scores():
  with open('scores.txt') as f1:
    first = f1.readline()
    print(first)
    students = []
    for line in f1:
      ts = line.strip().split()
      st = Student(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
      students.append(st)

    print('select math larger equal:')
    chosen_students = select_math_larger_equal(students, 80)
    print_students(chosen_students)
  
    print('select chinese less:')
    chosen_students = select_chinese_less(students, 80)
    print_students(chosen_students)

    print('select biology higher avg:')
    chosen_students = select_biology_higher_avg(students)
    print_students(chosen_students)

    print('select english lowest:')
    chosen_students = select_english_lowest(students)
    print_students(chosen_students)

    print('select avg highest:')
    chosen_students = select_avg_highest(students)
    print_students(chosen_students)
  
  

read_scores()