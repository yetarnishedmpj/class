s = "Hello123"
alpha = sum(c.isalpha() for c in s)
digit = sum(c.isdigit() for c in s)
print("Alphabets:", alpha, "Digits:", digit)
