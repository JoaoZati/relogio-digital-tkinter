import tkinter as tk

COR1 = "#3d3d3d"  # preta
COR2 = "#fafcff"  # branca
COR3 = "#21c25c"  # verde
COR4 = "#eb463b"  # vermelha
COR5 = "#dedcdc"  # cinza
COR6 = "#3080f0"  # azul


class RelogioDigital:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x180")
        self.window.resizable(0, 0)
        self.window.config(bg=COR1)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    relogio = RelogioDigital()
    relogio.run()
