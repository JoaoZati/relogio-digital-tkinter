import tkinter as tk
from datetime import datetime

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

        self.tempo=datetime.now()
        self.hora = self.tempo.strftime('%H:%M:%S')
        self.dia_semana = self.tempo.strftime("%A")
        self.dia = self.tempo.day
        self.mes = self.tempo.strftime("%B")
        self.ano = self.tempo.strftime("%y")
        print(self.hora, self.dia_semana, self.dia, self.mes, self.ano)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    relogio = RelogioDigital()
    relogio.run()
