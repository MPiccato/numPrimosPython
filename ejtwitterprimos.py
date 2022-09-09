from math import sqrt;

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print([i for i in range(100) if es_primo(i)])