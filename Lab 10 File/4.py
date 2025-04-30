# Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.
import os
import shutil

os.makedirs("new_subdir", exist_ok=True)
shutil.copy("other_subdir/file.txt", "new_subdir/file.txt")