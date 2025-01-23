#Объявление переменных от ввода пользователя
username = input("Введите имя пользователя: ")              #переменная содержит имя пользователя
text = (f"Привет, {username}!")
print(text.title())                                         #Использовал метод вывода первой буквы имени с большой буквы.
title = input("Введите наименование заголовка заметки: ")   #Переменная содержит заголовок заметки
content = input("Введите содержимое Вашей заметки: ")       # переменная содержит описание заметки
status = input("Введите статус вашей заметки (например 'активна', 'выполнено','в работе': ")            # переменная статуса
created_date = input("Введите дату создания в формате 'число-месяц': ") # дата создания заметки
issue_date = input("Введите дату истечения срока заметки: ")    # дата истечения срока


#Вывод значений переменных
print("___________________________________________________")
print("\nВы записали следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения срока заметки:", issue_date)