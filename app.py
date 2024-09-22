import tkinter as tk
from interfaces.producto_ui import ProductoUI

def main():
    root = tk.Tk()
    root.title("Sistema de Gestion de Tienda")

    tk.Button(root, text="Gestion de Productos", command=lambda: productoUI(tk.Toplevel(root))).pack(pady=10)

    root.mainloop()

    if __name__ == "__main__":
        main()