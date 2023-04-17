from tkinter import *

def check_data():

    while True:
        try:
            input = int(input_data.get())
            if input > 7:
                display = "Привет"
            else:
                display = "Что то не то"

        except ValueError:
            display = "Введенное значение не является числом"
        return display

def answer():
    display_data.delete(0, END)
    display_data.insert(0, check_data())
    input_data.delete(0, END)

ws = Tk()
ws.title('Task1')
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