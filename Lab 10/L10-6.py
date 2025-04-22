file1 = 'file1.txt'
file2 = 'file2.txt'
outfile = 'merged.txt'

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(outfile, 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    
    for l1, l2 in zip(lines1, lines2):
        out.write(l1.strip() + '\n')
        out.write(l2.strip() + '\n')
    
    remaining = lines1[len(lines2):] if len(lines1) > len(lines2) else lines2[len(lines1):]
    out.writelines(remaining)
print("Files merged alternately.")
