from tkinter import Canvas, Tk, mainloop
from maze import maze
from algorithms import depth_first

path = []
a = "a"
b = "b"

def main():
    display(a)
    depth_first(maze, 1, 1, path)
    display(b)
    

def display(w):
    master = Tk()

    w = Canvas(master, width = 750, height = 750)
    w.pack()
    
    x1 = 0
    x2 = 50
    y1 = 0
    y2 = 50

    for i in range(len(maze)):
        y1 += 50
        y2 += 50
        x1 = 0
        x2 = 50

        for j in range(len(maze[0])):
            rec = maze[i][j]
            x1 += 50
            x2 += 50

            if rec == 0:
                color = "white"
            elif rec == 1:
                color = "black"
            elif rec == 2:
                color = "blue"
            elif rec == 9:
                color = "red"

            w.create_rectangle(x1, y1, x2, y2, fill = color)

    mainloop()

if __name__ == "__main__":
    main()