import tkinter as tk
from auth_controller import validar_credenciales
from tkinter import messagebox
from user_view import UserApp

class LoginApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Inicio de sesión")
        self.root.geometry("600x460")
        self.root.resizable(True,True)
        self.root.update()
        
        #Encabezado
        frame = tk.Frame(root,bg="lightblue",width=self.root.winfo_width(),height=40)
        frame.pack(side=tk.TOP,fill=tk.X)
        frame.config(cursor="circle")
        frame_mb = tk.Frame(root,bg="white",width=self.root.winfo_width(),height=80)
        frame_mb.pack(side=tk.TOP,fill=tk.X)
        tk.Label(frame_mb, text="Bienvenido al sistema", font=("Arial",16,"bold"),bg="white").place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_campo = tk.Frame(root,bg="white",width=100,height=300)
        frame_campo.pack(fill="both",expand=True,padx=20,pady=(40,0))
        #Campos de texto
        tk.Label(frame_campo,text="Ingresa tu nombre de usuario",bg="white").pack(pady=(54,10))
        self.username_entry=tk.Entry(frame_campo,bg="#F5F5F5")
        self.username_entry.pack(pady=5)
        tk.Label(frame_campo,text="Ingresa tu contraseña",bg="white").pack(pady=(10,10))
        self.password_entry=tk.Entry(frame_campo,show="*",bg="#F5F5F5")
        self.password_entry.pack(pady=5)
        
        #Boton
        tk.Button(frame_campo, text="Iniciar sesión",command=self.login).pack(pady=20)
        
    def login(self):
        usuario=self.username_entry.get().strip()
        password=self.password_entry.get().strip()
        if not (usuario and password):
            messagebox.showinfo(title="Ups... algo salio mal *^* ",message="Faltan datos. Favor de ingresar usuario y contraseña")
        
        if validar_credenciales(usuario,password):
            messagebox.showinfo(title="Acceso permitido",message=f"Bienvenido {usuario}")
            self.root.destroy()
            UserApp(usuario)
        else:
            messagebox.showerror(title="Accesso denegado",message=" tus credenciales son incorrectas")
def iniciar():    
    root=tk.Tk()
    app=LoginApp(root)
    root.mainloop()