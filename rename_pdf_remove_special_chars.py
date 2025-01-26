import os
import re
import sys


# Function to rename PDF files by removing special characters and replacing them with whitespace
def rename_pdfs_remove_special_chars(pdf_folder_path):
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            new_filename = re.sub(r'[-_]', ' ', filename)
            new_filename = new_filename.replace(',', '')
            old_file_path = os.path.join(pdf_folder_path, filename)
            new_file_path = os.path.join(pdf_folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')
            


def main() -> int:
    pdf_folder_path = r'c:\Users\hasee\Desktop\Work\References\pdfs\NewFP'
    rename_pdfs_remove_special_chars(pdf_folder_path)
    
if __name__ == '__main__':
    sys.exit(main())