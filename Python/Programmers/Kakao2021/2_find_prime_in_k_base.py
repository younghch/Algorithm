'''
https://programmers.co.kr/learn/courses/30/lessons/92335
'''
def solution(n, k):
    counts = 0
    
    target_numbers = split_k_base(n, k)
    for target in target_numbers:
        if not target:
            continue
        if is_prime(int(target)):
            counts += 1
    return counts

def split_k_base(n, k):
    base_k = []
    mod = n%k
    n = (n-mod)//k
    base_k.append(str(mod))
    
    while n != 0:
        mod = n%k
        n = (n-mod)//k
        base_k.append(str(mod))
    return ''.join(base_k[::-1]).split('0')

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num == 1:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True