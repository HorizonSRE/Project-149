from tkinter import *
import random
root=Tk()
root.title("Random Word Generator")
root.geometry("500x500")
randword=Label(root)
def randwordgenerator():
    alpha_list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "x", "y", "z"]
    random_no1=random.randint(1,26)
    random_no2=random.randint(1,26)
    random_no3=random.randint(1,26)
    random_no4=random.randint(1,26)
    random_no5=random.randint(1,26)
    randword["text"]=alpha_list[random_no1]+alpha_list[random_no2]+alpha_list[random_no3]+alpha_list[random_no4]+alpha_list[random_no5]
btn=Button(root, text="Generate Random Word", command=randwordgenerator)
randword.pack()
btn.pack()
root.mainloop()