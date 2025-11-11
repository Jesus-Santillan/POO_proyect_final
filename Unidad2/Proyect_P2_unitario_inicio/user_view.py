import tkinter as tk
import user_controller as uc
from tkinter import messagebox,ttk

class UserApp:
    def __init__(self,usuario):
        self.username=usuario
        self.root=tk.Tk()
        self.root.title(f"Bienvenido {usuario}")
        self.root.geometry("800x500")
        self.root.resizable(True,True)
        self.crear_elementos()
        self.ver_usuarios()
        self.root.mainloop()  
    def OnClick(self, event):
        #Ver si el click se hizo en la columna espesifica
        #hacer proceso
        id_colmn=self.tree.identify_column(event.x)
        if id_colmn=='#3':
            self.actualizar_usuarios(self.tree.item(id_colmn,"Username"),self.tree.item(id_colmn,"ID"))
         
    def crear_elementos(self):
        tk.Label(self.root,text=f"hola {self.username}",font=("Arial",22,"bold")).pack(pady=10)
        tk.Button(self.root,text="Agregar usuarios", command=self.agregar_usuarios, width=20).pack(pady=10)
        tk.Button(self.root,text="Actualizar usuarios", command=self.actualizar_usuarios, width=20).pack(pady=10)
        tk.Button(self.root,text="Eliminar usuarios", command=self.eliminar_usuarios , width=20).pack(pady=10)
        tk.Button(self.root,text="Cerrar sesión", width=50,command=self.cerrar_sesion).pack(pady=20)
        
        
        
    def ver_usuarios(self):
        #Creacion de tablas para ver usuarios
        self.tree=ttk.Treeview(self.root, columns=("ID","Username","A1","A2"),height=10,show="headings")
        self.tree.heading("ID",text="ID usuario")
        self.tree.heading("Username",text="Nombre del usuario")
        self.tree.heading("A1",text="Accion 1")
        self.tree.heading("A2",text="Accion 2")
        self.tree.pack(padx=10,pady=9,fill="both",expand=True)
        self.tree.column("ID", anchor=tk.CENTER)
        self.tree.column("Username", anchor=tk.CENTER)
        self.tree.column("A1", anchor=tk.CENTER)
        self.tree.column("A2", anchor=tk.CENTER)
        for (us_nomb,ID_us) in uc.ver_usuarios():
            self.tree.insert('',0,text="",values=(us_nomb,ID_us,"Actualizar","Eliminar"))
        self.tree.bind("<Button-1>", self.OnClick)
                
    def agregar_usuarios(self):
        def guardar():
            u = entry_user.get().strip()
            p = entry_pass.get().strip()
            if not u or not p:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if uc.crear_usuarios(u, p):
                messagebox.showinfo("Éxito", f"Usuario {u} creado correctamente.")
                self.tree.delete(*self.tree.get_children())
                for (us_nomb,ID_us) in uc.ver_usuarios():
                    self.tree.insert('',0,text="",values=(us_nomb,ID_us,"Actualizar","Eliminar"))
                self.tree.bind("<Button-1>", self.OnClick)
                self.root.update()    
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.")
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Usuario")
        ventana.geometry("300x200")
        tk.Label(ventana, text="Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)
         
    def actualizar_usuarios(self,n_usuario,ID):
        def guardar():
            us = entry_user.get().strip()
            passwa = entry_actpass.get().strip()
            passw = entry_pass.get().strip()
            if not us or not passw:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if uc.actualizar_usuarios(ID,us,passwa,passw):#Cambiar a usuarios segun se pulse.
                messagebox.showinfo("Éxito", f"Usuario correctamente.")
                self.ver_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.")
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Usuario")
        ventana.geometry("300x280")
        tk.Label(ventana, text="Usuario").pack(pady=(20,5))
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        if n_usuario!=None:
            entry_user.insert(0,n_usuario)
        else:
            messagebox.showwarning("No se selecciono un usuario", "Teclea el usuario y los demas campos.")    
        tk.Label(ventana, text="Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)
        tk.Label(ventana, text="Contraseña actual").pack(pady=5)
        entry_actpass = tk.Entry(ventana, show="*")
        entry_actpass.pack(pady=10)
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10) 
    def eliminar_usuarios(self):
        def guardar():
            us = entry_pass.get().strip()
            
        opc=messagebox.askquestion('Antes de continuar...', '¿Estas seguro de que quieres eliminar este usuario?')
        if opc=='yes':
            ventana = tk.Toplevel(self.root)
            ventana.title("Eliminar Usuario")
            ventana.geometry("300x100")
            tk.Label(ventana, text="Verifica tu contraseña").pack(pady=5)
            entry_pass = tk.Entry(ventana)
            entry_pass.pack(pady=5)
            tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10) 
        else:
            messagebox.showinfo('Ok', 'Accion abortada')
    def cerrar_sesion(self):
        if messagebox.askokcancel("Antes de irte...","Estas seguro de que quieres cerrar tu sesión?"):
            self.root.destroy()  