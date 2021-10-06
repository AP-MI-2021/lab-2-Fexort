'''
verifica daca numarul este antiplaindrom
'''


def is_antipalindrome(n):
    m=n
    p=1
    while m!=0:
        p=p*10
        m=m//10

    while n:
        if n%10 == n//p:
            return False
        n=n//10
        p=p//10
        n=n%p
    return True





'''
din baza 10 in baza 2
'''


def get_base_2(n):
    m=0
    p=1
    while n:
        r = n%2
        m = m+ r*p
        p = p*10
        n=n//2
    return m




def main():





