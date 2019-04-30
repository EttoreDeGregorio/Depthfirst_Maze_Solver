from tkinter import Canvas, Tk, mainloop
from maze import *
from algorithms import depth_first

path = []
a = "a"
b = "b"

def main():

    print("Quale labirinto vuoi risolvere :")
    x = input()

    if x == "1":
        display(a, maze_1)
        depth_first(maze_1, 1, 1, path)
        display(b, maze_1)

    elif x == "2":
        display(a, maze_2)
        depth_first(maze_2, 0, 3, path)
        display(b, maze_2)
    
    elif x == "3":
        display(a, maze_3)
        depth_first(maze_3, 1, 2, path)
        display(b, maze_3)
    

def display(w, maze):
    master = Tk()

    w = Canvas(master, width = 900, height = 900)
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