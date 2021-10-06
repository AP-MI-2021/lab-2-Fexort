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

'''
Găsește ultimul număr prim mai mic decât un număr dat.
'''
def get_largest_prime_below(n):

    maxprim = -1


    while n % 2 == 0:
        maxprim = 2
        n = n / 2

    while n % 3 == 0:
        maxprim = 3
        n = n / 3

    for i in range(5, int(n//2) + 1):
        while n % i == 0:
            maxprim = i
            n = n // i
        while n % (i + 2) == 0:
            maxprim = i + 2
            n = n // (i + 2)

    return (maxprim)
def test_get_largest_prime_below():
    n = 15
    print(get_largest_prime_below(n))

def main():

    # interfata de tip consola aici

    if __name__ == '__main__':
        main()



