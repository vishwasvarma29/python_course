'''import os 
if not os.path.exists('python files'):
    os.mkdir('python files')


import shutil
if not os.path.exists('python files'):
    os.mkdir('python files')
shutil.rmdir('python files')
print(os.getcwd())'''



file= open ('demo.txt', 'r')
print(file.read())