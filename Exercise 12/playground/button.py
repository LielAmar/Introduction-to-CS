import tkinter as tk
root = tk.Tk()


class cursors:
    def __init__(self):
        self.cursors = ["circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart",
                        "man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "trek", "watch"]
        self.index = 0

    def __iter__(self):
        return self.cursors

    def __next__(self):
        self.index += 1
        if self.index >= len(self.cursors):
            raise StopIteration
        return self.cursors[self.index-1]


cursor = cursors()

C1 = "#496878"
C2 = "#0F4C75"
C3 = "#3282B8"
C4 = "#BBE1FA"

text_align_dict = {
    "top": "n",
    "bottom": "s",
    "center": "center",
    "left": "w",
    "right": "e",
    "top_right": "ne",
    "top_left": "nw",
    "bottom_right": "se",
    "bottom_left": "sw"
}
HEIGHT = 500
WITDH = 1000
SIZE = 10

FONT = ('Helvetica', 24, 'bold')
BORDER_WIDTH = 0
ALIGN_CENTER = True
TEXT_ALIGN = "center"
# COLORS
BG = C3
FG = C4
WHILE_CLICK_BG = C2
WHILE_CLICK_FG = C3
AFTER_CLICK_BG = C1
AFTER_CLICK_FG = C2


root.geometry(f"{WITDH}x{HEIGHT}")


def click(sender: tk.Button):
    sender.config(cursor=next(cursor, "arrow"))
    sender.config(bg=AFTER_CLICK_BG, fg=AFTER_CLICK_FG)


text_align = text_align_dict[TEXT_ALIGN] if TEXT_ALIGN in text_align_dict else "center"

button1 = tk.Button(
    root,
    text="A",
    height=int(SIZE/1.5),
    width=SIZE,
    font=FONT,
    borderwidth=BORDER_WIDTH,
    cursor="arrow",
    anchor=text_align
)

# CONFIG COLORS
button1.config(
    fg=FG,
    bg=BG,
    activebackground=WHILE_CLICK_BG,
    activeforeground=WHILE_CLICK_FG
)
# CONFIG CLICK EVENT
button1.config(command=lambda: click(button1))


button1.pack(expand=ALIGN_CENTER)
if __name__ == "__main__":
    root.mainloop()
