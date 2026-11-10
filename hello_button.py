"""Средняя сложность, задание 1: окно с кнопкой «Привет»."""

import tkinter as tk
from tkinter import messagebox, ttk


def show_greeting() -> None:
    """Показывает приветствие в диалоговом окне."""
    messagebox.showinfo("Приветствие", "Привет!")


def main() -> None:
    """Создаёт окно, кнопку приветствия и запускает обработку событий."""
    root = tk.Tk()
    root.title("Кнопка «Привет»")
    root.geometry("320x160")
    root.resizable(False, False)
    ttk.Label(root, text="Нажмите кнопку для приветствия.").pack(pady=20)
    ttk.Button(root, text="Привет", command=show_greeting).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
