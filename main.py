import os
import matplotlib.pyplot as plt
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    file_path = "DS6.txt"

    if not os.path.exists(file_path):
        print("Файл не знайдено")
        return

    points = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                points.append((int(parts[0]), int(parts[1])))

    if not points:
        print("Файл не містить координат точок")
        return

    display_window(points)

def display_window(points):
    root = Tk()
    root.title("Відображення точок")

    canvas_width = 960
    canvas_height = 540

    root.geometry(f"{canvas_width}x{canvas_height}")
    root.resizable(False, False)

    fig, ax = plt.subplots(figsize=(canvas_width / 100, canvas_height / 100), dpi=100)
    
    x_vals, y_vals = zip(*points)
    ax.scatter(x_vals, y_vals, color="black", s=10)

    ax.set_xlim(0, canvas_width)
    ax.set_ylim(0, canvas_height)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.spines['left'].set_position(('outward', 0))
    ax.spines['bottom'].set_position(('outward', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()

if __name__ == "__main__":
    main()