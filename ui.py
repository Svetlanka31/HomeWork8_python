import logger
import model

while True:
    mode = model.selection_mode()
    if mode == 1: # режим добавления данных
        logger.write_new_data(model.get_data())

    elif mode == 2: # режим поиска данных
        print(model.data_search(logger.read_data()))

    elif mode == 3: # режим вывода данных
        print(logger.read_data())

    elif mode == 4: # режим редактирования данных
        old_data = model.data_search(logger.read_data())
        print(old_data)
        while old_data.count('\n') > 0:
            print('Уточните критерии поиска, для редактирования записи конкретного сотрудника')
            old_data = model.data_search(old_data)
            print(old_data)
        new_data = model.editing_data(old_data)
        logger.editing('employee_base.txt', old_data, new_data)

    elif mode == 0: 
        print('Работа закончена')
        break
