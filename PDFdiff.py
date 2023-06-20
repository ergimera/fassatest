# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:37:09 2023
"""

import streamlit as st
from PyPDF2 import PdfReader
import docx
import os
from io import BytesIO

# Streamlit app title and description
st.title("PDF and Word Comparison")
st.write("Select the PDF file and Word document to compare and download the differences.")

# Choose the PDF file
pdf_file = st.file_uploader("Select PDF File", type="pdf")
if pdf_file is not None:
    reader = PdfReader(pdf_file)

    # Choose the Word document
    word_file = st.file_uploader("Select Word Document", type="docx")
    if word_file is not None:
        doc = docx.Document(word_file)

        # List to store extracted text from all pages
        pages_text = []

        # Iterating over all pages and extracting text from PDF
        for page in range(len(reader.pages)-1):
            current_page = reader.pages[page]
            text = current_page.extract_text()
            pages_text.append(text)

        all_text = "\n".join(pages_text)

        # Get the text from the Word document
        doc_text = '\n'.join([para.text for para in doc.paragraphs])

        # Split the texts into words
        words1 = doc_text.split()
        words2 = all_text.split()

        # Get the differences between the words
        differences = set(words2) - set(words1)

        # Print the differences
        st.subheader("Differences:")
        differing_words = list(differences)

        for word in differing_words:
            st.write(f'- {word}')

        # Save differing words in a file
        output_file = st.text_input("Output file name", value="Differences.txt")
        if st.button("Download Differences"):
            if output_file:
                output_filename = output_file.strip()
                output_text = "\n".join(differing_words)
                output_bytes = output_text.encode('utf-8')
                st.download_button(label="Download Differences", data=output_bytes, file_name=output_filename, mime='text/plain')
            else:
                st.error("Please enter a valid output file name.")
