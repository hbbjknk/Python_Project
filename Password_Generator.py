import random                           # importing the random module  
import tkinter as tk                    # importing the tkinter module  
from tkinter import *                   # importing everything from tkinter  
from tkinter import messagebox as mb    # importing messag
# defining a function to randomly generate the password  
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  
  
    # defining the list of characters that will be used to generate the password  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
  
    # using the random.sample() method to return a list of randomly get_length characters from the list of characters.  
    selected_char = random.sample(list_of_chars, len)  
  
    # converting the list into the string  
    pass_str = "".join(selected_char)  
      
    # displaying the generated password string in the label  
    pass_label.config(text = pass_str)  
  
    # printing the password string in command line  
    print("Generated Password is :", pass_str, "\n")  
# defining a function to check if the user has selected any option  
def selection():  
    '''''This function will check if the user has selected 
    any option and call the generate_password() function 
    by passing the appropriate length'''  
  
    # retrieving the length of the password  
    len = length.get()  
    # if the length is not 0 calling the generate_password(len) function  
    if len != 0:  
        generate_password(len)  
    # else displaying the error message using the messagebox's showerror() method  
    else:  
        mb.showerror("Invalid Selection", "Length of Password is not defined.")  
# defining a function to retrieve the length of the password  
def get_length():  
    '''''This function will retrieve the length of the password 
    from the selected option and print it in Command Line'''  
  
    # printing the selected length of the password for the user   
    print("Selected Length of Password :", length.get(), "characters")  
  
# defining a function to reset everything  
def reset():  
    "This function will reset everything in the application"  
  
    # setting the initial value of the password's length  
    length.set(0)  
    # setting the initial value of the label  
    pass_label.config(text = "")  
    
if __name__ == "__main__":  
    # creating a window using the Tk() class  
    gui_root = tk.Tk()  
    # setting the title of the window
    gui_root.title("Random Password Generator - JAVATPOINT")  
    # configuring the size and position of the window  
    gui_root.geometry("500x450+400+200")  
    # setting the background color of the window  
    gui_root.config(bg = "#E6E6FA")
    heading_frame=Frame(gui_root,bg="#000000")
    radiobtn_frame=Frame(gui_root,bg="#E6E6FA")
    Button_frame=Frame(gui_root,bg="#E6E6FA")
    result_frame=Frame(gui_root,bg="#E6E6FA")
    heading_frame.pack(fill="both")
    radiobtn_frame.pack(pady=10)
    Button_frame.pack(pady=10)
    result_frame.pack(pady=10)
    heading=Label(heading_frame,text="RANDOM PASSWORD GENERATOR", font=("Bahnschrift SemiBold","17"),bg="#7B68EE",fg="#FFFFFF")
    subheading=Label(heading_frame,text="Customize the Length of the Password: ",font=("Times new roman","14"),bg="#7B68EE",fg="#FFFFFF")
    heading.pack(pady=10)
    subheading.pack(fill="both")
# instantiating the IntVar() class  
length = IntVar()  
# setting an initial value of the IntVar object  
length.set(0)  
  
# adding some radio buttons to the window  
# 4 Characters Length  
radiobuttonOne = Radiobutton(  
    radiobtn_frame,  
    text = 'Length-4',  
    variable = length,  
    value = 4,  
    font = ("Times New Roman", "12"),  
    bg = "#E6E6FA",  
    command = get_length  
    )  
# 6 Characters Length  
radiobuttonTwo = Radiobutton(  
    radiobtn_frame,  
    text = 'Length-6',  
    variable = length,  
    value = 6,  
    font = ("Times New Roman", "12"),  
    bg = "#E6E6FA",  
    command = get_length  
    )  
# 8 Characters Length  
radiobuttonThree = Radiobutton(  
    radiobtn_frame,  
    text = 'Length-8',  
    variable = length,  
    value = 8,  
    font = ("Times New Roman", "12"),  
    bg = "#E6E6FA",  
    command = get_length  
    )  
# 10 Characters Length  
radiobuttonFour = Radiobutton(  
    radiobtn_frame,  
    text = 'Length-10',  
    variable = length,  
    value = 10,  
    font = ("Times New Roman", "12"),  
    bg = "#E6E6FA",  
    command = get_length  
    )  
# 12 Characters Length  
radiobuttonFive = Radiobutton(  
    radiobtn_frame,  
    text = 'Length-12',  
    variable = length,  
    value = 12,  
    font = ("Times New Roman", "12"),  
    bg = "#E6E6FA",  
    command = get_length  
    )  
# 16 Characters Length  
radiobuttonSix = Radiobutton(  
    radiobtn_frame,  
    text = 'Length-16',  
    variable = length,  
    value = 16,  
    font = ("Times New Roman", "12"),  
    bg = "#E6E6FA",  
    command = get_length  
    )  
  
# using the grid() method to set the position of the above radio buttons in grid format  
radiobuttonOne.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = W)  
radiobuttonTwo.grid(row = 0, column = 1, padx = 10, pady = 2, sticky = W)  
radiobuttonThree.grid(row = 1, column = 0, padx = 10, pady = 2, sticky = W)  
radiobuttonFour.grid(row = 1, column = 1, padx = 10, pady = 2, sticky = W)  
radiobuttonFive.grid(row = 2, column = 0, padx = 10, pady = 2, sticky = W)
radiobuttonSix.grid(row = 2, column = 1, padx = 10, pady = 2, sticky = W)
get_pass=Button(Button_frame,
                text="Get Password",
                font = ("Bahnschrift SemiBold", "12"),  
                width = 14,  
                bg = "#32CD32",  
                fg = "#FFFFFF",  
                activebackground = "#006400",  
                activeforeground = "#000000",  
                relief = GROOVE,  
                command = selection
)
clear_all = Button(  
    Button_frame,  
    text = "Reset",  
    font = ("Bahnschrift SemiBold", "12"),  
    width = 14,  
    bg = "#FF0000",  
    fg = "#FFFFFF",  
    activebackground = "#8B0000",  
    activeforeground = "#000000",  
    relief = GROOVE,  
    command = reset  
    )
get_pass.grid(row = 0, column = 0, padx = 5, pady = 2)  
clear_all.grid(row = 0, column = 1, padx = 5, pady = 2)  
pass_label=Label(
    result_frame,
    text="",
    font=("Consolas","15","bold"),
    bg="#E6E6FA",
    fg="#000000"
)
pass_label.pack()
gui_root.mainloop()




   
