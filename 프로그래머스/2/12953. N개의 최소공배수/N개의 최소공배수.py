from math import gcd
from functools import reduce, cmp_to_key

def solution(arr):
    answer = 0
    
    def get_lcm(a, b):
        
        return (a*b) // gcd(a, b) # 두수의 곱 // 최대공약수 = 최소공배수
    

    answer = reduce(get_lcm, arr)
    
    return answer