"""Повышенная сложность, задание 1: заметки с сохранением в файл."""

import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from typing import Optional


class NotesApp:
    """Предоставляет редактор заметки и сохранение текста в UTF-8."""

    def __init__(self, root: tk.Tk) -> None:
        """Создаёт редактор, кнопки сохранения и обработчик закрытия."""
        self.root = root
        self.file_path: Optional[Path] = None
        root.title("Заметки — новый файл")
        root.geometry("680x440")
        toolbar = ttk.Frame(root, padding=8)
        toolbar.pack(fill="x")
        ttk.Button(toolbar, text="Сохранить", command=self.save_note).pack(
            side="left", padx=4
        )
        ttk.Button(
            toolbar, text="Сохранить как…",
            command=lambda: self.save_note(save_as=True),
        ).pack(side="left", padx=4)
        self.editor = ScrolledText(root, wrap="word", undo=True)
        self.editor.pack(fill="both", expand=True, padx=10, pady=5)
        self.editor.edit_modified(False)
        self.status = tk.StringVar(root, value="Введите текст заметки.")
        ttk.Label(root, textvariable=self.status, padding=8).pack(anchor="w")
        root.protocol("WM_DELETE_WINDOW", self.close_window)

    def save_note(self, save_as: bool = False) -> bool:
        """Сохраняет заметку; возвращает False при отмене или ошибке записи."""
        target = self.file_path
        if save_as or target is None:
            selected = filedialog.asksaveasfilename(
                parent=self.root,
                title="Сохранить заметку",
                defaultextension=".txt",
                filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
                confirmoverwrite=True,
            )
            if not selected:
                return False
            target = Path(selected)
        text = self.editor.get("1.0", "end-1c")
        try:
            target.write_text(text, encoding="utf-8")
        except (OSError, UnicodeError) as error:
            messagebox.showerror("Ошибка сохранения", str(error),
                                 parent=self.root)
            return False
        self.file_path = target
        self.editor.edit_modified(False)
        self.root.title(f"Заметки — {target.name}")
        self.status.set(f"Сохранено: {target}")
        return True

    def close_window(self) -> None:
        """Предлагает сохранить изменения перед закрытием приложения."""
        if self.editor.edit_modified():
            answer = messagebox.askyesnocancel(
                "Несохранённые изменения", "Сохранить заметку перед выходом?",
                parent=self.root,
            )
            if answer is None:
                return
            if answer and not self.save_note():
                return
        self.root.destroy()


def main() -> None:
    """Запускает редактор заметок."""
    root = tk.Tk()
    NotesApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
