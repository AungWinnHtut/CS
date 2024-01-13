import tkinter as tk
import tkinter.messagebox
from tkinter import font
import json
from icecream import ic

global s_no
global total_s_no
global qlist
global score
global slide_index


def fun_count_exam():    
    with open('q.json','r') as qfile:
        global total_s_no
        global qlist
        qlist = json.load(qfile)
        total_s_no = len(qlist)
       


def fun_check():
    global score
    global s_no
    global slide_index

    ans = txt_ans.get()
    if ans == qlist[s_no]['correct_ans']:
        tk.messagebox.showinfo('Correct!','Your answer is Correct!, Bravo!')
        score += 1
        
    else:
        tk.messagebox.showinfo('Fail!','Your answer is NOT Correct!, Sorry!')
    
    lbl_score.config(text=f"Total: {score}")    
    s_no += 1
    if s_no < total_s_no:        
        slide_index = 'Exam No. ' + str(s_no+1) + ' / ' + str(total_s_no)
        lbl_slide_number.config(text=str(slide_index))
        lbl_question.config(text=qlist[s_no]['question'])
        lbl_option1.config(text=qlist[s_no]['option1'])
        lbl_option2.config(text=qlist[s_no]['option2'])
        lbl_option3.config(text=qlist[s_no]['option3'])
        txt_ans.delete(0, tk.END)
    else:
        tk.messagebox.showinfo('Congratulation! You answered all questions')
        btn_check.config(state=tk.DISABLED)




# Program Start Here
score = 0
s_no = 0
total_s_no = 0
fun_count_exam()
window = tk.Tk()
window.geometry('500x350')



slide_index = 'Exam No. ' + str(s_no+1) + ' / ' + str(total_s_no)
lbl_slide_number = tk.Label(window, text=slide_index, font =('Courier',20, 'bold'))
lbl_slide_number.pack()

str_question = qlist[s_no]['question']
lbl_question = tk.Label(window, text=str_question, font =('Courier',20, 'bold'))
lbl_question.pack()

str_option1 = qlist[s_no]['option1']
lbl_option1 = tk.Label(window, text=str_option1, font =('Courier',20, 'bold'))
lbl_option1.pack()

str_option2 = qlist[s_no]['option2']
lbl_option2 = tk.Label(window, text=str_option2, font =('Courier',20, 'bold'))
lbl_option2.pack()

str_option3 = qlist[s_no]['option3']
lbl_option3 = tk.Label(window, text=str_option3, font =('Courier',20, 'bold'))
lbl_option3.pack()


txt_ans = tk.Entry(window, font =('Courier',20, 'bold'))
txt_ans.pack()

btn_check = tk.Button(window,text='Check', font =('Courier',20, 'bold'),command=fun_check)
btn_check.pack()

lbl_score = tk.Label(window, text='Total: ' + str(score), font =('Courier',20, 'bold'))
lbl_score.pack()

window.mainloop()