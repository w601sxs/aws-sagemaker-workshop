from yamldirs.filemaker import Filemaker
import os

current_dir = os.getcwd()

with open ("contentmap.yaml", "r") as myfile:
    files=myfile.read()

print(files)

Filemaker(current_dir,files)