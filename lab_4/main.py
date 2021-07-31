from tkinter import *
from math import *
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tkinter import messagebox as mb
CIRCLE = 0
ELLIPSE = 1
LIB_FUNC = 0
CANON = 1
PARAM = 2
BR = 3
MIDP = 4
#EPS = 1e-12
RED = 1
GREEN = 2
BLUE = 3
WHITE = 0
def show_stat(event):
    COLOR = [255, 255, 255]
    if (var.get() == CIRCLE):
        x_c = 300
        y_c = 300
        x = np.arange(100, 1000, 150)
        alg_time = [[], [], [], [], []]
        ind = 0
        for j in x:
            for i in range(5):
                if (i == LIB_FUNC):
                    start = time.clock()
                    lib_circle(x_c, y_c, j, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == CANON):
                    start = time.clock()
                    canon_circle(x_c, y_c, j, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == PARAM):
                    start = time.clock()
                    param_circle(x_c, y_c, j, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == BR):
                    start = time.clock()
                    br_circle(x_c, y_c, j, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == MIDP):
                    start = time.clock()
                    midp_circle(x_c, y_c, j, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
            ind += 1
        plt.plot(x, alg_time[0], label = "Библиотечная функция")
        plt.plot(x, alg_time[1], label = "Канoническое уравнение")
        plt.plot(x, alg_time[2], label = "Параметрическое уравнение")
        plt.plot(x, alg_time[3], label = "Алгоритм Брезенхэма")
        plt.plot(x, alg_time[4], label = "Алгоритм средней точки")

        plt.legend()

        plt.xlabel('Размеры') 
        plt.ylabel('Время')

        plt.grid()

        plt.show()
    elif (var.get() == ELLIPSE):
        
        x_c = 300
        y_c = 300
        x = np.arange(100, 1000, 150)
        x_const = 100
        alg_time = [[], [], [], [], []]
        ind = 0
        for j in x:
            for i in range(5):
                if (i == LIB_FUNC):
                    start = time.clock()
                    lib_ellipse(x_c, y_c, j, x_const, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == CANON):
                    start = time.clock()
                    canon_ellipse(x_c, y_c, j, x_const, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == PARAM):
                    start = time.clock()
                    param_ellipse(x_c, y_c, j, x_const, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == BR):
                    start = time.clock()
                    br_ellipse(x_c, y_c, j, x_const, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
                elif (i == MIDP):
                    start = time.clock()
                    midp_ellipse(x_c, y_c, j, x_const, COLOR)
                    stop = time.clock()
                    alg_time[i].append(stop - start)
            ind += 1
        plt.plot(x, alg_time[0], label = "Библиотечная функция")
        plt.plot(x, alg_time[1], label = "Канoническое уравнение")
        plt.plot(x, alg_time[2], label = "Параметрическое уравнение")
        plt.plot(x, alg_time[3], label = "Алгоритм Брезенхэма")
        plt.plot(x, alg_time[4], label = "Алгоритм средней точки")

        plt.legend()

        plt.xlabel('Размеры') 
        plt.ylabel('Время')

        plt.grid()

        plt.show()

def build_circle(event, x_c, y_c, r):
        COLOR = []
        if (var2.get() == BLUE):
            COLOR.append(0)
            COLOR.append(0)
            COLOR.append(255)
        elif (var2.get() == GREEN):
            COLOR.append(0)
            COLOR.append(255)
            COLOR.append(0)
        elif (var2.get() == RED):
            COLOR.append(255)
            COLOR.append(0)
            COLOR.append(0)
        elif (var2.get() == WHITE):
            COLOR.append(255)
            COLOR.append(255)
            COLOR.append(255)
        if (var1.get() == CANON):
            start_time = time.perf_counter()
            canon_circle(x_c, y_c, r, COLOR)
        elif (var1.get() == PARAM):
            param_circle(x_c, y_c, r, COLOR)
        elif (var1.get() == BR):
            br_circle(x_c, y_c, r, COLOR)
        elif (var1.get() == LIB_FUNC):
            holst.create_oval(x_c - r, y_c - r, x_c + r, y_c + r,outline = color_translate(COLOR))
        elif (var1.get() == MIDP):
            midp_circle(x_c, y_c, r, COLOR)
def build_ellipse(event, x_c, y_c, r1, r2):
        COLOR = []
        if (var2.get() == BLUE):
            COLOR.append(0)
            COLOR.append(0)
            COLOR.append(255)
        elif (var2.get() == GREEN):
            COLOR.append(0)
            COLOR.append(255)
            COLOR.append(0)
        elif (var2.get() == RED):
            COLOR.append(255)
            COLOR.append(0)
            COLOR.append(0)
        elif (var2.get() == WHITE):
            COLOR.append(255)
            COLOR.append(255)
            COLOR.append(255)
        if (var1.get() == CANON):
            canon_ellipse(x_c, y_c, r1, r2, COLOR)
        elif (var1.get() == PARAM):
            param_ellipse(x_c, y_c, r1, r2, COLOR)
        elif (var1.get() == BR):
            br_ellipse(x_c, y_c, r1, r2, COLOR)
        elif (var1.get() == LIB_FUNC):
            holst.create_oval(x_c - r1, y_c - r2, x_c + r1, y_c + r2,outline = color_translate(COLOR))
        elif (var1.get() == MIDP):
            midp_ellipse(x_c, y_c, r1, r2, COLOR)
        
def color_translate(color):
    color_copy = []
    color_copy.append(color[0])
    color_copy.append(color[1])
    color_copy.append(color[2])
    clr = '#'
    for i in range(len(color_copy)):
        hx = str(hex(color_copy[i]))
        clr += hx[2:]
        if (len(hx) - 2 == 1):
            clr += '0'
    return clr
def draw_pix(x, y, clr):
    holst.create_line(x, y, x, y + 1, fill = clr)
def canon_circle(x_c, y_c, radius, color):
    y0 = y_c - radius
    for i in range(x_c - radius, x_c + radius, 1):
        y = sqrt(radius**2 - (i - x_c)**2)
        x = sqrt(radius**2 - (y0 - y_c)**2)
        draw_pix(i, y + y_c, color_translate(color))
        draw_pix(i, -y + y_c, color_translate(color))
        draw_pix(x + x_c, y0, color_translate(color))
        draw_pix(-x + x_c, y0, color_translate(color))
        y0 += 1
def canon_ellipse(x_c, y_c, r1, r2, color):
    y0 = y_c - r2
    for i in range(x_c - r1, x_c + r1):
        y = r2 * sqrt(1 - (i - x_c)**2/(r1**2)) 
        x = r1 * sqrt(1 - (y0 - y_c)**2/(r2**2))
        #print(x, y)

        draw_pix(i, y + y_c, color_translate(color))
        draw_pix(i, -y + y_c, color_translate(color))
        draw_pix(x + x_c, y0, color_translate(color))
        draw_pix(-x + x_c, y0, color_translate(color))
        
        y0 += r2/ r1
def lib_circle(x_c, y_c, r, color):
    holst.create_oval(x_c - r, y_c - r, x_c + r, y_c + r, outline = color_translate(color))
def lib_ellipse(x_c, y_c, r1, r2, color):
    holst.create_oval(x_c - r1, y_c - r2, x_c + r1, y_c + r2, outline = color_translate(color))

def param_circle(x_c, y_c, radius, color):
    t = 0
    while (t < 2 * pi):
        draw_pix(x_c + radius * cos(t), y_c + radius * sin(t), color_translate(color))
        t = t + 1/radius
def param_ellipse(x_c, y_c, r1, r2, color):
    t = 0
    while (t < 2 * pi):
        draw_pix(x_c + r1 * cos(t), y_c + r2 * sin(t), color_translate(color))
        t = t + 1/max(r1,r2)
def br_circle(x_c, y_c, rad, color):
    xi = 0
    yi = rad
    ei = 2 * (1 - rad)
    lim = 0
    clr = color_translate(color)
    for i in range(4):
        while(True):
            #print(xi, yi)
            draw_pix(xi + x_c, yi + y_c, clr)
            draw_pix(x_c - xi, yi + y_c, clr)
            draw_pix(xi + x_c, y_c - yi, clr)
            draw_pix(x_c - xi, y_c - yi, clr)
            if (yi <= lim ):
                break;
            if ei < 0:
                dlt = 2 * ei + 2 * yi - 1
                if (dlt <= 0):
                    xi = xi + 1
                    ei = ei + 2 * xi + 1
                elif (dlt > 0):
                    xi = xi + 1
                    yi = yi - 1
                    ei = ei + 2 * xi - 2 * yi + 2
            if (ei > 0):
                dlt = 2 * ei + 2 * xi - 1
                if (dlt <= 0):
                    xi = xi + 1
                    yi = yi - 1
                    ei = ei + 2 * xi - 2 * yi + 2
                elif (dlt > 0):
                    yi = yi - 1
                    ei = ei - 2 * yi + 1
            if (ei == 0):
                xi = xi + 1
                yi = yi - 1
                ei = ei + 2 * xi - 2 * yi + 2
def br_ellipse(x_c, y_c, r1, r2, color):
    xi = 0
    yi = r2
    ei = r2**2 - 2*(r1**2)*r2 + r1**2
    lim = 0
    clr = color_translate(color)
    sqr_r1 = r1 * r1
    sqr_r2 = r2 * r2
    for i in range(4):
        while(True):
            #print(xi, yi)
            draw_pix(xi + x_c, yi + y_c, clr)
            draw_pix(x_c - xi, yi + y_c, clr)
            draw_pix(xi + x_c, y_c - yi, clr)
            draw_pix(x_c - xi, y_c - yi, clr)
            if (yi <= lim ):
                break;
            if ei < 0:
                dlt = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi)**2 - sqr_r1 * sqr_r2 + sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2

                if (dlt <= 0):
                    xi = xi + 1
                    ei = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2
                elif (dlt > 0):
                    xi = xi + 1
                    yi = yi - 1
                    ei = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2
            if (ei > 0):
                dlt = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2 + sqr_r2 * (xi)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2
                if (dlt <= 0):
                    xi = xi + 1
                    yi = yi - 1
                    ei = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2
                elif (dlt > 0):
                    yi = yi - 1
                    ei = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2
            if (ei == 0):
                xi = xi + 1
                yi = yi - 1
                ei = sqr_r2 * (xi + 1)**2 + sqr_r1 * (yi - 1)**2 - sqr_r1 * sqr_r2

def midp_circle(x_c, y_c, r, color):
    x = r
    y = 0

    dlt = 1 - r

    draw_pix(x + x_c, y + y_c, color_translate(color))
    draw_pix(y + x_c, x + y_c, color_translate(color))

    draw_pix(x_c - x, y + y_c, color_translate(color))
    draw_pix(x_c - y, x + y_c, color_translate(color))
    
    draw_pix(x + x_c, y_c - y, color_translate(color))
    draw_pix(y + x_c, y_c - x, color_translate(color))
    
    draw_pix(x_c - x, y_c - y, color_translate(color))
    draw_pix(x_c - y, y_c - x, color_translate(color))

    while (x > y):
        y += 1
        if (dlt > 0):
            x-= 1
            dlt -= 2*x - 2
        dlt += 2 * y + 3
        draw_pix(x + x_c, y + y_c, color_translate(color))
        draw_pix(y + x_c, x + y_c, color_translate(color))

        draw_pix(x_c - x, y + y_c, color_translate(color))
        draw_pix(x_c - y, x + y_c, color_translate(color))
    
        draw_pix(x + x_c, y_c - y, color_translate(color))
        draw_pix(y + x_c, y_c - x, color_translate(color))
    
        draw_pix(x_c - x, y_c - y, color_translate(color))
        draw_pix(x_c - y, y_c - x, color_translate(color))

def midp_ellipse(x_c, y_c, r1, r2, color):
    sqr_r1 = r1 * r1
    sqr_r2 = r2 * r2
    limit = round(r1 / sqrt(1 + sqr_r2 / sqr_r1))
    
    xi = 0
    yi = r2

    draw_pix(xi + x_c, yi + y_c, color_translate(color))

    draw_pix(x_c - xi, yi + y_c, color_translate(color))
    
    draw_pix(xi + x_c, y_c - yi, color_translate(color))
    
    draw_pix(x_c - xi, y_c - yi, color_translate(color))
    func = sqr_r2 - round(sqr_r1 * (r2 - 1 / 4) )
    while xi < limit:
        if  func > 0:
            yi -= 1
            func -= sqr_r1 * yi * 2
        xi += 1
        func += sqr_r2 * (xi + xi + 1)
        draw_pix(xi + x_c, yi + y_c, color_translate(color))

        draw_pix(x_c - xi, yi + y_c, color_translate(color))
    
        draw_pix(xi + x_c, y_c - yi, color_translate(color))
    
        draw_pix(x_c - xi, y_c - yi, color_translate(color))
    
    limit = round(r2 / sqrt(1 + sqr_r1 / sqr_r2))

    xi = r1
    yi = 0

    func = sqr_r1 - round(sqr_r2 * (xi - 1 / 4))
    while yi < limit:
        if func > 0:
            xi -= 1
            func -= 2 * sqr_r2 * xi
        yi += 1
        func += sqr_r1 * (yi + yi + 1)
        draw_pix(xi + x_c, yi + y_c, color_translate(color))

        draw_pix(x_c - xi, yi + y_c, color_translate(color))
    
        draw_pix(xi + x_c, y_c - yi, color_translate(color))
    
        draw_pix(x_c - xi, y_c - yi, color_translate(color))
def input_values(inp_w, e_xc, e_yc, e_r1, e_r2):
    #try:
        x_c = e_xc.get(); x_c = int(x_c)
        y_c = e_yc.get(); y_c = int(y_c)
        
        r1 = e_r1.get(); r1 = int(r1)
       # print("INPUT WINDOW")
        if (var.get() == CIRCLE):
            build_circle(e, x_c, y_c, r1)
        else:
            r2 = e_r2.get(); r2 = int(r2)
            build_ellipse(e, x_c, y_c, r1, r2)
        inp_w.destroy()

    #except:
     #   mb.showerror("ERROR", "Incorrect values")
def input_window(event):
        inp_w = Toplevel()
        inp_w.geometry('500x500+{}+{}'.format(width, height))

        l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
        l_x0.place(anchor = "nw", relx = 0.0, rely = 0.5)
        l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
        l_y0.place(anchor = "nw", relx = 0.1, rely = 0.5)
        l_xn = Label(inp_w, text = "r1", font = "arial 12")
        l_xn.place(anchor = "nw", relx = 0.2, rely = 0.5)
        l_yn = Label(inp_w, text = "r2", font = "arial 12")
        l_yn.place(anchor = "nw", relx = 0.3, rely = 0.5)

        e_x_c = Entry(inp_w, font = "arial 12", width = 5)
        e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.55)
        e_y_c = Entry(inp_w, font = "arial 12", width = 5)
        e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.55)
        e_r1 = Entry(inp_w, font = "arial 12", width = 5)
        e_r1.place(anchor = "nw", relx = 0.2, rely = 0.55)
        e_r2 = Entry(inp_w, font = "arial 12", width = 5)
        e_r2.place(anchor = "nw", relx = 0.3, rely = 0.55)
        
        if (var.get() == CIRCLE):
            e_r2.configure(state="disabled")
        else:
            e_r2.configure(state="normal")

        ok_b = Button (inp_w, text = "OK")
        ok_b.place(anchor = "se", relx = 1, rely = 1)
        ok_b.bind('<Button-1>', lambda e: input_values(inp_w, e_x_c, e_y_c, e_r1, e_r2))
def input_spectre_window(event):
        inp_w = Toplevel()
        inp_w.geometry('500x500+{}+{}'.format(width, height))
        if (var.get() == CIRCLE):

            ft_rad = 0
            lt_rad = 1
            step = 2
            n = 3
            
            var_choice = IntVar()
            var_choice.set(0)

            l_hide = Label (inp_w, text = "Скрыть", font = "arial 12")
            l_hide.place(anchor = "nw", relx = 0.0, rely = 0.1)
            ft_r_b = Radiobutton(inp_w, text = "r1", variable = var_choice, value = ft_rad)
            lt_r_b = Radiobutton(inp_w, text = "r2", variable = var_choice, value = lt_rad)
            step_b = Radiobutton(inp_w, text = "Шаг", variable = var_choice, value = step)
            n_b = Radiobutton(inp_w, text = "N", variable = var_choice, value = n)
            
            ft_r_b.place(anchor = "nw", relx = 0.0, rely = 0.15)
            lt_r_b.place(anchor = "nw", relx = 0.0, rely = 0.2)
            step_b.place(anchor = "nw", relx = 0.4, rely = 0.15)
            n_b.place(anchor = "nw", relx = 0.4, rely = 0.2)
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: scnd_cir_win(inp_w, var_choice.get()))
        else:
            ft_rad = 0
            lt_rad = 1
            
            var_choice = IntVar()
            var_choice.set(0)

            l_hide = Label (inp_w, text = "Выберите полуось для изменения:", font = "arial 12")
            l_hide.place(anchor = "nw", relx = 0.0, rely = 0.1)
            ft_r_b = Radiobutton(inp_w, text = "a", variable = var_choice, value = ft_rad)
            lt_r_b = Radiobutton(inp_w, text = "b", variable = var_choice, value = lt_rad)
            
            ft_r_b.place(anchor = "nw", relx = 0.0, rely = 0.15)
            lt_r_b.place(anchor = "nw", relx = 0.0, rely = 0.2)
  
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: scnd_ell_win(inp_w, var_choice.get()))

def scnd_cir_win(inp_w, var_choice):
    inp_w.destroy()
    inp_w = Toplevel()
    inp_w.geometry('500x500+{}+{}'.format(width, height))
    if (var_choice == 0):
            l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
            l_x0.place(anchor = "nw", relx = 0.0, rely = 0.3)
            l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
            l_y0.place(anchor = "nw", relx = 0.1, rely = 0.3)
            l_r1 = Label(inp_w, text = "r1", font = "arial 12")
            l_r1.place(anchor = "nw", relx = 0.2, rely = 0.3)
            l_r2 = Label(inp_w, text = "r2", font = "arial 12")
            l_r2.place(anchor = "nw", relx = 0.3, rely = 0.3)
            l_step = Label(inp_w, text = "Шаг", font = "arial 12")
            l_step.place(anchor = "nw", relx = 0.4, rely = 0.3)
            l_N = Label(inp_w, text = "N", font = "arial 12")
            l_N.place(anchor = "nw", relx = 0.5, rely = 0.3)
            e_x_c = Entry(inp_w, font = "arial 12", width = 5)
            e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.35)
            e_y_c = Entry(inp_w, font = "arial 12", width = 5)
            e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.35)
            e_r1 = Entry(inp_w, font = "arial 12", width = 5)
            e_r1.place(anchor = "nw", relx = 0.2, rely = 0.35)
            e_r2 = Entry(inp_w, font = "arial 12", width = 5)
            e_r2.place(anchor = "nw", relx = 0.3, rely = 0.35)
            e_step = Entry(inp_w, font = "arial 12", width = 5)
            e_step.place(anchor = "nw", relx = 0.4, rely = 0.35)
            e_N = Entry(inp_w, font = "arial 12", width = 5)
            e_N.place(anchor = "nw", relx = 0.5, rely = 0.35)
            e_r1.configure(state = "disabled")
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: win_sp_r1(e_x_c, e_y_c, e_r2, e_step, e_N))
    elif (var_choice == 1):
            l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
            l_x0.place(anchor = "nw", relx = 0.0, rely = 0.3)
            l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
            l_y0.place(anchor = "nw", relx = 0.1, rely = 0.3)
            l_r1 = Label(inp_w, text = "r1", font = "arial 12")
            l_r1.place(anchor = "nw", relx = 0.2, rely = 0.3)
            l_r2 = Label(inp_w, text = "r2", font = "arial 12")
            l_r2.place(anchor = "nw", relx = 0.3, rely = 0.3)
            l_step = Label(inp_w, text = "Шаг", font = "arial 12")
            l_step.place(anchor = "nw", relx = 0.4, rely = 0.3)
            l_N = Label(inp_w, text = "N", font = "arial 12")
            l_N.place(anchor = "nw", relx = 0.5, rely = 0.3)
            e_x_c = Entry(inp_w, font = "arial 12", width = 5)
            e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.35)
            e_y_c = Entry(inp_w, font = "arial 12", width = 5)
            e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.35)
            e_r1 = Entry(inp_w, font = "arial 12", width = 5)
            e_r1.place(anchor = "nw", relx = 0.2, rely = 0.35)
            e_r2 = Entry(inp_w, font = "arial 12", width = 5)
            e_r2.place(anchor = "nw", relx = 0.3, rely = 0.35)
            e_step = Entry(inp_w, font = "arial 12", width = 5)
            e_step.place(anchor = "nw", relx = 0.4, rely = 0.35)
            e_N = Entry(inp_w, font = "arial 12", width = 5)
            e_N.place(anchor = "nw", relx = 0.5, rely = 0.35)
            e_r2.configure(state = "disabled")
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: win_sp_r2(e_x_c, e_y_c, e_r1, e_step, e_N))
    elif (var_choice == 2):
            l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
            l_x0.place(anchor = "nw", relx = 0.0, rely = 0.3)
            l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
            l_y0.place(anchor = "nw", relx = 0.1, rely = 0.3)
            l_r1 = Label(inp_w, text = "r1", font = "arial 12")
            l_r1.place(anchor = "nw", relx = 0.2, rely = 0.3)
            l_r2 = Label(inp_w, text = "r2", font = "arial 12")
            l_r2.place(anchor = "nw", relx = 0.3, rely = 0.3)
            l_step = Label(inp_w, text = "Шаг", font = "arial 12")
            l_step.place(anchor = "nw", relx = 0.4, rely = 0.3)
            l_N = Label(inp_w, text = "N", font = "arial 12")
            l_N.place(anchor = "nw", relx = 0.5, rely = 0.3)
            e_x_c = Entry(inp_w, font = "arial 12", width = 5)
            e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.35)
            e_y_c = Entry(inp_w, font = "arial 12", width = 5)
            e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.35)
            e_r1 = Entry(inp_w, font = "arial 12", width = 5)
            e_r1.place(anchor = "nw", relx = 0.2, rely = 0.35)
            e_r2 = Entry(inp_w, font = "arial 12", width = 5)
            e_r2.place(anchor = "nw", relx = 0.3, rely = 0.35)
            e_step = Entry(inp_w, font = "arial 12", width = 5)
            e_step.place(anchor = "nw", relx = 0.4, rely = 0.35)
            e_N = Entry(inp_w, font = "arial 12", width = 5)
            e_N.place(anchor = "nw", relx = 0.5, rely = 0.35)
            e_step.configure(state = "disabled")
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: win_sp_step(e_x_c, e_y_c, e_r1, e_r2, e_N))
    elif (var_choice == 3):
            l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
            l_x0.place(anchor = "nw", relx = 0.0, rely = 0.3)
            l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
            l_y0.place(anchor = "nw", relx = 0.1, rely = 0.3)
            l_r1 = Label(inp_w, text = "r1", font = "arial 12")
            l_r1.place(anchor = "nw", relx = 0.2, rely = 0.3)
            l_r2 = Label(inp_w, text = "r2", font = "arial 12")
            l_r2.place(anchor = "nw", relx = 0.3, rely = 0.3)
            l_step = Label(inp_w, text = "Шаг", font = "arial 12")
            l_step.place(anchor = "nw", relx = 0.4, rely = 0.3)
            l_N = Label(inp_w, text = "N", font = "arial 12")
            l_N.place(anchor = "nw", relx = 0.5, rely = 0.3)
            e_x_c = Entry(inp_w, font = "arial 12", width = 5)
            e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.35)
            e_y_c = Entry(inp_w, font = "arial 12", width = 5)
            e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.35)
            e_r1 = Entry(inp_w, font = "arial 12", width = 5)
            e_r1.place(anchor = "nw", relx = 0.2, rely = 0.35)
            e_r2 = Entry(inp_w, font = "arial 12", width = 5)
            e_r2.place(anchor = "nw", relx = 0.3, rely = 0.35)
            e_step = Entry(inp_w, font = "arial 12", width = 5)
            e_step.place(anchor = "nw", relx = 0.4, rely = 0.35)
            e_N = Entry(inp_w, font = "arial 12", width = 5)
            e_N.place(anchor = "nw", relx = 0.5, rely = 0.35)
            e_N.configure(state = "disabled")
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: win_sp_N(e_x_c, e_y_c, e_r1, e_r2, e_step))

def scnd_ell_win(inp_w, var_choice):
    inp_w.destroy()
    inp_w = Toplevel()
    inp_w.geometry('500x500+{}+{}'.format(width, height))

    if (var_choice == 0):
            l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
            l_x0.place(anchor = "nw", relx = 0.0, rely = 0.3)
            l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
            l_y0.place(anchor = "nw", relx = 0.1, rely = 0.3)
            l_r1 = Label(inp_w, text = "r1", font = "arial 12")
            l_r1.place(anchor = "nw", relx = 0.2, rely = 0.3)
            l_r2 = Label(inp_w, text = "r2", font = "arial 12")
            l_r2.place(anchor = "nw", relx = 0.3, rely = 0.3)
            l_step = Label(inp_w, text = "Шаг", font = "arial 12")
            l_step.place(anchor = "nw", relx = 0.4, rely = 0.3)
            l_N = Label(inp_w, text = "N", font = "arial 12")
            l_N.place(anchor = "nw", relx = 0.5, rely = 0.3)
            e_x_c = Entry(inp_w, font = "arial 12", width = 5)
            e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.35)
            e_y_c = Entry(inp_w, font = "arial 12", width = 5)
            e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.35)
            e_r1 = Entry(inp_w, font = "arial 12", width = 5)
            e_r1.place(anchor = "nw", relx = 0.2, rely = 0.35)
            e_r2 = Entry(inp_w, font = "arial 12", width = 5)
            e_r2.place(anchor = "nw", relx = 0.3, rely = 0.35)
            e_step = Entry(inp_w, font = "arial 12", width = 5)
            e_step.place(anchor = "nw", relx = 0.4, rely = 0.35)
            e_N = Entry(inp_w, font = "arial 12", width = 5)
            e_N.place(anchor = "nw", relx = 0.5, rely = 0.35)
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: win_sp_1_ell(e_x_c, e_y_c, e_r1, e_r2, e_step, e_N))
    elif (var_choice == 1):
            l_x0 = Label(inp_w, text = "x_c", font = "arial 12")
            l_x0.place(anchor = "nw", relx = 0.0, rely = 0.3)
            l_y0 = Label(inp_w, text = "y_c", font = "arial 12")
            l_y0.place(anchor = "nw", relx = 0.1, rely = 0.3)
            l_r1 = Label(inp_w, text = "r1", font = "arial 12")
            l_r1.place(anchor = "nw", relx = 0.2, rely = 0.3)
            l_r2 = Label(inp_w, text = "r2", font = "arial 12")
            l_r2.place(anchor = "nw", relx = 0.3, rely = 0.3)
            l_step = Label(inp_w, text = "Шаг", font = "arial 12")
            l_step.place(anchor = "nw", relx = 0.4, rely = 0.3)
            l_N = Label(inp_w, text = "N", font = "arial 12")
            l_N.place(anchor = "nw", relx = 0.5, rely = 0.3)
            e_x_c = Entry(inp_w, font = "arial 12", width = 5)
            e_x_c.place(anchor = "nw", relx = 0.0, rely = 0.35)
            e_y_c = Entry(inp_w, font = "arial 12", width = 5)
            e_y_c.place(anchor = "nw", relx = 0.1, rely = 0.35)
            e_r1 = Entry(inp_w, font = "arial 12", width = 5)
            e_r1.place(anchor = "nw", relx = 0.2, rely = 0.35)
            e_r2 = Entry(inp_w, font = "arial 12", width = 5)
            e_r2.place(anchor = "nw", relx = 0.3, rely = 0.35)
            e_step = Entry(inp_w, font = "arial 12", width = 5)
            e_step.place(anchor = "nw", relx = 0.4, rely = 0.35)
            e_N = Entry(inp_w, font = "arial 12", width = 5)
            e_N.place(anchor = "nw", relx = 0.5, rely = 0.35)
            ok_b = Button (inp_w, text = "OK")
            ok_b.place(anchor = "se", relx = 1, rely = 1)
            ok_b.bind('<Button-1>', lambda e: win_sp_2_ell(e_x_c, e_y_c, e_r1, e_r2, e_step, e_N))
    
def win_sp_1_ell(e_x_c, e_y_c, e_r1, e_r2, e_step, e_N):
    try:
        x_c = e_x_c.get(); x_c = int(x_c)
        y_c = e_y_c.get(); y_c = int(y_c)
        r1 = e_r1.get(); r1 = int(r1)
        r2 = e_r2.get(); r2 = int(r2)
        step = e_step.get(); step = int(step)
        N = e_N.get(); N = int(N)
        if (r2 <= 0 or  r1 <= 0 or step <= 0 or N <= 0):
            mb.showerror("Ошибка!", "Некорректные значения")
            return;
        else:
            color = []
            if (var2.get() == BLUE):
                color.append(0)
                color.append(0)
                color.append(255)
            elif (var2.get() == GREEN):
                color.append(0)
                color.append(255)
                color.append(0)
            elif (var2.get() == RED):
                color.append(255)
                color.append(0)
                color.append(0)
            elif (var2.get() == WHITE):
                color.append(255)
                color.append(255)
                color.append(255)
            if (var1.get() == CANON):
                build_sp_1_ell(canon_ellipse, x_c, y_c, r1, r2, step, N, color)
            elif (var1.get() == PARAM):
                build_sp_1_ell(param_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == BR):
                build_sp_1_ell(br_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == LIB_FUNC):
                build_sp_1_ell(lib_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == MIDP):
                build_sp_1_ell(midp_ellipse, x_c, y_c, r1,  r2, step, N, color)
    except:
        mb.showerror("Ошибка", "Некорректные данные")

def win_sp_2_ell(e_x_c, e_y_c, e_r1, e_r2, e_step, e_N):
    try:
        x_c = e_x_c.get(); x_c = int(x_c)
        y_c = e_y_c.get(); y_c = int(y_c)
        r1 = e_r1.get(); r1 = int(r1)
        r2 = e_r2.get(); r2 = int(r2)
        step = e_step.get(); step = int(step)
        N = e_N.get(); N = int(N)
        if (r2 <= 0 or  r1 <= 0 or step <= 0 or N <= 0):
            mb.showerror("Ошибка!", "Некорректные значения")
            return;
        else:
            color = []
            if (var2.get() == BLUE):
                color.append(0)
                color.append(0)
                color.append(255)
            elif (var2.get() == GREEN):
                color.append(0)
                color.append(255)
                color.append(0)
            elif (var2.get() == RED):
                color.append(255)
                color.append(0)
                color.append(0)
            elif (var2.get() == WHITE):
                color.append(255)
                color.append(255)
                color.append(255)
            if (var1.get() == CANON):
                build_sp_2_ell(canon_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == PARAM):
                build_sp_2_ell(param_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == BR):
                build_sp_2_ell(br_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == LIB_FUNC):
                build_sp_2_ell(lib_ellipse, x_c, y_c, r1,  r2, step, N, color)
            elif (var1.get() == MIDP):
                build_sp_2_ell(midp_ellipse, x_c, y_c, r1,  r2, step, N, color)
    except:
        mb.showerror("Ошибка!", "Некорректные данные")
def build_sp_1_ell(func, x_c, y_c, r1, r2, step, N, color):
    n = 0
    while (n < N):
        func(x_c, y_c, r1, r2, color)
        r1 += step
        n += 1
def build_sp_2_ell(func, x_c, y_c, r1, r2, step, N, color):
    n = 0
    while (n < N):
        func(x_c, y_c, r1, r2, color)
        r2 += step
        n += 1

def win_sp_r1(e_x_c, e_y_c, e_r2, e_step, e_N):
    try:
        x_c = e_x_c.get(); x_c = int(x_c)
        y_c = e_y_c.get(); y_c = int(y_c)
        r2 = e_r2.get(); r2 = int(r2)
        step = e_step.get(); step = int(step)
        N = e_N.get(); N = int(N)
        if (r2 <= 0 or step <= 0 or N <= 0):
            mb.showerror("Ошибка!", "Некорректные значения")
            return;
        else:
            color = []
            if (var2.get() == BLUE):
                color.append(0)
                color.append(0)
                color.append(255)
            elif (var2.get() == GREEN):
                color.append(0)
                color.append(255)
                color.append(0)
            elif (var2.get() == RED):
                color.append(255)
                color.append(0)
                color.append(0)
            elif (var2.get() == WHITE):
                color.append(255)
                color.append(255)
                color.append(255)
            if (var1.get() == CANON):
                build_sp_r1(canon_circle, x_c, y_c, r2, step, N, color)
            elif (var1.get() == PARAM):
                build_sp_r1(param_circle, x_c, y_c, r2, step, N, color)
            elif (var1.get() == BR):
                build_sp_r1(br_circle, x_c, y_c, r2, step, N, color)
            elif (var1.get() == LIB_FUNC):
                build_sp_r1(lib_circle, x_c, y_c, r2, step, N, color)
            elif (var1.get() == MIDP):
                build_sp_r1(midp_circle, x_c, y_c, r2, step, N, color)
    except:
        mb.showerror("Ошибка!", "Некорректные данные")

def win_sp_r2(e_x_c, e_y_c, e_r1, e_step, e_N):
    try:
        x_c = e_x_c.get(); x_c = int(x_c)
        y_c = e_y_c.get(); y_c = int(y_c)
        r1 = e_r1.get(); r1 = int(r1)
        step = e_step.get(); step = int(step)
        N = e_N.get(); N = int(N)
        if (r1 < 0 or step <= 0 or N <= 0):
            mb.showerror("Ошибка!", "Некорректные значения")
            return;
        else:
            color = []
            if (var2.get() == BLUE):
                color.append(0)
                color.append(0)
                color.append(255)
            elif (var2.get() == GREEN):
                color.append(0)
                color.append(255)
                color.append(0)
            elif (var2.get() == RED):
                color.append(255)
                color.append(0)
                color.append(0)
            elif (var2.get() == WHITE):
                color.append(255)
                color.append(255)
                color.append(255)
            if (var1.get() == CANON):
                build_sp_r2(canon_circle, x_c, y_c, r1, step, N, color)
            elif (var1.get() == PARAM):
                build_sp_r2(param_circle, x_c, y_c, r1, step, N, color)
            elif (var1.get() == BR):
                build_sp_r2(br_circle, x_c, y_c, r1, step, N, color)
            elif (var1.get() == LIB_FUNC):
                build_sp_r2(lib_circle, x_c, y_c, r1, step, N, color)
            elif (var1.get() == MIDP):
                build_sp_r2(midp_circle, x_c, y_c, r1, step, N, color)
    except:
        mb.showerror("Ошибка!", "Некорректные данные")
def win_sp_step(e_x_c, e_y_c, e_r1, e_r2, e_N):
    try:
        x_c = e_x_c.get(); x_c = int(x_c)
        y_c = e_y_c.get(); y_c = int(y_c)
        r1 = e_r1.get(); r1 = int(r1)
        r2 = e_r2.get(); r2 = int(r2)
        N = e_N.get(); N = int(N)
        if (r2 <= 0 or r1 < 0 or N <= 0):
            mb.showerror("Ошибка!", "Некорректные значения")
            return;
        else:
            color = []
            if (var2.get() == BLUE):
                color.append(0)
                color.append(0)
                color.append(255)
            elif (var2.get() == GREEN):
                color.append(0)
                color.append(255)
                color.append(0)
            elif (var2.get() == RED):
                color.append(255)
                color.append(0)
                color.append(0)
            elif (var2.get() == WHITE):
                color.append(255)
                color.append(255)
                color.append(255)
            if (var1.get() == CANON):
                build_sp_step(canon_circle, x_c, y_c, r1, r2, N, color)
            elif (var1.get() == PARAM):
                build_sp_step(param_circle, x_c, y_c, r1, r2, N, color)
            elif (var1.get() == BR):
                build_sp_step(br_circle, x_c, y_c, r1, r2, N, color)
            elif (var1.get() == LIB_FUNC):
                build_sp_step(lib_circle, x_c, y_c, r1, r2, N, color)
            elif (var1.get() == MIDP):
                build_sp_step(midp_circle, x_c, y_c, r1, r2, N, color)
    except:
        mb.showerror("Ошибка!", "Некорректные данные")
def win_sp_N(e_x_c, e_y_c, e_r1, e_r2, e_step):
    try:
        x_c = e_x_c.get(); x_c = int(x_c)
        y_c = e_y_c.get(); y_c = int(y_c)
        r1 = e_r1.get(); r1 = int(r1)
        r2 = e_r2.get(); r2 = int(r2)
        step = e_step.get(); step = int(step)
        if (r2 <= 0 or r1 < 0 or step <= 0):
            mb.showerror("Ошибка!", "Некорректные значения")
            return;
        else:
            color = []
            if (var2.get() == BLUE):
                color.append(0)
                color.append(0)
                color.append(255)
            elif (var2.get() == GREEN):
                color.append(0)
                color.append(255)
                color.append(0)
            elif (var2.get() == RED):
                color.append(255)
                color.append(0)
                color.append(0)
            elif (var2.get() == WHITE):
                color.append(255)
                color.append(255)
                color.append(255)
            if (var1.get() == CANON):
                build_sp_n(canon_circle, x_c, y_c, r1, r2, step, color)
            elif (var1.get() == PARAM):
                build_sp_n(param_circle, x_c, y_c, r1, r2, step, color)
            elif (var1.get() == BR):
                build_sp_n(br_circle, x_c, y_c, r1, r2, step, color)
            elif (var1.get() == LIB_FUNC):
                build_sp_n(lib_circle, x_c, y_c, r1, r2, step, color)
            elif (var1.get() == MIDP):
                build_sp_n(midp_circle, x_c, y_c, r1, r2, step, color)
    except:
        mb.showerror("Ошибка!", "Некорректные данные")
def build_sp_r1(func, x_c, y_c, r2, step, N, color):
       
    r_i = r2
    n = 0
    while (r_i > 0):
        if (n == N):
            break
        func(x_c, y_c, r_i, color)
        r_i -= step
        n += 1
            
            
def build_sp_r2(func, x_c, y_c, r1, step, N, color):
    r_i = r1
    n = 0
    while (n < N):
        func(x_c, y_c, r_i, color)
        r_i += step
        n += 1
def build_sp_step(func, x_c, y_c, r1, r2, N, color):
    r_i = r1
    n = 0
    step = (e_r2 - e_r1) / N
    while (r_i < r2):
        if (n == N):
            break
        func(x_c, y_c, r_i, color)
        r_i += step
        n += 1
def build_sp_n(func, x_c, y_c, r1, r2, step, color):
    r_i = r1
    while (r_i < r2):
        func(x_c, y_c, r_i, color)
        r_i += step
def del_all(event):
    holst.delete("all")
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

width = width // 2
height = height // 2
width -= 700
height -= 400



kriv_l = Label(text = "Выбор кривой:", font = 'arial 12', fg = 'black')
kriv_l.place(anchor = "nw", relx = 0.3, rely = 0)

var = IntVar()
var.set(0)

circ_but = Radiobutton(text = "Окружность", variable = var, value = CIRCLE)
ell_but = Radiobutton(text = "Эллипс", variable = var, value = ELLIPSE)
circ_but.place(anchor = "nw", relx = 0.3, rely = 0.05)
ell_but.place(anchor = "nw", relx = 0.3, rely = 0.1)

var1 = IntVar()
var1.set(1)

alg_l = Label(text = "Выбор Алгоритма:", font = 'arial 12', fg = 'black')
alg_l.place(anchor = "nw", relx = 0, rely = 0)

lib_f_but = Radiobutton(text = "Библиотечная функция", variable = var1, value = LIB_FUNC)
canon_but = Radiobutton(text = "Каноническое уравнение", variable = var1, value = CANON)
param_but = Radiobutton(text = "Параметрическое уравнение", variable = var1, value = PARAM)
br_but = Radiobutton(text = "Брезенхем", variable = var1, value = BR)
midp_but = Radiobutton(text = "Средняя точка", variable = var1, value = MIDP)

lib_f_but.place(anchor = "nw", relx = 0.0, rely = 0.05)
canon_but.place(anchor = "nw", relx = 0.0, rely = 0.1)
param_but.place(anchor = "nw", relx = 0.0, rely = 0.15)
br_but.place(anchor = "nw", relx = 0.0, rely = 0.2)
midp_but.place(anchor = "nw", relx = 0.0, rely = 0.25)

col_l = Label(text = "Выбор Цвета:", font = 'arial 12', fg = 'black')
col_l.place(anchor = "nw", relx = 0, rely = 0.4)

var2 = IntVar()
var2.set(BLUE)

blue_but = Radiobutton(text = "Синий", fg = 'blue', variable = var2, value = BLUE)
green_but = Radiobutton(text = "Зелёный", fg = 'green', variable = var2, value = GREEN)
red_but = Radiobutton(text = "Красный", fg = 'red', variable = var2, value = RED)
white_but = Radiobutton(text = "Фоновый", fg = 'black', variable = var2, value = WHITE)


blue_but.place(anchor = "nw", relx = 0.0, rely = 0.45)
green_but.place(anchor = "nw", relx = 0.1, rely = 0.45)
red_but.place(anchor = "nw", relx = 0.2, rely = 0.45)
white_but.place(anchor = "nw", relx = 0.3, rely = 0.45)



inpt_b = Button(text = "Построить кривую")
inpt_b.bind('<Button-1>', input_window)
inpt_b.place(anchor = "nw", relx = 0.0, rely = 0.6)


build_puch = Button(text = "Построить спектр")
build_puch.bind('<Button-1>', input_spectre_window)
build_puch.place(anchor = "nw", relx = 0.0, rely = 0.8)







root.geometry('1400x700+{}+{}'.format(width, height))
holst = Canvas(root, width = 700, height = 700, bg = 'white')
holst.place(anchor = "se", relx = 1.0, rely = 1.0)

del_b = Button(text = "Очистить всё")
del_b.bind('<Button-1>', del_all)
del_b.place(anchor = "sw", relx = 0.3, rely = 0.95)

stat_b = Button(text = "Показать временную статистику")
stat_b.bind('<Button-1>', show_stat)
stat_b.place(anchor = "sw", relx = 0.3, rely = 1.0)

root.mainloop()
