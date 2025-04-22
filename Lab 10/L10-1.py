import csv

data = [
    [101, 'Alice', 85, 90, 92],
    [102, 'Bob', 78, 82, 88],
    [103, 'Charlie', 90, 91, 89]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['RollNo', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerows(data)
print("CSV file created.")
