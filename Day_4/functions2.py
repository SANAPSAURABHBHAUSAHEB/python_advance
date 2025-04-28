
def is_odd_or_even(num: int) -> bool:
    return num%2 == 0

def is_prime(num: int) -> bool:
    is_prime = False
    for i in range(2, (num//2)+1, 1):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    else:
        return is_prime

def factorial(num: int) -> int:
    """Calculate the factorial of a non-negative integer n."""
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer.")
    if num == 0:
        return 1
    return num * factorial(num - 1)