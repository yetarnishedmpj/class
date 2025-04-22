def convert(s):
    words = s.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return " ".join(sorted_words)

s = input("Enter your string:")
print(convert(s))