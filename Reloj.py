import tkinter as tk
import keyboard 

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.segundos = 0
        self.minutos = 0
        self.run = False
        self.display = tk.StringVar()
        self.actualizar_display("00:00")
        self.master.title("Cronómetro")
        self.master.config(bg="black")
        self.master.geometry("300x100+1630+0")
        self.master.resizable(False, False)
        self.master.wm_attributes("-topmost", True)
        #self.master.wm_overrideredirect(True)  # Elimina la barra de título de la ventanao
        #self.master.wm_attributes("-transparentcolor", "black")  # transparente XD
        self.master.wm_attributes("-alpha", 0.9)

        self.display_label = tk.Label(master, textvariable=self.display,bg="black", font=("Arial", 48), fg="white")
        self.display_label.pack()
        self.boton_frame = tk.Frame(master, bg="black")
        self.boton_frame.pack()

        while True:
            if keyboard.is_pressed('7'):
                self.iniciar()
            elif keyboard.is_pressed('8'):
                self.detener()
            elif keyboard.is_pressed('9'):
                self.reiniciar()
            elif keyboard.is_pressed('0'):
                self.master.destroy()
                break
            self.master.update_idletasks()
            self.master.update()
    

      



    def actualizar_display(self, tiempo):
        self.display.set(tiempo)
         
    def iniciar(self):
        if not self.run:
            self.run = True
            self.mostrar_tiempo()

    def detener(self):
        self.run = False 

    def reiniciar(self):
        self.segundos = 0
        self.minutos = 0
        self.actualizar_display("00:00")
   
   
    def mostrar_tiempo(self):
        if self.run:
            self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
            tiempo_formateado = f"{self.minutos:02}:{self.segundos:02}"
            self.actualizar_display(tiempo_formateado)
            self.master.after(1000, self.mostrar_tiempo)


if __name__ == "__main__":
    ventana = tk.Tk()
    cronometro = Cronometro(ventana)
 
    ventana.mainloop()