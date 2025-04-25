import tkinter as tk
def main ():

    CELL_SIZE = 25
    ROWS = 15
    COLS = 15

    def create_grid (canvas):
        grid= []
        for row in range(ROWS):
            row_cell =[]
            for col in range(COLS):
                x1 = col* CELL_SIZE
                y1 = row * CELL_SIZE
                x2 =x1 + CELL_SIZE 
                y2 = y1 + CELL_SIZE
                rect=canvas.create_rectangle(x1, y1, x2, y2, fill ="blue", outline= "black")
                row_cell.append(rect)
            grid.append(row_cell)
        return grid
    
    def move_eraser(event):
        x = event.x
        y = event.y

        for row in grid:
            for cell in row:
                x1, y1, x2, y2 = canvas.coords(cell)
                if x1 <= x <= x2 and y1 <= y <= y2:
                 canvas.itemconfig(cell, fill="white")

    root = tk.Tk()
    root.title("Simple Canvas Eraser")
    canvas=tk.Canvas(root, width=CELL_SIZE*COLS, height=CELL_SIZE*ROWS)
    canvas.pack()

    grid= create_grid(canvas)

    canvas.bind('<B1-Motion>',move_eraser)

    root.mainloop()

if __name__ == "__main__":
    main()