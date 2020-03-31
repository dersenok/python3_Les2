# Алгоритм Евклида
# variant1
# def gcd(m, n):
#    while m !=n:
 #       if m > n:
  #          m -= n
   #     else:
    #        n -= m
    #return m

#print(gcd(55, 39))

1#########################################################

# Variant2

# def gcd2(m, n):
  #  if n == 0:
   #     return m
    #return gcd2(n, m % n)
#print(gcd2(540, 287598372956))

2##########################################################

#Variant3

def gcd3(m, n):
        while n != 0:
            m, n = n, m % n
        return m
print(gcd3(540, 28759837295678976989869869))