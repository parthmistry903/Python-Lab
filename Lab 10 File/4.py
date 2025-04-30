# Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.
import os
import shutil
os.makedirs('new_subdir', exist_ok=True)
shutil.copyfile('source_sub Ascending'/'source_subdir/source.txt', 'new_subdir/destination.txt')