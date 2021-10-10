from generators import file_manipulation

files = file_manipulation.fileList()
fils = files.generator("C://Users/pc/Documents/My projects/PYTHON/python sctipts", ".py", True)
print(fils)
