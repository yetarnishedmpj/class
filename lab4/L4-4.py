n = 153

# Prime
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
print("Prime:", is_prime)

# Perfect
is_perfect = sum(i for i in range(1, n) if n % i == 0) == n
print("Perfect:", is_perfect)

# Armstrong
is_armstrong = sum(int(d) ** len(str(n)) for d in str(n)) == n
print("Armstrong:", is_armstrong)

# Palindrome
is_palindrome = str(n) == str(n)[::-1]
print("Palindrome:", is_palindrome)

# Automorphic
is_automorphic = str(n * n).endswith(str(n))
print("Automorphic:", is_automorphic)
