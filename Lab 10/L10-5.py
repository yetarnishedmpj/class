src_file = 'lowercase.txt'
dest_file = 'uppercase.txt'

with open(src_file, 'r') as src:
    content = src.read().upper()

with open(dest_file, 'w') as dest:
    dest.write(content)
print("Contents copied with uppercase transformation.")
