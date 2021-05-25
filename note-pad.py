from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

global w
w = 1


def window(text, path, title):
    win2 = Tk()
    win2.title(title)
    win2.minsize(220, 415)
    #   scrol = Scrollbar(win2)
    #   scrol.pack(side=RIGHT, fill=BOTH)
    text_ = Text(win2, font='tahoma')
    text_.pack(fill='both', expand=True)
    text_.insert(INSERT, text)
    #   scrol.config(command=text_.yview)
    #menu = Menu(win2)
    #menu.add_command(label='save', command= save_(path, text_.get(1.0, END))
    #win2.config(menu=menu)
    try:
        Button(win2, text='save', bd=3, font='tahoma', cursor='hand2', command=lambda: save_(path, text_.get(1.0, END))).pack(pady=2)
    except:
        pass
    Button(win2, text='exit ', fg='white', bg='black', bd=3, font='tahoma', command=win2.destroy, cursor='hand2').pack(pady=4)


# path : str, text : str
def save_(path: str, text: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def file_():
    try:
        global error_text
        error_text.destroy()
    except:
        pass
    path = 'file_mowaghat.txt'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except:
        with open(path, 'x', encoding='utf-8') as f:
            pass
        text = ''
    window(text, path, 'فایل موقت')


def open_file():
    try:
        global error_text
        error_text.destroy()
    except:
        pass
    try:
        error_text.destroy()
    except:
        pass
    file_work = askopenfilename(title='یک فایل را انتخاب کن')
    try:
        with open(file_work, 'r', encoding='utf-8') as f:
            text = f.read()
        window(text, file_work, 'note')
    except FileNotFoundError :
        error_text = Label(win, text=' فایل مورد نظر پیدا نشد ', fg='red', font=('tahoma'))
        error_text.pack(pady=4)
    except:
        text = ''
        error_text = Label(win, text=' نمیتوانیم فایل را باز کنیم', fg='red', font=('tahoma'))
        error_text.pack(pady=4)

'''
def error(file_path1:str):
    global w
    try:
        t = list(file_path1)
        h = []
        for i in range(5):
            h.append(t.pop())
            if t[-1] == '.':
                h.append(t.pop())
                t.extend(list(' ({})'.format(w)))
                t.append('.')
                t.extend(h)
                file_path = ''.join(t)
                #open(file_path, 'x', encoding='utf-8').close()
                window('', file_path, 'note')
                w += 1
    except FileExistsError:
        error(file_path1)
'''

def new_file():
    try:
        global error_text
        error_text.destroy()
    except:
        pass
    file_path = asksaveasfilename(title=' لطفا مکان و نام و پسوند فایل را انتخاب کنید',
                                  filetypes=[('note', '*txt;*py;*html')])
    t = list(file_path)
    if t:
        for i in range(5):
            t.pop()
            if t[-1] == '.':
                break
            elif t[-1] == '\\' or t[-1] == '/':
                file_path += '.txt'
                break
            elif i == 4:
                file_path += '.txt'
        try:
            #open(file_path, 'x', encoding='utf-8').close()
            window('', file_path, 'note')
        #except FileExistsError:
        #    error(file_path)
        except:
            error_text = Label(win, text=' نمیتوانیم فایل را بسازیم', fg='red', font='tahoma')
            error_text.pack(pady=4)


win = Tk()
win.title('برنامه نوت پد وریا مرادی')
# win.minsize(220, 415)
win.geometry('300x225')
win.resizable(False, False)
Label(win, text='خوش آمدید به این برنامه', font=('bold', 20)).pack(pady=10, side=TOP)
#  ساخت برنامه نوتپد وبرای برنامه نویسی هم
Button(win, text='  ساخت فایل جدید', font=('tahoma', 14), bd=3, fg='blue', command=new_file, cursor='hand2').pack()
Button(win, text='        باز کردن فایل', font=('tahoma', 14), bd=3, fg='blue', command=open_file, cursor='hand2').pack()
Button(win, text='باز کردن فایل موقت', font=('tahoma', 14), bd=3, fg='blue', command=file_, cursor='hand2').pack()

win.mainloop()
