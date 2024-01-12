from tkinter import *
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Выход из приложения",'Do you want to exit?'):
        root.destroy()

root = Tk()
root.protocol('WM_DELETE_WINDOW', on_closing)
root.title("Приложение")
root.geometry('600x600')
root.minsize(250,350)
root.maxsize(600,600)
root['bg'] = '#778899'

def symbol():
    q = Toplevel()
    q.geometry('570x350')
    q['bg'] = 'grey'

    Label(q, text='обозначения спец символов:\n'
                  '\ - знак разделения\n'
                  '^ - знак возвдения в степень\n'
                  '/ - знак деления или дроби\n'
                  'sqrt() - обозначение корня', font=('Times New Roman', 11, 'bold')).pack(expand=1)
    q.title('о спец символах')

def about():
    a = Toplevel()
    a.geometry('570x350')
    a['bg'] = 'grey'

    Label(a, text="Сборник всех необходимых формул по математике"
        " и физике для школьников \n и преподавателей:"
                  "\n для выбора предмета кликните по нему, а затем кликните на желаемый "
                  "\n учебный раздел",
          font=('Times New Roman', 11, 'bold')).pack(expand=1)
    a.title('инструкция по пользованию')

def about2():
    b = Toplevel()
    b.geometry('426x273')
    b.maxsize(426,273)


    b.title('предмет - математика')

    Button(b, text='формулы сокращённого умножения', command=about4).grid(row=1,column=0)
    Button(b, text='cвойства степеней', command=about5).grid(row=2, column=0, stick='wens')
    Button(b, text='квадратное уравнение, формула \n '
                   'разложения квадратного трёхчлена \n'
                   'на множители', width=10, height=3, command=about6).grid(row=3,column=0,stick='we')
    Button(b, text='арифметическая и геометрическая \n '
                   'прогрессия', height=3, command=about7).grid(row=2,column=1, stick='we')
    Button(b, text='тригонометричекие \n'
                   'формулы', command=about8).grid(row=5,column=0, stick='we')
    Button(b, text='планиметрия: №1', command=about9).grid(row=6,column=0, stick='we')
    Button(b, text='стереометрия', command=read).grid(row=7, column=0, stick='we')
    Button(b, text='свойства логарифмов', command=log).grid(row=1,column=1, stick='we')
    Button(b, text='таблица квадратов', command=sqrts).grid(row=5, column=1, rowspan=3, stick='wens')
    Button(b, text='тригонометрическая \n'
                   'окружность', command=around).grid(row=4,column=0, stick='we')
    Button(b, text='тригонометрические \n'
                   'уравнения', command=something).grid(row=3,column=1, stick = 'wens')
    Button(b, text = 'планиметрия: №2', command=something2).grid(row=4,column=1, stick='wens')

def about3():
    c = Toplevel()
    c.geometry('570x350')
    #c['bg'] = '#778899'

    c.title('предмет - физика')

    Button(c, text='Кинематика', command=fis).grid(row=1,column=0)
    Button(c, text='2', command=fis1).grid(row=2,column=0)
    Button(c, text='3', command=fis2).grid(row=3,column=0)
    Button(c, text='4', command=fis3).grid(row=4,column=0)

def fis():
    y = Toplevel()
    y.geometry('1150x670')

    y.image = PhotoImage(file='Кинематика.png')
    task = Label(y, image=y.image)
    task.pack()

    y.title('')


def fis1():
    r = Toplevel()
    r.geometry('550x600')

    r.title('')

def fis2():
    g = Toplevel()
    g.geometry('550x600')

    g.title('')

def fis3():
    q = Toplevel()
    q.geometry('550x600')

    q.title('')

def fis4():
    r = Toplevel()
    r.geometry('550x600')

    r.title('')

def about4():
    d = Toplevel()
    d.geometry('570x350')

    d.image = PhotoImage(file='сокращённое умножение.png.')
    task = Label(d, image=d.image)
    task.pack()

    l = Label(d, text='формулы:', font=('Times New Roman', 11, 'bold'))
    l.pack()
    l.place(x=0,y=0)

    d.title('')

def about5():
    e = Toplevel()
    e.geometry('570x350')

    e.image = PhotoImage(file='степени.png')
    task = Label(e, image=e.image)
    task.pack()


    e.title('')

def about6():
    f = Toplevel()
    f.geometry('568x300')

    f.image = PhotoImage(file='квадратное уравнение.png')
    task = Label(f, image=f.image)
    task.pack()
    f.title('')

def about7():
    g = Toplevel()
    g.geometry('586x386')

    g.image = PhotoImage(file='арифм_и_геом_прогрессия.png')
    task = Label(g, image=g.image)
    task.pack()


    g.title('')

def about8():
    h = Toplevel()
    h.geometry('1081x725')

    h.image = PhotoImage(file='Тригонометрия.png')
    task = Label(h, image=h.image)
    task.pack()

def around():
    a = Toplevel()
    a.geometry('736x725')

    a.image = PhotoImage(file='окружность1.png')
    task = Label(a, image=a.image)
    task.pack()

def about9():
    i = Toplevel()
    i.geometry('600x600')

    i.image = PhotoImage(file='Плаиметрия_1.png')
    task = Label(i, image=i.image)
    task.pack()

    i.title('')

def read():
    u = Toplevel()
    u.geometry('600x500')

    u.image = PhotoImage(file='стереометрия.png')
    task = Label(u, image=u.image)
    task.pack()

    l = Label(u, text='куб')
    l.pack()
    l.place(x=70,y=25)

    ll = Label(u, text='параллелепипед')
    ll.pack()
    ll.place(x=40,y=120)

    l1 = Label(u, text='призма')
    l1.pack()
    l1.place(x=60,y=210)

    l2 = Label(u, text='цилиндр')
    l2.pack()
    l2.place(x=50,y=300)

    l3 = Label(u, text='пирамида')
    l3.pack()
    l3.place(x=440,y=40)

    l4 = Label(u, text='конус')
    l4.pack()
    l4.place(x=440,y=180)

    l5 = Label(u, text='шар/сфера')
    l5.pack()
    l5.place(x=420,y=320)

def log():
    f = Toplevel()
    f.geometry('600x500')

    f.image = PhotoImage(file='Логарифмы.png')
    task = Label(f, image=f.image)
    task.pack()

def sqrts():
    d = Toplevel()
    d.geometry('700x620')


    d.image = PhotoImage(file='таблица.png')
    task = Label(d, image=d.image)
    task.pack()

def something():
    g = Toplevel()
    g.geometry('1000x550')

    g.image = PhotoImage(file='Тригонометрические уравнения.png')
    task = Label(g, image = g.image)
    task.pack()

    g.title('')

def something2():
    r = Toplevel()
    r.geometry('800x600')

    r.image = PhotoImage(file='Планиметрия_2.png')
    task = Label(r, image = r.image)
    task.pack()

    l = Label(r, text='Теорема о пропорциональных отрезках хорд:')
    l.pack()
    l.place(x=0,y=0)

    l1 = Label(r,text='Теорема о касательной и секущей:')
    l1.pack()
    l1.place(x=0,y=170)

    l2 = Label(r, text="Теорема о двух секущих:")
    l2.pack()
    l2.place(x=0, y=340)

    l3 = Label(r, text='Теорема о центральном и вписанном углах (величина центрального угла в два раза \n'
                       'больше величины вписанного угла, если они опираются на общую дугу):')
    l3.pack()
    l3.place(x=300,y=50)

    l4 = Label(r, text = 'Свойство вписанных углов (все вписанные углы опирающиеся \n '
                         'на общую дугу равны между собой):')
    l4.pack()
    l4.place(x=320,y=235)

    r.title('')

B1 = Button(text="Инструкция по пользованию", width=50, height=5, relief=RAISED, bd=10, command=about)
B2 = Button(text='МАТЕМАТИКА', font=('Times New Roman', 11, 'bold'), width=25, height=15, relief=RAISED, bd=10,
            command=about2)
B3 = Button(text='ФИЗИКА', font=('Times New Roman', 11, 'bold'), width=25, height=15, relief=RAISED, bd=10,
            command=about3)
B4 = Button(text='О спец символах',width=50, height=5, relief=RAISED, bd=10, command=symbol)

B1.pack()
B1.place(x=100, y=455)
B2.pack()
B2.place(x=50, y=50)
B3.pack()
B3.place(x=300, y=50)
B4.pack()
B4.place(x=100, y=350)

root.mainloop()