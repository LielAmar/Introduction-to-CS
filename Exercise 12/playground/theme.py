import tkinter as tk
from tkinter import ttk
root = tk.Tk()
HEIGHT = 500
WITDH = 1000
root.geometry(f"{WITDH}x{HEIGHT}")
style = ttk.Style(root)

# print(style.theme_use())
style.theme_use("winnative")
# print(style.theme_names()) -> ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')


class iter:
    def __init__(self):
        self.themes = ["clam", "alt",
                       "default", "classic", "vista", "xpnative", "winnative"]
        self.index = 0

    def __iter__(self):
        return self.themes

    def __next__(self):
        self.index += 1
        if self.index >= len(self.themes):
            self.index = 1
        return self.themes[self.index-1]


themes = iter()

label = ttk.Label(root, font=("Arial", 20), text=style.theme_use())
label.pack(expand=True)


def click():
    style.theme_use(next(themes))
    label.config(text=style.theme_use())


ttk.Button(
    root,
    text='Change Theme',
    command=click
).pack(expand=True)


if __name__ == "__main__":
    root.mainloop()
