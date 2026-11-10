"""Средняя сложность, задание 5: окно с вкладками Notebook."""

import tkinter as tk
from tkinter import ttk


class TabsApp:
    """Демонстрирует три вкладки и передачу данных между ними."""

    def __init__(self, root: tk.Tk) -> None:
        """Создаёт вкладки с описанием, вводом имени и результатом."""
        root.title("Программа со вкладками")
        root.geometry("440x240")
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        about_tab = ttk.Frame(self.notebook, padding=15)
        input_tab = ttk.Frame(self.notebook, padding=15)
        self.result_tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(about_tab, text="Описание")
        self.notebook.add(input_tab, text="Ввод")
        self.notebook.add(self.result_tab, text="Результат")
        ttk.Label(
            about_tab,
            text="Лабораторная работа № 5, вариант 1.\n"
                 "Откройте вкладку «Ввод» и укажите своё имя.",
            wraplength=380,
        ).pack(anchor="w")
        ttk.Label(input_tab, text="Ваше имя:").pack(anchor="w")
        self.name_entry = ttk.Entry(input_tab, width=30)
        self.name_entry.pack(anchor="w", pady=10)
        ttk.Button(input_tab, text="Показать приветствие",
                   command=self.show_result).pack(anchor="w")
        self.result = tk.StringVar(root, value="Имя пока не введено.")
        ttk.Label(self.result_tab, textvariable=self.result,
                  wraplength=380).pack(anchor="w")

    def show_result(self) -> None:
        """Формирует приветствие и переключает вкладку на результат."""
        name = self.name_entry.get().strip()
        if name:
            self.result.set(f"Привет, {name}!")
        else:
            self.result.set(
                "Имя не указано. Заполните поле на вкладке «Ввод»."
            )
        self.notebook.select(self.result_tab)


def main() -> None:
    """Запускает приложение с вкладками."""
    root = tk.Tk()
    TabsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
