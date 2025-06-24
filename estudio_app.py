import tkinter as tk
import datetime
import winsound


tecnicas = {
    "Pomodoro (25/5)": (25*60, 5*60),
    "52/17": (52*60, 17*60),
    "Bloques de 1 hora": (60*60, 0),
    "Cuenta regresiva (90 min)": (90*60, 0),
    "biip":(5,0)
}

class EstudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temporizador de Estudio")
        self.root.geometry("350x200")
        self.root.configure(bg="#2c3e50")

        self.tecnica_var = tk.StringVar(value="Pomodoro (25/5)")
        self.tiempo_restante = 0
        self.en_curso = False

        tk.Label(root, text="Técnica:", fg="white", bg="#2c3e50").pack()
        tk.OptionMenu(root, self.tecnica_var, *tecnicas).pack()

        self.reloj = tk.Label(root, text="00:00", font=("Arial", 36), fg="white", bg="#2c3e50")
        self.reloj.pack(pady=10)

        self.boton = tk.Button(root, text="Iniciar", command=self.iniciar_sesion)
        self.boton.pack(pady=5)

        self.root.wm_attributes("-alpha", 0.95)

    def iniciar_sesion(self):
        if not self.en_curso:
            estudio, descanso = tecnicas[self.tecnica_var.get()]
            self.tiempo_restante = estudio
            self.en_curso = True
            self.actualizar_tiempo()
            self.boton.config(text="Terminar")
           

        else:
            self.guardar_historial()
            self.en_curso = False
            self.reloj.config(text="00:00")
            self.boton.config(text="Iniciar")
            (datetime.datetime.now().isoformat())

    def actualizar_tiempo(self):
        if self.en_curso and self.tiempo_restante > 0:
            minutos = self.tiempo_restante // 60
            segundos = self.tiempo_restante % 60
            self.reloj.config(text=f"{minutos:02}:{segundos:02}")
            self.tiempo_restante -= 1
            self.root.after(1000, self.actualizar_tiempo)
        elif self.en_curso:
            self.reloj.config(text="¡Tiempo!")
            winsound.Beep(2000, 2*1000)  # Frecuencia 1000 Hz, duración 500 ms
            #winsound.PlaySound("ruta/del/sonido.wav", winsound.SND_FILENAME)

            self.boton.config(text="Iniciar")
            self.en_curso = False
            self.guardar_historial()

    def guardar_historial(self):
        with open("historial_estudio.txt", "a") as archivo:
            fecha = datetime.date.today().isoformat()
            tecnica = self.tecnica_var.get()
            archivo.write(f"{fecha},{tecnica}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = EstudioApp(root)
    root.mainloop()
