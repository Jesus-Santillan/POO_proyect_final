from PIL import ImageTk, Image
import tkinter as tk
import os

class LoginApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Inicio de sesión")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.resizable(True,True)
        self.root.update()
        
        #Fondo
        img = ImageTk.PhotoImage(Image.open("img_f.jpg"))  
        l=tk.Label(image=img)
        l.pack()
        #.place(x = 0, y = 0)
        
        #Encabezado
        frame = tk.Frame(root,bg="lightblue",width=self.root.winfo_width(),height=40)
        frame.pack(side=tk.TOP,fill=tk.X)
        frame.config(cursor="circle")
        frame_mb = tk.Frame(root,bg="white",width=self.root.winfo_width(),height=80)
        frame_mb.pack(side=tk.TOP,fill=tk.X)
        tk.Label(frame_mb, text="Bienvenido al sistema", font=("Arial",16,"bold"),bg="white").place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_campo = tk.Frame(root,bg="white",width=100,height=300)
        frame_campo.pack(fill="both",expand=True,padx=20,pady=(40,0))
def iniciar():    
    root=tk.Tk()
    LoginApp(root)
    root.mainloop()
    