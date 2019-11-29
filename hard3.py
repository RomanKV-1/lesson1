# Задание-3
#Вывести на экран:
#AAABBBAAABBBAAABBB
#BBBAAABBBAAABBBAAA
#AAABBBAAABBBAAABBB
#(таких строк n, в каждой строке m троек AAA)
n = int(input('введите число строк'))
m = int(input('введите количество троек ААА'))
c = 1
while c <= n:
  if c % 2 != 0:
    print('AAABBB' * m)
  else:
    print('BBBAAA' * m)
  c += 1