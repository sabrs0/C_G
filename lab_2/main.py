from tkinter import *
import os
from PIL import Image, ImageTk
import numpy as np
import sympy as sym
from math import *
from tkinter import messagebox as mb
EPS = 1e-9
LEFT = -1
RIGHT = 1
dx = 0.0
dy = 0.0
angle = 0
def draw_fig_by_dots(fig_obj, dots, holst):
        for i in range(len(dots[0])):
                print_dot(dots[0][i], dots[1][i] , holst)
        text_x = round(fig_obj["center"][0], 2)
        text_y = round(fig_obj["center"][1], 2)
        holst.create_text(300, 300, text = f"{text_x};{text_y}",font = 'arial 10', anchor = S, fill = "red")
        holst.create_oval(300, 300, 300 + 3, 300 + 3, fill = "red")
def print_dot(x, y, holst):
        #print("!\n")
        holst.create_oval(x - 1, y - 1, x + 1, y + 1, fill = 'black')
        holst.create_line(x - 1, y - 1, x + 1, y + 1, fill = 'black')
def goto_move (event, holst, fig_obj, maxi, dots):
    move_win = Toplevel()
    move_win.geometry("200x200")
    e_dx = Entry(move_win, width = 6, font = "arial 12")
    e_dx.place(anchor = "sw", x = 10, y = 150)

    e_dy = Entry(move_win, width = 6, font = "arial 12")
    e_dy.place(anchor = "sw", x = 120, y = 150)

    l_dx = Label (move_win, text = "dx", font = "arial 12")
    l_dx.place(anchor = "sw", x = 10, y = 100)

    l_dy = Label (move_win, text = "dy", font = "arial 12")
    l_dy.place(anchor = "sw", x = 120, y = 100)

    b_move_fig = Button(move_win, text = "OK")
    b_move_fig.bind('<Button-1>', lambda e: move_fig(e, holst, fig_obj, dots, maxi, e_dx, e_dy))
    b_move_fig.place(anchor = "s", x = 100, y = 200)

def goto_rotate (event, holst, fig_obj, dots, maxi):
    rotate_win = Toplevel()
    rotate_win.geometry("250x200")
    e_xc = Entry(rotate_win, width = 6, font = "arial 12")
    e_xc.place(anchor = "sw", x = 10, y = 150)

    e_yc = Entry(rotate_win, width = 6, font = "arial 12")
    e_yc.place(anchor = "sw", x = 85, y = 150)

    e_ang = Entry(rotate_win, width = 6, font = "arial 12")
    e_ang.place(anchor = "sw", x = 160, y = 150)

    l_xc = Label (rotate_win, text = "X_C", font = "arial 12")
    l_xc.place(anchor = "sw", x = 10, y = 100)

    l_yc = Label (rotate_win, text = "Y_C", font = "arial 12")
    l_yc.place(anchor = "sw", x = 85, y = 100)

    l_ang = Label (rotate_win, text = "Угол", font = "arial 12")
    l_ang.place(anchor = "sw", x = 160, y = 100)

    b_rotate_fig = Button(rotate_win, text = "OK")
    b_rotate_fig.bind('<Button-1>', lambda e: rotate_fig(e, holst, fig_obj, dots, maxi, e_xc, e_yc, e_ang))
    b_rotate_fig.place(anchor = "s", x = 100, y = 200)
    
def goto_scale (event, holst, fig_obj, dots, maxi):
    rotate_win = Toplevel()
    rotate_win.geometry("300x300")
    
    e_xc = Entry(rotate_win, width = 5, font = "arial 12")
    e_xc.place(anchor = "sw", x = 10, y = 150)

    e_yc = Entry(rotate_win, width = 5, font = "arial 12")
    e_yc.place(anchor = "sw", x = 85, y = 150)

    e_kx = Entry(rotate_win, width = 5, font = "arial 12")
    e_kx.place(anchor = "sw", x = 160, y = 150)

    e_ky = Entry(rotate_win, width = 5, font = "arial 12")
    e_ky.place(anchor = "sw", x = 235, y = 150)

    l_xc = Label (rotate_win, text = "X_C", font = "arial 12")
    l_xc.place(anchor = "sw", x = 10, y = 100)

    l_yc = Label (rotate_win, text = "Y_C", font = "arial 12")
    l_yc.place(anchor = "sw", x = 85, y = 100)

    l_kx = Label (rotate_win, text = "K_X", font = "arial 12")
    l_kx.place(anchor = "sw", x = 160, y = 100)

    l_ky = Label (rotate_win, text = "K_Y", font = "arial 12")
    l_ky.place(anchor = "sw", x = 235, y = 100)

    b_rotate_fig = Button(rotate_win, text = "OK")
    b_rotate_fig.bind('<Button-1>', lambda e: scale_fig(e, holst, fig_obj, dots, maxi, e_xc, e_yc, e_kx, e_ky))
    b_rotate_fig.place(anchor = "sw", relx = 0, rely = 1)

def goto_main(event):
    button_begin.destroy()
    canvas.destroy()
    l_main.destroy()
    root.geometry("800x600+{}+{}".format(width-200, height - 150))
    l_A = Label(text = "A:", font = "arial 14")
    l_A.place(x = 25, y = 150)
    e_A = Entry(bd = 3,width = 9, font = 'arial 14')
    e_A.place(x = 50, y = 150)

    l_B = Label(text = "B:", font = "arial 14")
    l_B.place(x = 25, y = 200)
    e_B = Entry(bd = 3,width = 9, font = 'arial 14')
    e_B.place(x = 50, y = 200)

    l_C = Label(text = "C:", font = "arial 14")
    l_C.place(x = 25, y = 250)
    e_C = Entry(bd = 3,width = 9, font = 'arial 14')
    e_C.place(x = 50, y = 250)

    l_D = Label(text = "D:", font = "arial 14")
    l_D.place(x = 25, y = 300)
    e_D = Entry(bd = 3,width = 9, font = 'arial 14')
    e_D.place(x = 50, y = 300)

    l_R = Label(text = "R:", font = "arial 14")
    l_R.place(x = 25, y = 350)
    e_R = Entry(bd = 3,width = 9, font = 'arial 14')
    e_R.place(x = 50, y = 350)

    b_solve = Button(text = "Показать изображение", font = 'arial 12')
    b_solve.place(anchor = "sw", relx = 0, rely = 1)
    b_solve.bind('<Button-1>', lambda e: build_img(e, e_A, e_B, e_C, e_D, e_R))

def move_fig(event, holst, fig_obj, dots, maxi, ex, ey):
        d_e_x = ex.get()
        #dx += float(d_e_x)
        d_e_y = ey.get()
        #dy += float(d_e_y)
        holst.delete("all")
        d_e_x = float(d_e_x)
        d_e_y = float(d_e_y)
        fig_obj["replace"] = fig_obj["replace"][0] + d_e_x, fig_obj["replace"][1] + d_e_y
        l_screen = 200
        h_abstract = (600 * maxi / l_screen)
        #(600 * fig_obj["replace"][0] / h_abstract)
        for i in range(len(dots[0])):
                dots[0][i] = dots[0][i] + (600 * d_e_x / h_abstract)
                dots[1][i] = dots[1][i] + (600 * d_e_y / h_abstract)
                
        draw_fig_by_dots(fig_obj, dots, holst)
def scale_fig(event, holst, fig_obj, dots, maxi, ex, ey, ekx, eky):
        e_x_c = ex.get()
        xc = float(e_x_c)
        e_y_c = ey.get()
        yc = float(e_y_c)

        e_kx = ekx.get()
        kx = float(e_kx)
        e_ky = eky.get()
        ky = float(e_ky)
        holst.delete("all")

        l_screen = 200
        h_abstract = (600 * maxi / l_screen)
        mnoj = 1
        if (xc < fig_obj["center"][0]):
                mnoj = -1
        center_rotate_x_screen = 300 + 300 * mnoj * abs(xc - fig_obj["center"][0]) / (h_abstract / 2)
        if (yc < fig_obj["center"][1]):
                mnoj = -1
        else:
                mnoj = 1
        center_rotate_y_screen = 300 - 300 * mnoj * abs(yc - fig_obj["center"][1]) / (h_abstract / 2)
        print(center_rotate_x_screen, center_rotate_y_screen)
        for i in range(len(dots[0])):
                
                dots[0][i] = dots[0][i] * kx + (1 - kx) * center_rotate_x_screen
                dots[1][i] = dots[1][i] * ky + (1 - ky) * center_rotate_y_screen
        draw_fig_by_dots(fig_obj, dots, holst)

def rotate_fig(event, holst, fig_obj, dots, maxi, ex, ey, e_ang):
        e_x_c = ex.get()
        xc = float(e_x_c)
        e_y_c = ey.get()
        yc = float(e_y_c)

        e_a = e_ang.get()
        angle = float(e_a)
        holst.delete("all")

        l_screen = 200
        h_abstract = (600 * maxi / l_screen)
        mnoj = 1
        if (xc < fig_obj["center"][0]):
                mnoj = -1
        center_rotate_x_screen = 300 + 300 * mnoj * abs(xc - fig_obj["center"][0]) / (h_abstract / 2)
        if (yc < fig_obj["center"][1]):
                mnoj = -1
        else:
                mnoj = 1
        center_rotate_y_screen = 300 - 300 * mnoj * abs(yc - fig_obj["center"][1]) / (h_abstract / 2)
        print(center_rotate_x_screen, center_rotate_y_screen)
        for i in range(len(dots[0])):
                x = dots[0][i]
                dots[0][i] = center_rotate_x_screen + (dots[0][i] - center_rotate_x_screen) * cos(radians(angle))\
                             + (dots[1][i] - center_rotate_y_screen) * sin(radians(angle))
                dots[1][i] = center_rotate_y_screen + (dots[1][i] - center_rotate_y_screen) * cos(radians(angle))\
                             - (x - center_rotate_x_screen) * sin(radians(angle))
        draw_fig_by_dots(fig_obj, dots, holst)
def is_par_over_cir(a, b, c, d, r):
    x_top_par = (-2 * d)/ (-2)
    y_top_par = f_parabola(x_top_par, c, d)
    if (y_top_par <= b):
            return 0
    x_par_left = f_y_parabola(b, c, d)
    if (x_par_left[0] <= a- r and x_par_left[1] >= a + r):
        return 1
    else:
        return 0
def scale(maxi, holst_size, scaled_val):
    return (holst_size * scaled_val) / maxi
def define_branch(x1, x2, x_top):
    #x1 should me < x2
    if (x2 < x_top):
        return LEFT
    elif (x1 > x_top):
        return RIGHT
    else:
        return 0
def define_side(cross_dots_y, b):
    #Определяет в какой части(правой, левой) окружности находится большиство точек
    less_0 = 0
    more_0 = 0
    for i in cross_dots_y:
        if (i < b):
            less_0 += 1
        elif (i > b):
            more_0 += 1
    if (less_0 >= 3):
        return LEFT
    elif (more_0 >= 3):
        return RIGHT
    else:
        return 0
def get_sides(cross_dots_x, a):
    #Определяет, сколько точек в полушариях
    less_0 = 0
    more_0 = 0
    for i in cross_dots_x:
        if (i < a):
            less_0 += 1
        elif (i > a):
            more_0 += 1
    arr = []
    arr.append(less_0)
    arr.append(more_0)
    return arr
def find_center(a, b, c, d, r, cross_dots_x, cross_dots_y, x_top_par, y_top_par):
    branch_def = define_branch(min(cross_dots_x), max(cross_dots_x), x_top_par)
    if (len(cross_dots_x) == 4 or branch_def == 0):
        x_leftest = min(cross_dots_x)
        x_rightest = max(cross_dots_x)
    else:
        if (branch_def == LEFT):
            x_leftest = min(cross_dots_x)
            if (f_parabola(min(cross_dots_x), c, d) < b and f_parabola(max(cross_dots_x), c, d) < b):
                x_rightest = max(cross_dots_x)
            else:
                x_rightest = a + r
        else:
            x_rightest = max(cross_dots_x)
            if (f_parabola(min(cross_dots_x), c, d) < b and f_parabola(max(cross_dots_x), c, d) < b):
                x_leftest = min(cross_dots_x)
            else:
                x_leftest = a - r
    x_c = (x_rightest + x_leftest) / 2

#Поиск точки максимума получаемой фигуры
    #вершина параболы внутри круга?
    if (y_top_par > (b - r) and y_top_par < (b + r) and x_top_par < (a + r) and x_top_par > (a - r)):
        y_top = y_top = y_top_par
        x_top = x_top_par
    else:
        if (len(cross_dots_x) == 2):
            if (branch_def == LEFT):
                if (max(cross_dots_x) < a):
                    y_top = b + r
                    x_top = a
                else:
                    y_top = f_parabola(max(cross_dots_x), c, d)
                    x_top = max(cross_dots_x)
            elif (branch_def == RIGHT):
                if (min(cross_dots_x) > a):
                    y_top =  b + r
                    x_top = a
                else:
                    y_top = f_parabola(min(cross_dots_x), c, d)
                    x_top = min(cross_dots_x)
        else:
            side = define_side(cross_dots_y, b)
            if (side != 0):
                y_top = max(cross_dots_y)
                x_top = max(f_y_parabola(y_top, c, d))
            else:
                y_top = b + r
                x_top = a
#Поиск точки минимума получаемой фигуры
    if (len(cross_dots_x) == 2):
        if (branch_def == LEFT):
            if (min(cross_dots_x) < a):
                y_low = b - r
                x_low = a
            else:
                y_low = f_parabola(min(cross_dots_x), c, d)
                x_low = min(cross_dots_x)
        elif (branch_def == RIGHT):
            if (max(cross_dots_x) > a):
                y_low = b - r
                x_low = a
            else:
                y_low = f_parabola(max(cross_dots_x), c, d)
                x_low = max(cross_dots_x)
        else:
                y_low = b - r
                x_low = a
    else:
        sides = get_sides(cross_dots_x, a)
        if (sides[0] + sides[1] < 4):
                y_low = b - r
                x_low = a
        else:
            if (sides[0] == 0 or sides[1] == 0):
                    y_low = min(cross_dots_y)
                    for i in cross_dots_x:
                            if (abs(y_low - f_parabola(i)) <= EPS):
                                    x_low = i
                                    break
            else:
                    y_low = b - r
                    x_low = a
                
                        
    y_c = (y_top + y_low) / 2
    c = []
    c.append(x_leftest)
    c.append(x_rightest)
    c.append(x_top)
    c.append(y_top)
    c.append(x_low)
    c.append(y_low)
    return c                
def cross_dots_amount(x_top, y_top, a, b, r, c, d):
    if (x_top <= (a + r)) and (x_top >= (a - r)):
        if (y_top > (b - r)):
            if (y_top <= (b + r)):
                return int(2)
            else:
                x_par = f_y_parabola(b, c, d)
                if (x_par[0] < a - r):
                    return int(0)
                else:
                    return int(4)
        else:
            return int(0)
    else:
        return int(0)
def f_circle(x, a, b, r):
        y = sqrt(r**2 - (x - a)**2) + b
        return y
        '''
        y = sym.Symbol("y")
        solution = sym.solve((x - a)**2 + (y - b)**2 - r**2, y)
        return solution
        '''
def f_y_parabola(y, c, d):
    x = []
    x.append((-sqrt(c - y)) + d)
    x.append((sqrt(c - y)) + d)
    return x
def f_parabola(x, c, d):
        y = c - (x - d)**2
        return y
def solver_for_x(a, b, c, d, r):
        res = (np.roots([1, (-2*d-2*d), (-c-c+d*d+b+4*d*d+d*d+b+1), (2*c*d+2*c*d-2*a-2*d*d*d-2*b*d-2*d*d*d-2*b*d), (c*c-c*d*d-b*c-c*d*d+d*d*d*d+b*d*d-b*c+b*d*d+b*b+a*a-r*r)]))
        ret = []
        for i in res:
                mnim = i.imag
                if (abs(mnim) <= EPS):
                        ret.append(i.real)
        return ret
def solver_for_y(c, d, x):
        y = sym.Symbol("y")
        return sym.solve(c - (x - d)**2 - y, y)

def build_img(event, e_A, e_B, e_C, e_D, e_R):

    #try:
        a = e_A.get()
        b = e_B.get()
        c = e_C.get()
        d = e_D.get()
        r = e_R.get()
        if a == '' or b == '' or c == '' or d == '' or r == '':
                    pustoy_vvod
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        r = float(r)

        
        x_top_par = (-2 * d)/ (-2)
        y_top_par = f_parabola(x_top_par, c, d)
        
        cross_dots_x = solver_for_x(a, b, c, d, r)
        leftest = []
        rightest = []
        top = []
        low = []
        if (r < 0.0 or abs(r) <= EPS):
                mb.showerror("Ошибка!", "Отрицательный радиус")
                return ;
        if (len(cross_dots_x) == 0):
            if (is_par_over_cir(a, b, c, d, r) == 1):
                    leftest.append(a - r)
                    leftest.append(b)
                    
                    rightest.append(a + r)
                    rightest.append(b)
                    
                    top.append(a)
                    top.append(b + r)

                    low.append(a)
                    low.append(b - r)

                    center = []

                    center.append(a)
                    center.append(b)
            else:
                    mb.showerror("Ошибка!", "Парабола не пересекает окружность!")
                    return;
        else:
                cross_dots_y = []
                for i in cross_dots_x:
                    cross_dots_y.append(f_parabola(i, c, d))
                center = find_center(a, b, c, d, r, cross_dots_x, cross_dots_y, x_top_par, y_top_par)
                print(center)
                leftest.append(center[0])
                leftest.append(f_parabola(center[0], c, d))

                rightest.append(center[1])
                rightest.append(f_parabola(center[1], c, d))

                top.append(center[2])
                top.append(center[3])


                low.append(center[4])
                low.append(center[5])


        while(len(center) > 0):
            center.pop()
        center.append((leftest[0] + rightest[0]) / 2)
        center.append((top[1] + low[1]) / 2)
        maxi = max(rightest[0] - leftest[0], top[1] - low[1])
        print("center = ",center)
        holst = Canvas(root, width = 600, height = 600, bg = 'white')
        holst.place(anchor = "se", relx = 1, rely = 1)
        fig_obj = {"center":(center[0], center[1]),
                   "center_rotate":(center[0], center[1]),
                   "leftest":(leftest[0], leftest[1]),
                   "rightest":(rightest[0], rightest[1]),
                   "top":(top[0], top[1]),
                   "bottom":(low[0], low[1]),
                   "angle":0.0,
                   "scale":(1.0, 1.0),
                   "replace":(0.0, 0.0)}
        fig_dots = [[],[]]
        x_cyc = fig_obj["leftest"][0]
        l_screen = 200
        h_abstract = (600 * maxi / l_screen)
        
        while(x_cyc - fig_obj["center"][0] < fig_obj["rightest"][0] - fig_obj["center"][0]):
                
                y_1 = f_circle(x_cyc, a, b, r)
                y_2 = f_parabola(x_cyc, c, d)
                y_3 = -1.0 * (y_1 - (2 * b))


                x_to_print_par = scale(maxi, 200, x_cyc - fig_obj["center"][0]) + 300 + (600 * fig_obj["replace"][0] / h_abstract)

                x_to_print_cir_top = scale(maxi, 200, x_cyc - fig_obj["center"][0]) + 300 + (600 * fig_obj["replace"][0] / h_abstract)

                x_to_print_cir_low = scale(maxi, 200, x_cyc - fig_obj["center"][0]) + 300 + (600 * fig_obj["replace"][0] / h_abstract)
                
                y_to_print_cir_low = 300 - scale(maxi, 200, y_3 - fig_obj["center"][1]) + (600 * fig_obj["replace"][1] / h_abstract)
                
                y_to_print_par = 300 - scale(maxi, 200, y_2 - fig_obj["center"][1]) + (600 * fig_obj["replace"][1] / h_abstract)
                
                y_to_print_cir_top = 300 - scale(maxi, 200, y_1 - fig_obj["center"][1]) + (600 * fig_obj["replace"][1] / h_abstract)



                fig_dots[0].append(x_to_print_cir_low)
                fig_dots[1].append(y_to_print_cir_low)
                if (y_2 < y_1):
                    fig_dots[0].append(x_to_print_par)
                    fig_dots[1].append(y_to_print_par)
                if (y_2 >= y_1):
                    fig_dots[0].append(x_to_print_cir_top)
                    fig_dots[1].append(y_to_print_cir_top)
                x_cyc += 0.0025
        draw_fig_by_dots(fig_obj, fig_dots, holst)
        b_move = Button(root, text = "Перемещение")
        b_move.bind('<Button-1>', lambda e: goto_move(e, holst, fig_obj, maxi, fig_dots))
        b_move.place(anchor = "sw", x = 10, y = 475)

        b_rotate = Button(root, text = "Поворот")
        b_rotate.bind('<Button-1>', lambda e: goto_rotate(e, holst, fig_obj,fig_dots, maxi))
        b_rotate.place(anchor = "sw", x = 10, y = 450)

        b_scaler = Button(root, text = "Масштабирование")
        b_scaler.bind('<Button-1>', lambda e: goto_scale(e, holst,fig_obj, fig_dots, maxi))
        b_scaler.place(anchor = "sw", x = 10, y = 500)
        
    
    #except NameError:
     #       mb.showerror("Ошибка!", "Все поля должны быть заполнены")
    #except:
     #   mb.showerror("Ошибка!", "Введены некорректные данные")
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

width = width // 2
height = height // 2
width -= 200
height -= 200

root.geometry('500x500+{}+{}'.format(width, height))

button_begin = Button(root, text = "Начать", width = 6, height = 1, font = 'arial 14')
l_main = Label(text = "Построить заштрихованную фигуру,\n\
затем её переместить, промасштабировать,\n повернуть.",\
               bg = 'white', fg = 'black', font = 'arial 14')
l_main.pack()

canvas = Canvas(root, height=200, width=700)
image = Image.open("img.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)

canvas.place(relx = 0, rely = 0.2)
button_begin.bind('<Button-1>', goto_main)
button_begin.place(anchor = "se", relx = 1, rely = 1)
root.mainloop()
