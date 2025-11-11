import tkinter as tk
from database import crear_conexion
from tkinter import messagebox, ttk

# Funciones de acceso a BD (nombres con sufijo _db para evitar choque con métodos de la clase)
def ver_usuarios_db():
    conexion = crear_conexion()
    if not conexion:
        print("ver_usuarios_db: no se pudo conectar a la BD")
        return []
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT ID, usuario FROM usuarios")
        except Exception:
            cursor.execute("SELECT id_usuario AS id, usuario FROM usuarios")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        print(f"ver_usuarios_db: encontrados {len(resultado)} registros -> {resultado}")
        return resultado
    except Exception as e:
        print(f"Error en ver_usuarios_db: {e}")
        return []

def agregar_usuarios_db(username, password):
    conexion = crear_conexion()
    if not conexion:
        print("agregar_usuarios_db: no se pudo conectar a la BD")
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (%s, %s)", (username, password))
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"agregar_usuarios_db: usuario '{username}' agregado")
        return True
    except Exception as e:
        print(f"Error en agregar_usuarios_db: {e}")
        return False

def actualizar_usuarios_db(id_usuario, new_usuario, new_password):
    conexion = crear_conexion()
    if not conexion:
        print("actualizar_usuarios_db: no se pudo conectar a la BD")
        return False
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET usuario = %s, password = %s WHERE id = %s",
                (new_usuario, new_password, id_usuario)
            )
        except Exception:
            cursor.execute(
                "UPDATE usuarios SET usuario = %s, password = %s WHERE id_usuario = %s",
                (new_usuario, new_password, id_usuario)
            )
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"actualizar_usuarios_db: id={id_usuario} actualizado")
        return True
    except Exception as e:
        print(f"Error en actualizar_usuarios_db: {e}")
        return False

def eliminar_usuarios_db(id_usuario):
    conexion = crear_conexion()
    if not conexion:
        print("eliminar_usuarios_db: no se pudo conectar a la BD")
        return False
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        except Exception:
            cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"eliminar_usuarios_db: id={id_usuario} eliminado")
        return True
    except Exception as e:
        print(f"Error en eliminar_usuarios_db: {e}")
        return False


class UserApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        self.crear_elementos()
        self.mostrar_usuarios()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola, {self.username}",  font=("Arial", 22, "bold")).pack(pady=10)
        tk.Button(self.root, text="Cerrar sesión", width=12, command=self.cerrar_sesion).pack(pady=8)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar usuario", width=18,  command=self.agregar_usuarios).pack(side="left", padx=6, pady=6)
        tk.Button(frame_botones, text="Actualizar usuario", width=18,  command=self.actualizar_usuarios).pack(side="left", padx=6, pady=6)
        tk.Button(frame_botones, text="Eliminar usuario", width=18, command=self.eliminar_usuarios).pack(side="left", padx=6, pady=6)

        tk.Label(self.root, text=f"Lista de usuarios",  font=("Arial", 26, "bold")).pack(pady=10)

        # CREAR TABLA CON TREEVIEW
        self.tree = ttk.Treeview(self.root, columns=("ID", "Usuario"), show="headings", height=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Usuario", width=300)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_usuarios(self):
        try:
            usuarios = ver_usuarios_db()
            # limpiar treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            # insertar filas
            for u in usuarios:
                self.tree.insert("", "end", values=u)
            print(f"mostrar_usuarios: {len(usuarios)} usuarios encontrados")
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            messagebox.showerror("Error", "No se pudieron obtener los usuarios.")
            return []

    def agregar_usuarios(self):
        def guardar():
            username = entry_user.get().strip()
            password = entry_pass.get().strip()
            if not username or not password:
                messagebox.showwarning("Datos faltantes", "Debe llenar todos los campos.")
                return
            if agregar_usuarios_db(username, password):
                messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
                top.destroy()
                self.mostrar_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo agregar el usuario. Revisa la consola.")

        top = tk.Toplevel(self.root)
        top.title("Agregar usuario")
        top.geometry("300x200")

        tk.Label(top, text="Usuario:").pack(pady=5)
        entry_user = tk.Entry(top)
        entry_user.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Contraseña:").pack(pady=5)
        entry_pass = tk.Entry(top, show="*")
        entry_pass.pack(pady=5, fill="x", padx=10)

        tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

    def actualizar_usuarios(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Actualizar", "Seleccione un usuario para actualizar.")
            return

        item = self.tree.item(seleccion[0], "values")
        user_id = item[0]
        user_name = item[1]

        def guardar_cambios():
            nuevo_nombre = entry_user.get().strip()
            nueva_contra = entry_pass.get().strip()
            if not nuevo_nombre or not nueva_contra:
                messagebox.showwarning("Datos faltantes", "Debe llenar todos los campos.")
                return
            if actualizar_usuarios_db(user_id, nuevo_nombre, nueva_contra):
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
                top.destroy()
                self.mostrar_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el usuario. Revisa la consola.")

        top = tk.Toplevel(self.root)
        top.title("Actualizar usuario")
        top.geometry("300x200")

        tk.Label(top, text="Nuevo usuario:").pack(pady=5)
        entry_user = tk.Entry(top)
        entry_user.insert(0, user_name)
        entry_user.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Nueva contraseña:").pack(pady=5)
        entry_pass = tk.Entry(top, show="*")
        entry_pass.pack(pady=5, fill="x", padx=10)

        tk.Button(top, text="Guardar cambios", command=guardar_cambios).pack(pady=10)

    def eliminar_usuarios(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Eliminar", "Seleccione un usuario para eliminar.")
            return

        item = self.tree.item(seleccion[0], "values")
        user_id = item[0]
        user_name = item[1]

        if messagebox.askyesno("Confirmar eliminación", f"¿Está seguro que desea eliminar al usuario '{user_name}'?"):
            if eliminar_usuarios_db(user_id):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.mostrar_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario. Revisa la consola.")

    def cerrar_sesion(self):
        if messagebox.askyesno("Confirmar cierre", "¿Está seguro que desea cerrar sesión?"):
            self.root.destroy()


if __name__ == "__main__":
    App = UserApp("admin")