# Task 5: Filter faculty names with more than 8 characters
faculty_names = ["Dr. Anderson", "Lee", "Dr. Catherine", "John", "Maximilian"]
long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print("Faculty names with more than 8 characters:", long_names)