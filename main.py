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
        
# --------------------------------------------------------------------- #
# correr_programa inicia el programa (la ventana junto a los widgets) una sola vez para no contar con problemas
def correr_programa():

    # Funciones
    # Sumatoria calcula la sumatoria en base a la expresión que escriba el usuario
    def Sumatoria():
        lblAlerta.configure(text='')
        resultado = 0
        try:
            i = float(txtI.get())
            n = int(txtN.get())

            if(i > n): # Verificar si i es menor que n para continuar con el cálculo
                lblAlerta.configure(text='i debe ser menor o igual que n')
                raise Exception('i es mayor que n')

            expresion = DetectarOperaciones() # Llamar a la función DetectarOperaciones para reescribir la función para que eval pueda interpretarla

            while(i <= n): # Iterar hasta que i llegue a n, mientras se suma el resultado de la ecuación
                try:
                    resultado += eval(expresion, {}, {'i': i})
                # En el dado caso que al evaluar la expresión se intente dividir entre 0 se ignorará el termino correspondiente y continuará con la sumatoria
                except ZeroDivisionError as e: 
                    print(f'Ocurrio un error: {e}')
                    lblAlerta.configure(text=f'Se ignoró el termino i={i.__round__()} por intentar dividir entre 0')
                i+=1
            
            # Imprimir el resultado
            txtResultado.configure(state='normal')
            txtResultado.delete(0, 'end')
            txtResultado.insert(0, str(round(resultado, 2)))
            txtResultado.configure(state='readonly')

        # Manejo de excepciones
        except ValueError as e:
            lblAlerta.configure(text='Ingresa un valor válido')
        except SyntaxError as e:
            lblAlerta.configure(text='Ingresa una expresión válida')
        except Exception as e:
            print(f"Ocurrio un error: {e.__class__}")
            
    # DetectarOperaciones identifica si la ecuación que ingreso el usuario cuenta con caracteres o operaciones que la función eval no maneja (potencias ^),
    # un producto usando paréntesis, o producto usando la variable (Ej: 2i)
    def DetectarOperaciones():
        ecuacion = txtEcuacion.get()
        nueva_ecuacion = ""
        i = 0

        # Se recorrerá por cada caracter de la ecuación y se identificara si la ecuación contiene lo antes mencionado
        while(i < len(ecuacion)):
            nueva_ecuacion += ecuacion[i] # Por cada iteración se guardaran los caracteres en una nueva variable la cual se regresará al final de la función
            try:
                if(ecuacion[i] == '('): # Identificar si la ecuación contiene ( 
                    if(i - 1 >= 0 and ecuacion[i - 1] not in ['*', '+', '-', '/', '^']): # Verificar si antes del caracter no hay un caracter que indique una operación
                        nueva_ecuacion = nueva_ecuacion.replace('(', '*(') # Reemplazar el caracter por lo mismo pero con un * atras
                if(ecuacion[i] == 'i'): # Identificar si la ecuación contiene i
                    if(i - 1 >= 0 and ecuacion[i - 1] not in ['*', '+', '-', '/', '^']): 
                        nueva_ecuacion = nueva_ecuacion.replace('i', '*i') # Reemplazar el caracter por lo mismo pero con un * atras
                if(ecuacion[i] == ')'): # Identificar si la ecuación contiene )
                    if(i + 1 < len(ecuacion) and ecuacion[i + 1] not in ['*', '+', '-', '/', '^']):
                        nueva_ecuacion += '*' # Añadir un * a la nueva ecuación
            except Exception as e:
                print(f'hubo un eror: {e.__class__}')
            i += 1

        if(nueva_ecuacion.__contains__('^')): # Verificar si la ecuación cuenta con una potencia
            nueva_ecuacion = nueva_ecuacion.replace('^', '**') # Reemplazar el ^ por ** para que eval pueda utilizar la ecuación sin problemas

        #print(nueva_ecuacion)

        return nueva_ecuacion
    
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

    ventana.mainloop()

    # --------------------------------------------------------------------- #

if __name__ == "__main__": # Ejecutar el programa
    correr_programa()