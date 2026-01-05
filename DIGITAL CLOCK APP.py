# DIGITAL CLOCK PROJECT:
  
# IMPORTING A MODULE FOR GRAPHICAL USER INTERFACE (GUI)
import tkinter as tk 

# IMPORTING A MODULE TO SHOW CURRENT TIME AND DATE FROM MY COMPUTER 
from time import strftime

# CREATING A WINDOW (BLANK PAGE)
root = tk.Tk()

# MAKING A TITLE ON A WINDOW 
root.title("DIGITAL CLOCK")

# SETTING A LABEL AND ITS FONT AND SIZE BACKGROUND ETC ...
label = tk.Label(root,font=('anton',50,'bold'),background = "#222",foreground = "#00C3FF")

# MAKING THE POISTION OF THE ELEMENT WHERE TO SET
label.pack(anchor="center")

# DEFINING A TIME
def time():

# SETTING TIME FORMAT
    string = strftime('%I:%M:%S:%p \n %D')
# %I = HOURS
# %M = MINUTES
# %S = SECOND
# %p = AM OR PM
# %D = DATE/YEAR

# CHANGE THE LABEL WHAT SHOW UPDATING IT WITH NEW TIME
    label.config(text=string)

# UPDATING A TIME AFTER EVERY SECOND 
    label.after(1000,time)

# STRARTING TIME FUNCTION
time()
root.mainloop()
