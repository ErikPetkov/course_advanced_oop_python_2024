from math import sqrt
def get_primes(nums):
    for n in nums:
        if n < 2:
            continue
        for i in range(2,int(sqrt(n))+1):
                if n%i ==0:
                    break
        else:
            yield n
