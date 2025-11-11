
import tkinter as tk
from tkinter import messagebox, ttk
from productos_controller import ver_productos_db, agregar_producto_db, actualizar_producto_db, eliminar_producto_db

class ProductosView:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Productos - Usuario: {username}")
        self.root.geometry("900x520")
        self.root.resizable(True, True)

        self.crear_elementos()
        self.mostrar_productos()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola, {self.username}", font=("Arial", 20, "bold")).pack(pady=8)
        tk.Button(self.root, text="Cerrar sesión", command=self.cerrar_sesion).pack(pady=4)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=6)

        tk.Button(frame_botones, text="Agregar producto", width=18, command=self.agregar_producto).pack(side="left", padx=6)
        tk.Button(frame_botones, text="Actualizar producto", width=18, command=self.actualizar_producto).pack(side="left", padx=6)
        tk.Button(frame_botones, text="Eliminar producto", width=18, command=self.eliminar_producto).pack(side="left", padx=6)

        tk.Label(self.root, text="Lista de productos", font=("Arial", 16, "bold")).pack(pady=8)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Stock", "Marca", "Proveedor", "Descripcion"), show="headings", height=14)
        for col, width in (("ID",60), ("Nombre",250), ("Stock",80), ("Marca",130), ("Proveedor",130), ("Descripcion",300)):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center" if col in ("ID","Stock") else "w")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_productos(self):
        try:
            productos = ver_productos_db()
            for item in self.tree.get_children():
                self.tree.delete(item)
            for p in productos:
                # p => (id_productos, nombre_producto, stock, marca, provedor, descripcion)
                self.tree.insert("", "end", values=p)
            print(f"mostrar_productos: {len(productos)} productos mostrados")
            return productos
        except Exception as e:
            print(f"Error en mostrar_productos: {e}")
            messagebox.showerror("Error", "No se pudieron cargar los productos.")
            return []

    def agregar_producto(self):
        top = tk.Toplevel(self.root)
        top.title("Agregar producto")
        top.geometry("450x380")

        tk.Label(top, text="Nombre:").pack(pady=4)
        entry_nombre = tk.Entry(top)
        entry_nombre.pack(fill="x", padx=10)

        tk.Label(top, text="Stock:").pack(pady=4)
        entry_stock = tk.Entry(top)
        entry_stock.pack(fill="x", padx=10)

        tk.Label(top, text="Marca:").pack(pady=4)
        entry_marca = tk.Entry(top)
        entry_marca.pack(fill="x", padx=10)

        tk.Label(top, text="Proveedor:").pack(pady=4)
        entry_provedor = tk.Entry(top)
        entry_provedor.pack(fill="x", padx=10)

        tk.Label(top, text="Descripción:").pack(pady=4)
        entry_descripcion = tk.Text(top, height=5)
        entry_descripcion.pack(fill="both", padx=10, pady=4)

        def guardar():
            nombre = entry_nombre.get().strip()
            stock = entry_stock.get().strip()
            marca = entry_marca.get().strip()
            provedor = entry_provedor.get().strip()
            descripcion = entry_descripcion.get("1.0", "end").strip()
            if not nombre or stock == "":
                messagebox.showwarning("Datos faltantes", "El nombre y el stock son obligatorios.")
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

        tk.Button(top, text="Guardar", command=guardar).pack(pady=8)

    def actualizar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Actualizar", "Seleccione un producto para actualizar.")
            return
        item = self.tree.item(seleccion[0], "values")
        prod_id, nombre, stock, marca, provedor, descripcion = item

        top = tk.Toplevel(self.root)
        top.title("Actualizar producto")
        top.geometry("450x420")

        tk.Label(top, text="Nombre:").pack(pady=4)
        entry_nombre = tk.Entry(top)
        entry_nombre.insert(0, nombre)
        entry_nombre.pack(fill="x", padx=10)

        tk.Label(top, text="Stock:").pack(pady=4)
        entry_stock = tk.Entry(top)
        entry_stock.insert(0, stock)
        entry_stock.pack(fill="x", padx=10)

        tk.Label(top, text="Marca:").pack(pady=4)
        entry_marca = tk.Entry(top)
        entry_marca.insert(0, marca)
        entry_marca.pack(fill="x", padx=10)

        tk.Label(top, text="Proveedor:").pack(pady=4)
        entry_provedor = tk.Entry(top)
        entry_provedor.insert(0, provedor)
        entry_provedor.pack(fill="x", padx=10)

        tk.Label(top, text="Descripción:").pack(pady=4)
        entry_descripcion = tk.Text(top, height=6)
        entry_descripcion.insert("1.0", descripcion)
        entry_descripcion.pack(fill="both", padx=10, pady=4)

        def guardar_cambios():
            nuevo_nombre = entry_nombre.get().strip()
            nuevo_stock = entry_stock.get().strip()
            nueva_marca = entry_marca.get().strip()
            nuevo_provedor = entry_provedor.get().strip()
            nueva_descripcion = entry_descripcion.get("1.0", "end").strip()
            if not nuevo_nombre or nuevo_stock == "":
                messagebox.showwarning("Datos faltantes", "El nombre y el stock son obligatorios.")
                return
            try:
                stock_val = int(nuevo_stock)
            except ValueError:
                messagebox.showwarning("Stock inválido", "El stock debe ser un número entero.")
                return
            try:
                id_val = int(prod_id)
            except Exception:
                id_val = prod_id
            if actualizar_producto_db(id_val, nuevo_nombre, stock_val, nueva_marca, nuevo_provedor, nueva_descripcion):
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                top.destroy()
                self.mostrar_productos()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto.")

        tk.Button(top, text="Guardar cambios", command=guardar_cambios).pack(pady=8)

    def eliminar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Eliminar", "Seleccione un producto para eliminar.")
            return
        item = self.tree.item(seleccion[0], "values")
        prod_id, prod_name = item[0], item[1]
        if messagebox.askyesno("Confirmar eliminación", f"¿Eliminar el producto '{prod_name}'?"):
            try:
                id_val = int(prod_id)
            except Exception:
                id_val = prod_id
            if eliminar_producto_db(id_val):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.mostrar_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def cerrar_sesion(self):
        if messagebox.askyesno("Confirmar cierre", "¿Está seguro de que desea cerrar sesión?"):
            self.root.destroy()

if __name__ == "__main__":
    App = ProductosView("admin")
