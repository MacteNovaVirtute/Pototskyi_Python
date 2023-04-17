from tkinter import *

enteredarray = []
arrdivedeby3 = []
error = "Значение не явлется числом либо числа не указаны через кому"

def entered_array():
    while True:
        try:
            global enteredarray
            global arrdivedeby3
            arrdivedeby3 = []
            input = input_data.get()
            enteredarray = list(map(int, input.split(",")))
            return enteredarray
        except ValueError:
            global error
            return error

def divided_by3():
    global error
    if entered_array() != error:
        for i in enteredarray:
            if i % 3 == 0:
                arrdivedeby3.append(i)
        return arrdivedeby3
    else:
        return entered_array()



def answer():
    display_entered.delete(0, END)
    display_entered.insert(0, entered_array())
    display_dividedby3.delete(0, END)
    display_dividedby3.insert(0, divided_by3())
    input_data.delete(0, END)


ws = Tk()
ws.title('Task3')
ws.geometry('800x500')
ws.config(bg='#0f4b6e')

input_data = Entry(ws, justify=CENTER, font=('Arial', 16), width=55)


lbl = Label(
    ws,
    text='Введите числа через кому: ',
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

lbl2 = Label(
    ws,
    text='Числа котороые вы ввели: ',
    bg='#0f4b6e',
    fg='white',
    font=('Arial', 16)
)

lbl2.pack(pady=20)


display_entered = Entry(
    ws,
    width=55,
    font=('Arial', 16),
    justify=CENTER
    )

display_entered.pack(pady=5)

lbl3 = Label(
    ws,
    text='Те которые делятся на три: ',
    bg='#0f4b6e',
    fg='white',
    font=('Arial', 16)
)

lbl3.pack(pady=20)

display_dividedby3 = Entry(
    ws,
    width=55,
    font=('Arial', 16),
    justify=CENTER
    )

display_dividedby3.pack(pady=5)


ws.mainloop()