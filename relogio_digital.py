import tkinter as tk
from datetime import datetime
import pyglet

pyglet.font.add_file('digital-7.ttf')

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

        self.window.rowconfigure(0, weight=3)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.label_1 = tk.Label(self.window, text="00:00:00", font=('ds-digital', 80),
                                bg=COR1, fg=COR6)
        self.label_1.grid(row=0, column=0, padx=0, pady=0)

        self.label_2 = tk.Label(self.window, text="00:00:00", font=('ds-digital', 20),
                                bg=COR1, fg=COR6)
        self.label_2.grid(row=1, column=0, sticky='nw', padx=0)

        self.relogio()

    def relogio(self):
        tempo = datetime.now()
        hora = tempo.strftime('%H:%M:%S')
        dia_semana = tempo.strftime("%A")
        dia = tempo.day
        mes = tempo.strftime("%B")
        ano = tempo.strftime("%y")

        self.label_1.config(text=hora)
        self.label_2.config(text=f"{dia_semana} - {dia}/{mes}/{ano}")
        self.label_1.after(200, self.relogio)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    relogio = RelogioDigital()
    relogio.run()
