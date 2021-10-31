n = int(input('enter the number that you want to find the sigma of: '))
p = 1
nMultiples = []
while p < n + 1 :
  if n % p == 0: 
   
    nMultiples.append(p)

    p = p + 1
  else:  
    p = p + 1   
i = len(nMultiples) 
if i == 2: 
  print(f"{n} is prime!")
sigmaN = sum(nMultiples)
print(f"the sigma of {n} is {sigmaN}")
