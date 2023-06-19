print(all_text)

# Open the Word document
doc = docx.Document(r"P:\IT\PROGETTI\LETTURA PDF\Sample.docx")

# Get the text from the document
doc_text = '\n'.join([para.text for para in doc.paragraphs])

# Split the texts into words
words1 = doc_text.split()
words2 = all_text.split()

# Get the differences between the words
differences = difflib.ndiff(words1, words2)


# Join the differences back into a string
diff_text = ' '.join([diff[2:] for diff in differences if diff.startswith('+ ') or diff.startswith('- ')])

# Print the differences

print("\nThe following words are different:")
differing_words = [word for word in diff_text.split()]

for word in differing_words:
    print(f'- {word}')


# Save differing words in a Word file
output_path = r"P:\IT\PROGETTI\LETTURA PDF\Differences.docx"

output_doc = docx.Document()
output_doc.add_paragraph("Differences between PDF and Word document:")

# Create a bulleted list
list_paragraph = output_doc.add_paragraph()
list_paragraph.style = output_doc.styles["List Bullet"]

for word in differing_words:
    list_paragraph.add_run(f"{word}\n")

output_doc.save(output_path)

print(f"\nDifferences saved to: {output_path}")
