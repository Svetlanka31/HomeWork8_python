  # функция выбора режима работы
def selection_mode():
    print('Режимы работы с данными:')
    print('1. Внесение данных\n\
2. Поиск данных\n\
3. Вывод данных\n\
4. Редактирование данных\n\
0. Выход из программы')
    mode = int(input('Выберите режим работы с данными => '))
    return mode 
    
    # функция внесения данных нового сотрудника
def get_data():
    id = input('Введите id сотрудника:')
    firstname = input(' Введите фамилию сотрудника:')
    name= input('Введите имя сотрудника: ')
    patronymic = input('Введите отчество сотрудника: ')
    phone = input('Введите номер телефона:')
    post = input('Введите должность сотрудника:')
    cost = input(' Введите зарплату сотрудника: ')
    return (f'{id}|| {firstname} || {name} || {patronymic} || {phone} || {post} || {cost}')

# функция поиска данных сотрудника
def data_search(f):
    a = input('Введите данные для поиска: ')
    data = list(filter(lambda x: a in x, f.split('\n')))
    data1 = '\n'.join(data)
    return data1

# функция редактирования данных
def editing_data(s):
    f = list(filter(lambda x: '||' not in x, s.split('||')))
    print('Выберите поле редактирования:\n\
id               -> 0\n\
фамилия              -> 1\n\
фимя          -> 2\n\
отчество         -> 3\n\
номер телефона   -> 4\n\
должность        -> 5\n\
зарплата         -> 6')

    check = int(input('=> '))
    print(f'Текущее значение поля -> {f[check]}')
    new_value = input('Введите новое значение поля -> ')
    f[check] = f' {new_value} '
    new_data = '||'.join(f)
    return new_data