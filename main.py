import customtkinter as tk
import os
import sys

#Instalar dependencias (customtkinter, etc)
def main():
    print("Instalando dependencias...")
    os.system(f"{sys.executable} -m pip install -r requirements.txt")
    print("✔ Instalación completada. Ahora puedes ejecutar el proyecto con:")
    print(f"{sys.executable} main.py")


def resource_path(relative_path):
    """Devuelve la ruta absoluta del recurso, compatible con PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
        
#---------------------------------------------------------------------#
def correr_programa():

    #Funciones
    def Sumatoria():
        lblAlerta.configure(text='')
        resultado = 0
        try:
            i = float(txtI.get())
            n = int(txtN.get())

            if(i > n):
                lblAlerta.configure(text='i debe ser menor o igual que n')
                raise Exception('i es mayor que n')

            expresion = txtEcuacion.get()
            expresion_temp = ''
            if(expresion.__contains__('^')):
                expresion_temp = txtEcuacion.get()
                expresion = expresion_temp.replace('^', '**')

            while(i <= n):
                try:
                    resultado += eval(expresion, {}, {'i': i})
                except ZeroDivisionError as e:
                    print(f'Ocurrio un error: {e}')
                    lblAlerta.configure(text=f'Se ignoró el termino i={i.__round__()} por intentar dividir entre 0')
                i+=1
            
            print(resultado)
            txtResultado.configure(state='normal')
            txtResultado.delete(0, 'end')
            txtResultado.insert(0, str(round(resultado, 2)))
            txtResultado.configure(state='readonly')
        except ValueError as e:
            lblAlerta.configure(text='Ingresa un valor válido')
        except SyntaxError as e:
            lblAlerta.configure(text='Ingresa una expresión válida')
        except Exception as e:
            print(f"Ocurrio un error: {e.__class__}")
            
    #Ventana del programa
    ventana = tk.CTk()
    ventana.geometry("720x380")
    ventana.minsize(720, 380)
    ventana.maxsize(720, 380)
    ventana.wm_title('Sumatorias')
    ventana.iconbitmap(resource_path("GRISpng.ico"))

    #Layout
    canvas = tk.CTkCanvas(ventana, width=720, height=380, bg='white')
    canvas.grid(column=0, row=0)
    canvas.create_rectangle(0, 0, 458, 380, fill="#C0D0C1", outline='#FFFFFF')
    canvas.create_rectangle(0, 0, 458, 70, fill="#4D9560", outline="#FFFFFF")
    canvas.create_rectangle(458, 0, 720, 380, fill="#BAD1C4", outline="#FFFFFF")
    canvas.create_rectangle(458, 0, 720, 70, fill="#82B9A1", outline="#FFFFFF")

    #Etiquetas
    lblOperacion = tk.CTkLabel(ventana, text="Operación", font=('Inter', 36, 'bold'), bg_color='#4D9560', anchor="center", width=132, height=35)
    lblOperacion.place(x=138, y=10)

    lblResultado = tk.CTkLabel(ventana, text="Resultado", font=('Inter', 36, 'bold'), bg_color='#82B9A1', anchor="center", width=177, height=35)
    lblResultado.place(x=501, y=10)

    lblNumN = tk.CTkLabel(ventana, text="n", font=('Inter', 20, 'bold'), bg_color='#C0D0C1', text_color="#000000", anchor="center", width=13, height=28)
    lblNumN.place(x=87, y=107)

    lblSigma = tk.CTkLabel(ventana, text="Σ", font=('Inter', 100, 'bold'), bg_color='#C0D0C1', text_color="#000000", anchor="center", width=66, height=95)
    lblSigma.place(x=60, y=164)

    lblNumI = tk.CTkLabel(ventana, text="i", font=('Inter', 20, 'bold'), bg_color='#C0D0C1', text_color="#000000", anchor="center", width=6, height=28)
    lblNumI.place(x=87, y=304)

    lblAlerta = tk.CTkLabel(ventana, text="", font=('Inter', 16, 'bold'), bg_color='#C0D0C1', anchor="center", text_color="red", width=457, height=32 )
    lblAlerta.place(x=0, y=75)

    #Inputs
    txtN = tk.CTkEntry(ventana, font=('inter', 16), justify='center', width=60, height=30, corner_radius=10, bg_color='#C0D0C1', fg_color="#FFFFFF", text_color="#000000", border_width=0)
    txtN.place(x=63, y=137)

    txtI = tk.CTkEntry(ventana, font=('inter', 16), justify='center', width=60, height=30, corner_radius=10, bg_color='#C0D0C1', fg_color="#FFFFFF", text_color="#000000", border_width=0)
    txtI.place(x=63, y=272)

    txtEcuacion = tk.CTkEntry(ventana, font=('inter', 16), justify='center', width=226, height=41, corner_radius=10, bg_color='#C0D0C1', fg_color="#FFFFFF", text_color="#000000", border_width=0)
    txtEcuacion.place(x=163, y=199)

    txtResultado = tk.CTkEntry(ventana, font=('inter', 25, 'bold'), justify='center', width=219, height=64, corner_radius=10, bg_color='#BAD1C4', fg_color="#FFFFFF", text_color="#000000", border_width=0, state='readonly')
    txtResultado.place(x=479, y=188)

    #Botones
    cmdCalcular = tk.CTkButton(ventana, text="Calcular", font=('inter', 20, 'bold'), fg_color="#FFFFFF", bg_color="#C0D0C1", width=100, height=32, corner_radius=10, text_color="#000000", hover_color="#95a395", command=Sumatoria)
    cmdCalcular.place(x=226, y=272)

    #---------------------------------------------------------------------#

    ventana.mainloop()

if __name__ == "__main__":
    correr_programa()