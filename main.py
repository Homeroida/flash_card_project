from tkinter import *
import pandas
import random



BACKGROUND_COLOR = "#B1DDC6"
timer = None
reps = 0
current_card = {}
words_dic = {}







#---------------------------------------DATA---------------------------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words_dic = original_data.to_dict(orient="records")
else:
    words_dic = data.to_dict(orient="records")




#---------------------------------------Functionality---------------------------------------



def wrong_button():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dic)
    canvas.itemconfig(card_title, text="French",fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image= card_back)


def is_know():
    words_dic.remove(current_card)

    data = pandas.DataFrame(words_dic)
    data.to_csv("data/words_to_learn.csv", index=False)

    wrong_button()





#---------------------------------------GUI---------------------------------------

window = Tk()
window.title("Flash card game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")


canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400,150,text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263,text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0,columnspan=2)




bt_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(border = 0, image=bt_wrong, highlightthickness=0, relief=FLAT,command=wrong_button)
button_wrong.grid(column=0, row=1)

bt_right = PhotoImage(file="./images/right.png")
button_right = Button(border = 0, image=bt_right, highlightthickness=0, relief=FLAT, command=is_know)
button_right.grid(column=1,row=1)



wrong_button()

window.mainloop()
