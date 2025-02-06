# ex1
x = 52633
for i in range(x+1):
  if i == 0:
    continue
  if x % i == 0:
    print(i)

# ex2
def print_factor(x):
  factors = []
  for i in range(x+1):
    if i == 0:
      continue
    if x % i == 0:
      factors.append(i)
  print(factors)

# ex3
#  Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
for i in l:
  print_factor(i)