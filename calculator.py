"""Средняя сложность, задание 3: калькулятор с интерфейсом Tkinter."""

import tkinter as tk
from math import isfinite
from tkinter import messagebox, ttk


def calculate(first: float, second: float, operation: str) -> float:
    """Вычисляет результат одной из четырёх арифметических операций."""
    if not isfinite(first) or not isfinite(second):
        raise ValueError("Введите конечные числа.")
    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            raise ValueError("Делить на ноль нельзя.")
        result = first / second
    else:
        raise ValueError("Выберите операцию: +, -, * или /.")
    if not isfinite(result):
        raise ValueError("Результат слишком велик.")
    return result


class CalculatorApp:
    """Связывает элементы интерфейса с арифметической функцией."""

    def __init__(self, root: tk.Tk) -> None:
        """Создаёт поля двух чисел, выбор операции и вывод результата."""
        self.root = root
        root.title("Калькулятор")
        root.resizable(False, False)
        frame = ttk.Frame(root, padding=20)
        frame.grid()
        ttk.Label(frame, text="Первое число:").grid(row=0, column=0, pady=5)
        self.first_entry = ttk.Entry(frame, width=22)
        self.first_entry.grid(row=0, column=1, pady=5)
        ttk.Label(frame, text="Операция:").grid(row=1, column=0, pady=5)
        self.operation = ttk.Combobox(
            frame, values=("+", "-", "*", "/"), state="readonly", width=19
        )
        self.operation.grid(row=1, column=1, pady=5)
        self.operation.current(0)
        ttk.Label(frame, text="Второе число:").grid(row=2, column=0, pady=5)
        self.second_entry = ttk.Entry(frame, width=22)
        self.second_entry.grid(row=2, column=1, pady=5)
        ttk.Button(frame, text="Вычислить", command=self.show_result).grid(
            row=3, column=0, columnspan=2, pady=10
        )
        self.result = tk.StringVar(root, value="Результат: —")
        ttk.Label(frame, textvariable=self.result, wraplength=320).grid(
            row=4, column=0, columnspan=2
        )
        self.first_entry.focus_set()

    def show_result(self) -> None:
        """Читает ввод и показывает результат либо сообщение об ошибке."""
        self.result.set("Результат: —")
        try:
            first = float(self.first_entry.get().strip().replace(",", "."))
            second = float(self.second_entry.get().strip().replace(",", "."))
        except ValueError:
            messagebox.showerror(
                "Ошибка ввода", "Введите два числа.", parent=self.root
            )
            return
        try:
            result = calculate(first, second, self.operation.get())
        except (ValueError, OverflowError) as error:
            messagebox.showerror("Ошибка вычисления", str(error),
                                 parent=self.root)
            return
        self.result.set(f"Результат: {result:.12g}")


def main() -> None:
    """Запускает графический калькулятор."""
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
