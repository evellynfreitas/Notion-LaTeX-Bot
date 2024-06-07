from tkinter import *
from tkinter import colorchooser


def escolhe_cor():
    codigo = colorchooser.askcolor(title="Escolha uma cor")[1]
    texto.config(foreground=codigo)


def escolhe_fundo():
    codigo = colorchooser.askcolor(title="Escolha uma cor")[1]
    texto.config(background=codigo)


def escolhe_texto():
    texto.config(text=entrada.get())


app = Tk()
app.title("LaTeX Bot")
app.geometry("300x300")

entrada = StringVar()

texto = Label(app, text="Texto")
texto.pack()

input_texto = Entry(app, textvariable=entrada)
input_texto.pack()

botao1 = Button(app, text="Enviar texto", command=escolhe_texto)
botao1.pack()

botao2 = Button(app, text="Escolha uma cor", command=escolhe_cor)
botao2.pack()

botao3 = Button(app, text="Escolha a cor do fundo", command=escolhe_fundo)
botao3.pack()

texto1 = Label(app, text="your text here")
texto1.pack()
texto1.configure(font=("French Script MT", 22))


texto2 = Label(app, text="your text here")
texto2.pack()
texto2.configure(font=("bodoni mt", 20))


texto3 = Label(app, text="your text here")
texto3.pack()
texto3.configure(font=("courier", 20))


texto3 = Label(app, text="your text here")
texto3.pack()
texto3.configure(font=("Microsoft JhengHei", 20))


app.mainloop()
