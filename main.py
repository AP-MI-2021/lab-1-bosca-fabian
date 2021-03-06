'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n < 2:
    return False
  for i in range(2,n//2+1):
    if n % i == 0:
      return False
  return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs = 1
  for i in lst:
    produs *= i
  return produs
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x != y:
    if x > y:
      x -= y
    else:
      y -= x
  return x
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  if y > x:
    x, y = y, x
  while y != 0:
    rest = x % y
    x = y
    y = rest
  return x
  
  
def main():
  n = int(input("Dati posibilul numar prim:"))
  print(is_prime(n))
  list = []
  number_of_elements = int(input("Introduceti numarul de elemente ale listei:"))
  for i in range(0,number_of_elements):
    number = int(input("Introduceti element:"))

    list.append(number)
  print(get_product(list))
  x = int(input("Primul numar pentru CMMDC:"))
  y = int(input("Al doilea numar pentru CMMDC:"))
  print("CMMDC_v1:",get_cmmdc_v1(x, y))
  print("CMMDC_v2:",get_cmmdc_v2(x, y))

if __name__ == '__main__':
  main()
