import os
import shutil

src_file = 'source_dir/sample.txt'
dest_dir = 'new_dir'

os.makedirs(dest_dir, exist_ok=True)
shutil.copy(src_file, dest_dir)
print(f"File copied to {dest_dir}")
