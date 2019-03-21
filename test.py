Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openpyxl
>>> wb=openpycl.load_workbook('example.xlsx')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    wb=openpycl.load_workbook('example.xlsx')
NameError: name 'openpycl' is not defined
>>> wb=openpyxl.load_workbook('example.xlsx')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    wb=openpyxl.load_workbook('example.xlsx')
  File "C:\Users\liuto\AppData\Local\Programs\Python\Python37\lib\site-packages\openpyxl\reader\excel.py", line 311, in load_workbook
    data_only, keep_links)
  File "C:\Users\liuto\AppData\Local\Programs\Python\Python37\lib\site-packages\openpyxl\reader\excel.py", line 126, in __init__
    self.archive = _validate_archive(fn)
  File "C:\Users\liuto\AppData\Local\Programs\Python\Python37\lib\site-packages\openpyxl\reader\excel.py", line 98, in _validate_archive
    archive = ZipFile(filename, 'r')
  File "C:\Users\liuto\AppData\Local\Programs\Python\Python37\lib\zipfile.py", line 1204, in __init__
    self.fp = io.open(file, filemode)
FileNotFoundError: [Errno 2] No such file or directory: 'example.xlsx'
>>> 
