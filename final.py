# создаем словарь для хранения данных о заметке вводимые пользователем
note = {}

#Объявление переменных от ввода пользователя
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите содержимое Вашей заметки: ")
note["status"] = input("Введите статус вашей заметки (например 'активна', 'выполнено','в работе': ")
note["created_date"] = input("Введите дату создания в формате 'число-месяц': ")
note["issue_date"] = input("Введите дату истечения срока заметки: ")


#Запрашиваем несколько заголовков и добавляем их в список
note["titles"] = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)


#Выводим данные внесенные пользователем
print("-------------------------------")
print('\nВы ввели следующие данные:')
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
