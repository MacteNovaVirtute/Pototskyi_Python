from tkinter import *





def check_int():
    try:
        int(input_data.get())
    except ValueError:
        if input == "Вячеслав":
            display = "Привет"
            return display
        else:
            display = "Нет такого имени"
            return display

def check_data():
        input = input_data.get()
        if check_int() == None:
            display = "Вы должны вводить только буквы"
        elif input == "Вячеслав":
            display = "Привет"
        else:
            display = "Нет такого имени"
        return display




def answer():
    display_data.delete(0, END)
    display_data.insert(0, check_data())
    input_data.delete(0, END)

ws = Tk()
ws.title('Task2')
ws.geometry('550x250')
ws.config(bg='#0f4b6e')

input_data = Entry(ws, justify=CENTER, font=('Arial', 16))


lbl = Label(
    ws,
    text='Введите число:',
    bg='#0f4b6e',
    fg='white',
    font=('Arial', 16)
)

lbl.pack(pady=20)
input_data.pack(pady=5)


btn = Button(
    ws,
    text='Проверить',
    relief=SOLID,
    command=answer,
    font=('Times New Roman', 14)

)
btn.pack(pady=5)



display_data = Entry(
    ws,
    width=40,
    font=('Arial', 16),
    justify=CENTER
    )

display_data.pack(pady=5)


ws.mainloop()