import os
import subprocess


# Delete existing PDFs
for filename in os.listdir():
	if filename.endswith('.pdf'):
		os.remove(filename)


# Compile PDFs
for filename in os.listdir():
	if filename.endswith('.tex'):
		subprocess.call(['pdflatex', '-halt-on-error', filename])
		
		
# Clean up
extensions = ('.aux', '.log')
for filename in os.listdir():
	if any(filename.endswith(ext) for ext in extensions):
		os.remove(filename)