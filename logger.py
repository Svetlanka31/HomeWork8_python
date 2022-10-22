# функция записи данных
def write_new_data(a):
    with open('employee_base.txt', 'a', encoding = 'utf-8') as f:
        f.write(f'{a}\n')
    

# функция чтения данных
def read_data():
    with open('employee_base.txt', 'r', encoding = 'utf-8') as f:
        return f.read()

import re
import os

# функция редактирования данных
def editing(file,old_data, new_data):
    with open(file, 'r', encoding = 'utf-8') as f1,open('%s.bak' % file, 'w', encoding = 'utf-8') as f2:
        for line in f1:
            if old_data in line:
                line = line.replace(old_data, new_data)
            f2.write(line)
    os.remove(file)
    os.rename('%s.bak' % file, file)
   
