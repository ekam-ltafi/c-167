from tkinter import *
from PIL import Image , ImageTk

root =Tk()

root.title("Drawing Operator")
root.geometry("600x600")

root.configure(background = "gray")
color_label = Label(root, text = "Enter a Color : ")
color_label.place(relx = 0.6 , rely = 0.9 , anchor = CENTER)

input_box = Entry(root)
input_box_insert = (0 , "black")
input_box.place(relx = 0.8 , rely = 0.9 , anchor = CENTER)

canvas = Canvas(root , height = 510 , width = 500 , bg = "white")
canvas.pack()
img = ImageTk.PhotoImage(Image.open("start_point1.png"))
My_image = canvas.create_image(50,50,image = img)

directions = ""
oldx = 50       
oldy = 50
newx = 50
newy = 50

def left_dir(event):
    global directions
    global oldx
    global oldy
    global newx 
    global newy
    newx = newx-5
    oldx = newx
    oldy = newy
    directions = "Left"
    draw(directions , oldx , oldy , newx , newy)
def right_dir(event):
    global directions
    global oldx
    global oldy
    global newx 
    global newy
    newx = newx+5
    oldx = newx
    oldy = newy
    directions = "Right"
    draw(directions , newx , oldx ,newy , oldy)
    
def up_dir(event):
    global directions
    global oldx
    global oldy
    global newx 
    global newy
    newy = newy-5    
    oldx = newx
    oldy = newy
    directions = "Up"
    draw(directions , oldx , newx , oldy , newy)
        
def down_dir(event):
    global directions
    global oldx
    global oldy
    global newx 
    global newy
    newy = newy+5
    oldx = newx
    oldy = newy
    directions = "Down"
    draw(directions , oldx , oldy , newx ,newy)
    
    

def draw(directions ,oldx , oldy ,newx , newy) :
    fill_color = input_box.get()
    if(directions == "Left"):
        left_line = canvas.create_line( oldx , oldy , newx , newy , width = 3 , fill = fill_color)
        
    if(directions == "Right"):
         right_line = canvas.create_line( oldx , oldy , newx , newy , width = 3 , fill = fill_color)
    
    if(directions == "Up"):
        up_line = canvas.create_line( oldx , oldy , newx , newy , width = 3 , fill = fill_color)
        
    if(directions == "Down"):
            down_line = canvas.create_line( oldx , oldy , newx , newy , width = 3 , fill = fill_color)



root.bind("<Left>",left_dir)
root.bind("<Right>",right_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)




root.mainloop()