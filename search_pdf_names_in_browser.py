import os
import re
import sys
import webbrowser

# Function to read the names of the PDF files and search them in the browser
def search_pdf_names_in_browser(pdf_folder_path):
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            # Remove the file extension for the search query
            search_query = os.path.splitext(filename)[0]
            # Create the search URL
            search_url = f"https://www.google.com/search?q={search_query}"
            # Open the search URL in a new tab in the default web browser
            webbrowser.open_new_tab(search_url)
            print(f'Searched: {search_query}')
            

def main() -> int:
    pdf_folder_path = r'c:\Users\hasee\Desktop\Work\References\pdfs\NewFP'
    search_pdf_names_in_browser(pdf_folder_path)

if __name__ == '__main__':
    sys.exit(main())