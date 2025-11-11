
import tkinter as tk
from tkinter import messagebox, ttk
from database import crear_conexion

# Operaciones en BD para productos
def ver_productos_db():
    conexion = crear_conexion()
    if not conexion:
        print("ver_productos_db: sin conexión")
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_productos, nombre_producto, stock, marca, provedor, descripcion FROM productos")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        print(f"ver_productos_db: {len(resultado)} productos encontrados")
        return resultado
    except Exception as e:
        print(f"Error ver_productos_db: {e}")
        return []

def agregar_producto_db(nombre, stock, marca, provedor, descripcion):
    conexion = crear_conexion()
    if not conexion:
        print("agregar_producto_db: sin conexión")
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre_producto, stock, marca, provedor, descripcion) VALUES (%s, %s, %s, %s, %s)",
            (nombre, stock, marca, provedor, descripcion)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"agregar_producto_db: '{nombre}' agregado")
        return True
    except Exception as e:
        print(f"Error agregar_producto_db: {e}")
        return False

def actualizar_producto_db(id_producto, nombre, stock, marca, provedor, descripcion):
    conexion = crear_conexion()
    if not conexion:
        print("actualizar_producto_db: sin conexión")
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre_producto = %s, stock = %s, marca = %s, provedor = %s, descripcion = %s WHERE id_productos = %s",
            (nombre, stock, marca, provedor, descripcion, id_producto)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"actualizar_producto_db: id={id_producto} actualizado")
        return True
    except Exception as e:
        print(f"Error actualizar_producto_db: {e}")
        return False

def eliminar_producto_db(id_producto):
    conexion = crear_conexion()
    if not conexion:
        print("eliminar_producto_db: sin conexión")
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_productos = %s", (id_producto,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"eliminar_producto_db: id={id_producto} eliminado")
        return True
    except Exception as e:
        print(f"Error eliminar_producto_db: {e}")
        return False

# Interfaz gráfica para productos
class ProductosApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("800x500")
        self.root.resizable(True, True)

        self.crear_elementos()
        self.mostrar_productos()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola, {self.username}", font=("Arial", 22, "bold")).pack(pady=10)
        tk.Button(self.root, text="Cerrar sesión", command=self.cerrar_sesion).pack(pady=10)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar producto", width=20, command=self.agregar_producto).pack(pady=5)
        tk.Button(frame_botones, text="Actualizar producto", width=20, command=self.actualizar_producto).pack(pady=5)
        tk.Button(frame_botones, text="Eliminar producto", width=20, command=self.eliminar_producto).pack(pady=5)

        tk.Label(self.root, text="Lista de productos", font=("Arial", 16, "bold")).pack(pady=10)

        # Tabla con columnas para productos
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Stock", "Marca", "Proveedor", "Descripcion"), show="headings", height=12)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Proveedor", text="Proveedor")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Ajuste de anchos (opcional)
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Nombre", width=200)
        self.tree.column("Stock", width=80, anchor="center")
        self.tree.column("Marca", width=120)
        self.tree.column("Proveedor", width=120)
        self.tree.column("Descripcion", width=250)

    def mostrar_productos(self):
        try:
            productos = ver_productos_db()
            for item in self.tree.get_children():
                self.tree.delete(item)
            for p in productos:
                # cada p debe ser tupla (id_productos, nombre_producto, stock, marca, provedor, descripcion)
                self.tree.insert("", "end", values=p)
            return productos
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron obtener los productos: {e}")
            return []

    def agregar_producto(self):
        def guardar():
            nombre = entry_nombre.get().strip()
            stock = entry_stock.get().strip()
            marca = entry_marca.get().strip()
            provedor = entry_provedor.get().strip()
            descripcion = entry_descripcion.get().strip()
            if not nombre or stock == "":
                messagebox.showwarning("Datos faltantes", "Nombre y stock son obligatorios.")
                return
            try:
                stock_val = int(stock)
            except ValueError:
                messagebox.showwarning("Stock inválido", "El stock debe ser un número entero.")
                return
            if agregar_producto_db(nombre, stock_val, marca, provedor, descripcion):
                messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                top.destroy()
                self.mostrar_productos()
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto.")

        top = tk.Toplevel(self.root)
        top.title("Agregar producto")
        top.geometry("400x350")

        tk.Label(top, text="Nombre:").pack(pady=5)
        entry_nombre = tk.Entry(top)
        entry_nombre.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Stock:").pack(pady=5)
        entry_stock = tk.Entry(top)
        entry_stock.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Marca:").pack(pady=5)
        entry_marca = tk.Entry(top)
        entry_marca.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Proveedor:").pack(pady=5)
        entry_provedor = tk.Entry(top)
        entry_provedor.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Descripción:").pack(pady=5)
        entry_descripcion = tk.Text(top, height=4)
        entry_descripcion.pack(pady=5, fill="both", padx=10)

        def get_descripcion_text():
            return entry_descripcion.get("1.0", "end").strip()

        # override guardar to read Text widget
        def guardar_wrapper():
            nonlocal entry_descripcion
            descripcion_text = get_descripcion_text()
            nombre = entry_nombre.get().strip()
            stock = entry_stock.get().strip()
            marca = entry_marca.get().strip()
            provedor = entry_provedor.get().strip()
            if not nombre or stock == "":
                messagebox.showwarning("Datos faltantes", "Nombre y stock son obligatorios.")
                return
            try:
                stock_val = int(stock)
            except ValueError:
                messagebox.showwarning("Stock inválido", "El stock debe ser un número entero.")
                return
            if agregar_producto_db(nombre, stock_val, marca, provedor, descripcion_text):
                messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                top.destroy()
                self.mostrar_productos()
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto.")

        tk.Button(top, text="Guardar", command=guardar_wrapper).pack(pady=10)

    def actualizar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Actualizar", "Seleccione un producto para actualizar.")
            return

        item = self.tree.item(seleccion[0], "values")
        prod_id, nombre, stock, marca, provedor, descripcion = item

        def guardar_cambios():
            nuevo_nombre = entry_nombre.get().strip()
            nuevo_stock = entry_stock.get().strip()
            nueva_marca = entry_marca.get().strip()
            nuevo_provedor = entry_provedor.get().strip()
            nueva_descripcion = entry_descripcion.get("1.0", "end").strip()
            if not nuevo_nombre or nuevo_stock == "":
                messagebox.showwarning("Datos faltantes", "Nombre y stock son obligatorios.")
                return
            try:
                stock_val = int(nuevo_stock)
            except ValueError:
                messagebox.showwarning("Stock inválido", "El stock debe ser un número entero.")
                return
            if actualizar_producto_db(prod_id, nuevo_nombre, stock_val, nueva_marca, nuevo_provedor, nueva_descripcion):
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                top.destroy()
                self.mostrar_productos()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto.")

        top = tk.Toplevel(self.root)
        top.title("Actualizar producto")
        top.geometry("400x380")

        tk.Label(top, text="Nombre:").pack(pady=5)
        entry_nombre = tk.Entry(top)
        entry_nombre.insert(0, nombre)
        entry_nombre.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Stock:").pack(pady=5)
        entry_stock = tk.Entry(top)
        entry_stock.insert(0, stock)
        entry_stock.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Marca:").pack(pady=5)
        entry_marca = tk.Entry(top)
        entry_marca.insert(0, marca)
        entry_marca.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Proveedor:").pack(pady=5)
        entry_provedor = tk.Entry(top)
        entry_provedor.insert(0, provedor)
        entry_provedor.pack(pady=5, fill="x", padx=10)

        tk.Label(top, text="Descripción:").pack(pady=5)
        entry_descripcion = tk.Text(top, height=4)
        entry_descripcion.insert("1.0", descripcion)
        entry_descripcion.pack(pady=5, fill="both", padx=10)

        tk.Button(top, text="Guardar cambios", command=guardar_cambios).pack(pady=10)

    def eliminar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Eliminar", "Seleccione un producto para eliminar.")
            return

        item = self.tree.item(seleccion[0], "values")
        prod_id = item[0]
        prod_name = item[1]

        if messagebox.askyesno("Confirmar", f"¿Seguro que desea eliminar el producto '{prod_name}'?"):
            if eliminar_producto_db(prod_id):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.mostrar_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def cerrar_sesion(self):
        if messagebox.askyesno("Confirmar cierre", "¿Está seguro de que desea cerrar sesión?"):
            self.root.destroy()


if __name__ == "__main__":
    App = ProductosApp("admin")
