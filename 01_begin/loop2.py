def rect_for(m, n, ch):
    for i in range(m):
      for j in range(n):
        print(ch, end=' ')
      print()
rect_for(3,5, '$')

def rect_while(m, n, ch):
    i = 0
    while i < m:
      j = 0
      while j< n:
        print(ch, end=' ')
        j += 1
      print()
      i += 1
rect_while(3, 5, '$')

def rect_str(m, n, ch):
  for i in range(m):
    print((ch+' ') * n)
rect_str(3, 5, '$')