# Necessary Imports
import os
import re
import sys
import webbrowser

# Add the directory containing the modules to the system path
#sys.path.append(r'C:\Users\hasee\Desktop\Work\TechDev\pdfFileManager')

# Includes
from rename_pdf_remove_special_chars import rename_pdfs_remove_special_chars
from rename_pdfs_remove_date import rename_pdfs_remove_date
from rename_pdfs_to_lowercase_except_first import rename_pdfs_to_lowercase_except_first
from search_pdf_names_in_browser import search_pdf_names_in_browser

# Define the PDF folder path
pdf_folder_path = r'c:\Users\hasee\Desktop\Work\References\pdfs\NewFP'

# Rename the PDF files
print("Starting to remove dates from PDF filenames...")
rename_pdfs_remove_date(pdf_folder_path)
print("Finished removing dates from PDF filenames.")

print("Starting to remove special characters from PDF filenames...")
rename_pdfs_remove_special_chars(pdf_folder_path)
print("Finished removing special characters from PDF filenames.")

print("Starting to rename PDF filenames to lowercase except the first character...")
rename_pdfs_to_lowercase_except_first(pdf_folder_path)
print("Finished renaming PDF filenames to lowercase except the first character.")

# Search the PDF file names in the browser
print("Starting to search PDF filenames in the browser...")
search_pdf_names_in_browser(pdf_folder_path)
print("Finished searching PDF filenames in the browser.")