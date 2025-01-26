import os
import re
import sys

def rename_pdfs_to_lowercase_except_first(pdf_folder_path):
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            new_filename = filename[0] + filename[1:].lower()
            old_file_path = os.path.join(pdf_folder_path, filename)
            new_file_path = os.path.join(pdf_folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

def main() -> int:
    pdf_folder_path = r'c:\Users\hasee\Desktop\Work\References\pdfs\NewFP'
    rename_pdfs_to_lowercase_except_first(pdf_folder_path)
    
if __name__ == '__main__':
    sys.exit(main())