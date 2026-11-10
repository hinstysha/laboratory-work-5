"""Повышенная сложность, задание 4: график matplotlib внутри Tkinter."""

import tkinter as tk
from math import isfinite
from tkinter import messagebox


def build_points(
    x_min: float = -5.0, x_max: float = 5.0, point_count: int = 201
) -> tuple[list[float], list[float]]:
    """Вычисляет равномерные точки графика y = x² на заданном отрезке."""
    if not isfinite(x_min) or not isfinite(x_max) or x_min >= x_max:
        raise ValueError("Границы должны быть конечными, левая меньше правой.")
    if isinstance(point_count, bool) or not isinstance(point_count, int):
        raise TypeError("Количество точек должно быть целым числом.")
    if point_count < 2:
        raise ValueError("Для графика нужны хотя бы две точки.")
    step = (x_max - x_min) / (point_count - 1)
    x_values = [x_min + index * step for index in range(point_count)]
    try:
        y_values = [value ** 2 for value in x_values]
    except OverflowError as error:
        raise ValueError("Границы слишком велики для вычисления.") from error
    if not all(isfinite(value) for value in x_values + y_values):
        raise ValueError("Получены слишком большие значения координат.")
    return x_values, y_values


class GraphApp:
    """Встраивает фигуру matplotlib и панель инструментов в окно Tkinter."""

    def __init__(self, root: tk.Tk) -> None:
        """Создаёт график y = x² с подписями, сеткой и масштабированием."""
        from matplotlib.backends.backend_tkagg import (
            FigureCanvasTkAgg,
            NavigationToolbar2Tk,
        )
        from matplotlib.figure import Figure

        root.title("График y = x² внутри Tkinter")
        root.geometry("760x540")
        figure = Figure(figsize=(7, 4.5), dpi=100, constrained_layout=True)
        axes = figure.add_subplot(111)
        x_values, y_values = build_points()
        axes.plot(x_values, y_values, color="#2563eb", label="y = x²")
        axes.set_title("График функции y = x²")
        axes.set_xlabel("x")
        axes.set_ylabel("y")
        axes.set_xlim(-5, 5)
        axes.set_ylim(bottom=0)
        axes.grid(True, alpha=0.3)
        axes.legend()
        self.canvas = FigureCanvasTkAgg(figure, master=root)
        self.toolbar = NavigationToolbar2Tk(
            self.canvas, root, pack_toolbar=False
        )
        self.toolbar.update()
        self.toolbar.pack(side="bottom", fill="x")
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas.draw()


def main() -> None:
    """Запускает окно графика или сообщает об отсутствии matplotlib."""
    root = tk.Tk()
    root.withdraw()
    try:
        GraphApp(root)
    except ImportError:
        messagebox.showerror(
            "Не хватает библиотеки",
            "Установите matplotlib:\npython -m pip install matplotlib",
            parent=root,
        )
        root.destroy()
        return
    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    main()
