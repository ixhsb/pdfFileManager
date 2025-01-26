# import os
# import re
# import sys


# Function to rename PDF files by removing the date part if it matches the pattern 000000_
def rename_pdfs_remove_date(pdf_folder_path):
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            # Use regex to match the pattern 6 digits followed by an underscore
            new_filename = re.sub(r'^\d{6}_', '', filename)
            old_file_path = os.path.join(pdf_folder_path, filename)
            new_file_path = os.path.join(pdf_folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')
            

def main() -> int:
    pdf_folder_path = r'c:\Users\hasee\Desktop\Work\References\pdfs\NewFP'
    rename_pdfs_remove_date(pdf_folder_path)
    
if __name__ == '__main__':
    sys.exit(main())