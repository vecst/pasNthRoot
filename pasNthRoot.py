import decimal
from functools import reduce

def fact(o):
#creates factorial of number 'o'
    return reduce(lambda x,y: x * y,range(1,o+1)) if o >0 else 1

def pas(r):
# Creates row 'r' of  pascals triangle
    pa=list(range(1,r))
    return [1]+[fact(r) / (fact(x)*fact(r-x)) for x in pa]+[1]

def shuf(a,g):
#takes row 'a' of pascals triangle and selets every gth value starting at 0,
#and 1, and returns two lists
    pa=pas(a)
    return pa[1::g],pa[::g]

def nth(a,g,x):
#takes values 'a', 'g', 'x' a is the pascal row, g is the gth value
#x is the number of the nthroot you are looking for. the function will return x^1/g

#sets the suffled pascal's triangle lists to 'num' and 'den'  set the first
#exponet value to 'n'. use 'i' for crawling through the lists and initialize
# nui and dei as long as the exponet value is greater than and equal to zero
#the function is valid otherwise it will stop and return (nui / dei)
    num,den = shuf(a,g)
    n= len(num)-1
    i = 0
    nui=0
    dei=0
    t= [x**n for n in range(n,0,-1)]
    nui = [b *c  for b,c in zip(num,t)]
    dei = [d *e  for d,e in zip(den,t)]
    return decimal.Decimal(sum(nui)/sum(dei))

print(nth(431,2,2))
