import re

with open('input.txt', 'r') as infile:
    content = infile.read()

updated_content = re.sub(r'\b(a|an|the)\b', ' ', content, flags=re.IGNORECASE)

with open('output.txt', 'w') as outfile:
    outfile.write(updated_content)
print("Articles removed and file created.")
