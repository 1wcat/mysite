def bmi(kg, m):
  return kg / (m * m)

def  check(kg, m=2, name='guest'):
  b = bmi(kg,m)
  print("{} BMI {}" .format(name, b)
  
check(50,1.6,"sj")