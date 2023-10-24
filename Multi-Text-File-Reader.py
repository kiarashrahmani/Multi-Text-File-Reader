# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:51:07 2023

@author: Kiarash Rahmani
"""

import os

# Directory path containing the text files
directory_path = r'E:\Study\University\codes\Jupyter\Preprocessing in NLP\Preprocessing-Methods-NLP\Corpora'

# Initialize a list to store the text from each file
text_list = []

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            text = file.read()
            text_list.append(text)

# The list text_list will now contain the text from all the .txt files in the directory
print(text_list)