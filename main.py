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
    assert get_largest_prime_below(15) == 5
    assert get_largest_prime_below(6) == 3
    assert get_largest_prime_below(21) == 7
def test_get_base_2():
    assert get_base_2(2) == 10
    assert get_base_2(8) == 100
    assert get_base_2(16) == 1000
def test_is_antipalindrome():
    assert is_antipalindrome(2345) == True
    assert is_antipalindrome(2334) == False
    assert is_antipalindrome(17587) == True


def main():

    while True:
        print("Optiuni: ")
        print("1. Găsește ultimul număr prim mai mic decât un număr dat")
        print("2. Din baza 10 in baza 2")
        print("3. Verifica daca numarul este antiplaindrom")
        print("4. Terminarea programului")
        option = input("scrie nr. optiuni: ")
        if option == 1:
            n = input("introdu numarul")
            get_largest_prime_below(n)
        if option == 2:
            n = input("introdu numarul")
            get_base_2(n)
        if option == 3:
            n = input("introdu numarul")
            is_antipalindrome(n)
        if option == 4:
            break



if __name__ == '__main__':
    test_get_largest_prime_below()
    test_get_base_2()
    test_is_antipalindrome()

    main()




