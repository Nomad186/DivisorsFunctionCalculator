def sum(lst):
  total = 0
  for i in range(0,len(lst)):
    total += float(lst[i])
  return total

def sigma(num):
  divisors_lst = []
  for i in range(1,num):
    if num % i == 0: #it is divisible
      divisors_lst.append(i)
  return sum(divisors_lst)

def main():
  while True:
    num = int(input('enter the number you would like to find the sigma of : '))
    sigma_n = sigma(num)

    print(f'sigma({num}) = {sigma_n}')


if __name__ == '__main__':
  main()
