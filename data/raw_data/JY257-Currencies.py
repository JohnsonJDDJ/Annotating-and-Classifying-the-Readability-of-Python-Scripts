import requests
import xmltodict
from tkinter import *
import tkinter as tk

# Создаем окно верхнего уровня
window = Tk()
window.geometry("400x100")
window.title('Currencies cbr.ru')

# Добавление кнопки закрытия окна
btnClosePopup = tk.Button(window, text="Закрыть", bg='#990000', fg='white', font=('Helvetica', 10, 'bold'), command=window.destroy)
btnClosePopup.place(x=280, y=50, width=110, height=30)

# Парсинг данных с cbr.ru
url = "http://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)
data = xmltodict.parse(response.content)


# Обработчик нажатия кнопки
def process_button():
    my_array = []
    for item in data['Valuta']['Item']:
        my_set = [item['Name'], item['EngName'], item['Nominal'], item['ParentCode']]
        my_array.append(my_set)
        print(my_set)
    popup_window(my_array)


def popup_window(my_array):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("Результат")

    # Добавление окна вывода текста
    txtOutput = tk.Text(window, font=('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)

    # Сформировать строку с данными
    output_str = ""
    for item in my_array:
        output_str += f"Name: {item[0]}\n"
        output_str += f"EngName: {item[1]}\n"
        output_str += f"Nominal: {item[2]}\n"
        output_str += f"ParentCode: {item[3]}\n\n"

    # Вывод строки в окне
    txtOutput.insert(END, output_str)


# Создание кнопки
button = tk.Button(window, text="Парсинг данных", font=('Helvetica', 10, 'bold'), command=process_button)
button.place(x=10, y=50, width=110, height=30)

window.mainloop()


