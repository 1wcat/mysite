def frame(m, n, ch='*'):
  for i in range(n):
    print(ch, end=' ')
  print()
  
  for j in range(m-2):
    print(ch, end=' ')
    for i in range(n-2):
      print(' ', end=' ')
    print(ch)
  
  for i in range(n):
    print(ch, end=' ')
  print()
frame(5, 6, '#')

def square_numbers(n):
  i = 1
  while i*i < n:
    print(i*i, end=' ')
    i += 1
  print()

square_numbers(25)
square_numbers(30)

def pr_digits(n):
  while n > 0:
    print(int(n % 10), end=' ')
    n = (n - (n % 10))/10
  print()

pr_digits(5764)
pr_digits(123456)