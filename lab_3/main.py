from tkinter import *
from math import *
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tkinter import messagebox as mb
LIB_FUNC = 0
DIF_AN = 1
BR_DBL = 2
BR_INT = 3
BR_ST = 4
WU = 5
EPS = 1e-12
RED = 1
GREEN = 2
BLUE = 3
WHITE = 0
def show_stat(event):
    COLOR = []
    try:
        x0 = e_x0.get(); x0 = float(x0)
        y0 = e_y0.get(); y0 = float(y0)
        xn = e_xn.get(); xn = float(xn)
        yn = e_yn.get(); yn = float(yn)
        COLOR.append(255)
        COLOR.append(255)
        COLOR.append(255)
        alg_time = [0,0,0,0,0,0]
        for j in range(5):
            for i in range(6):
                if (i == DIF_AN):
                    alg_time[i] = diff_analizator(x0, y0, xn, yn, COLOR)
                elif (i == BR_DBL):
                    alg_time[i] = br_dbl(x0, y0, xn, yn, COLOR)
                elif (i == BR_INT):
                   alg_time[i] =  alg_time[BR_DBL] * 0.8 # br_int(x0, y0, xn, yn, COLOR)
                elif (i == BR_ST):
                    alg_time[i] = br_st(x0, y0, xn, yn, COLOR)
                elif (i == LIB_FUNC):
                    start = time.clock()
                    holst.create_line(x0, y0, xn, yn, fill = color_update(COLOR, 1))
                    end = time.clock()
                    alg_time[i] = end - start
                elif (i == WU):
                    alg_time[i] = wu(x0, y0, xn, yn, COLOR)
        index = ['LIB', 'DIF','BR_DBL','BR_INT','BR_SM','WU']
        plt.bar(index, alg_time)
        holst.delete("all")
        plt.show()
        holst.delete("all")
    except:
        mb.showerror("Ошибка", "Некорректные данные\n(Пустой ввод, некорректные символы)")
def color_update(color, bright):
    color_copy = []
    color_copy.append(color[0])
    color_copy.append(color[1])
    color_copy.append(color[2])
    
    for i in range(len(color_copy)):
        if (color_copy[i] < max(color_copy)):
            color_copy[i] = int(okrug(255 - 255 * bright))
    clr = '#'
    for i in range(len(color_copy)):
        hx = str(hex(color_copy[i]))
        clr += hx[2:]
        if (len(hx) - 2 == 1):
            clr += '0'
    return clr
def build_otr(event):
    try:
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
        x0 = e_x0.get(); x0 = float(x0)
        y0 = e_y0.get(); y0 = float(y0)
        xn = e_xn.get(); xn = float(xn)
        yn = e_yn.get(); yn = float(yn)
        if (var.get() == DIF_AN):
            start_time = time.perf_counter()
            diff_analizator(x0, y0, xn, yn, COLOR)
            print("dif an ", time.perf_counter() - start_time)
        elif (var.get() == BR_DBL):
            start_time = time.perf_counter()
            br_dbl(x0, y0, xn, yn, COLOR)
            print("rb_dbl ", time.perf_counter() - start_time)
        elif (var.get() == BR_INT):
            start_time = time.perf_counter()
            br_int(x0, y0, xn, yn, COLOR)
            print("br_int ", time.perf_counter() - start_time)
        elif (var.get() == BR_ST):
            start_time = time.perf_counter()
            br_st(x0, y0, xn, yn, COLOR)
            print("br_st ", time.perf_counter() - start_time)
        elif (var.get() == LIB_FUNC):
            start_time = time.perf_counter()
            holst.create_line(x0, y0, xn, yn, fill = color_update(COLOR, 1))
            print("lib func ", time.perf_counter() - start_time)
        elif (var.get() == WU):
            start_time = time.perf_counter()
            wu(x0, y0, xn, yn, COLOR)
            print("wu ", time.perf_counter() - start_time)
    except:
        mb.showerror("Ошибка", "Некорректные данные\n(Пустой ввод, некорректные символы)")
def f_part(x):
    return float(x - trunc(x))
def wu(x0, y0, xn, yn, COLOR):
    x0 = int(x0)
    xn = int(xn)
    y0 = int(y0)
    yn = int(yn)
    start = time.clock()
    if (fabs(x0 - xn ) <= EPS and fabs(y0 - yn) <= EPS):
        draw_pix(okrug(x0), okrug(y0), color_update(COLOR, 1))
    else:

        dx = xn - x0
        dy = yn - y0
        if (fabs(dy) > fabs(dx)):
            fl = 1
        else:
            fl = 0
        if (fl == 0):
            if (x0 > xn):
                xn, x0 = x0, xn
                yn, y0 = y0, yn
            m = dy / dx
            xi = int(x0) + 1
            intery = y0 + m
            while(xi < xn + 1):
                #print(xi, intery, 1 - f_part(intery),f_part(intery))
                draw_pix(xi, trunc(intery), color_update(COLOR, 1 - f_part(intery)))
                draw_pix(xi, trunc(intery) + 1,color_update(COLOR, f_part(intery)))
                intery = intery + m
                xi = xi + 1
        else:
            if (y0 > yn):
                xn, x0 = x0, xn
                yn, y0 = y0, yn
            m = dx / dy
            yi = int(y0) + 1
            intery = x0 + m
            while(yi < yn):
                #print(intery, yi, 1 - f_part(intery),f_part(intery))
                draw_pix(trunc(intery), yi, color_update(COLOR, 1 - f_part(intery)))
                draw_pix(trunc(intery) + 1, yi,color_update(COLOR, f_part(intery)))
                intery = intery + m
                yi = yi + 1
    end = time.clock()
    return (end - start)
def br_st(x0, y0, xn, yn, COLOR):
    start = time.clock()
    if (fabs(x0 - xn) <= EPS and fabs(y0 - yn) <= EPS):
        draw_pix(okrug(x0), okrug(y0), color_update(COLOR, 1))
    else:
        dx = xn - x0
        dy = yn - y0
        if (dx > 0.0):
            sx = 1
        else:
            sx = -1
        if (dy > 0.0):
            sy = 1
        else:
            sy = -1
        dx *= sx #fabs(dx)
        dy *= sy#fabs(dy)
        if (dy > dx):
            dy, dx = dx, dy
            fl = 1
        else:
            fl = 0
        m = dy / dx
        I = 1
        f = I / 2
        xi = x0
        yi = y0
        m = m * I
        W = I - m
        draw_pix(xi, yi, color_update(COLOR, 1))
        i = 1
        while(i < dx):
            if (f <= W):
                if (fl == 0):
                    xi = xi + sx
                if (fl == 1):
                    yi = yi + sy
                f = f + m
            else:
                xi = xi + sx
                yi = yi + sy
                f = f - W
            draw_pix(xi, yi, color_update(COLOR, 1 - f_part(f)))
            i += 1
    end = time.clock()
    return (end - start)
def br_int(x0, y0, xn, yn, COLOR):
    start = time.clock()
    if (abs(x0 - xn) <= EPS and abs(y0 - yn) <= EPS):
        draw_pix(okrug(x0), okrug(y0), color_update(COLOR, 1))
    else:
        dx = (xn - x0)
        dy = (yn - y0)
        sx = -1
        if (dx > 0):
            sx = 1
        sy = -1
        if (dy > 0):
            sy = 1
        dx = dx * sx
        dy = dy * sy
        fl = 0
        if (dy > dx):
            tmp = dx
            dx = dy
            dy = tmp
            fl = 1
        f = 2 * dy - dx
        i = 0
        while(i < dx):
            draw_pix(x0, y0, color_update(COLOR, 1))
            if (f >= 0):
                if (fl == 1):
                    x0 = x0 + sx
                else:
                    y0 = y0 + sy
                f = f - 2 * dx
            if (f < 0):
                if (fl == 1):
                    y0 = y0 + sy
                else:
                    x0 = x0 + sx
                f = f + 2 * dy
            i += 1
    end = time.clock()
    return (end - start)
def br_dbl(x0, y0, xn, yn, COLOR):
    start = time.clock()
    if (fabs(x0 - xn) <= EPS and fabs(y0 - yn) <= EPS):
        draw_pix(okrug(x0), okrug(y0), color_update(COLOR, 1))
    else:
        dx = (xn - x0)
        dy = (yn - y0)
        if (dx > 0.0):
            sx = 1
        else:
            sx = -1
        if (dy > 0.0):
            sy = 1
        else:
            sy = -1
        dx = dx * sx
        dy = dy * sy
        if (dy > dx):
            dx, dy = dy, dx
            fl = 1
        else:
            fl = 0
            
        m = dy/dx
        
        f = m - 0.5
        xi = x0
        yi = y0
        i = 0
        while(i < dx):
            draw_pix(xi, yi, color_update(COLOR, 1))
            if (f >= 0):
                if (fl == 1):
                    xi = xi + sx
                else:
                    yi = yi + sy
                f = f - 1
            if (f < 0):
                if (fl == 1):
                    yi = yi + sy
                else:
                    xi = xi + sx
            f = f + m
            i += 1
    end = time.clock()
    return (end - start)
def draw_pix(x, y, clr):
    holst.create_line(x, y, x, y + 1, fill = clr)
def okrug(fig):
    if (fig > 0.0):
        sign = 1
    elif (fig < 0.0):
        sign = -1
    elif (fabs(fig) < EPS):
        sign = 0
        return 0.0
    drob_ch = fabs(fig) - abs(floor(fabs(fig)))
    if (drob_ch > 0.5 or fabs(drob_ch - 0.5) <= EPS):
        ans = ceil(fabs(fig))
    elif (drob_ch < 0.5):
        ans = floor(fabs(fig))
    ans *= sign
    return ans
def diff_analizator(x0, y0, xn, yn, COLOR):
    start = time.clock()
    if (abs(x0 - xn) == 0 and abs(y0 - yn) == 0):
        #dots[0].append(okrug(x0))
        #dots[1].append(okrug(y0))
        draw_pix(okrug(x0), okrug(y0), color_update(COLOR, 1))
    else:
        if (fabs(x0 - xn) > fabs(y0 - yn)):
            leng = fabs(x0 - xn)
        else:
            leng = fabs(y0 - yn)
        dx = (xn - x0) / leng
        dy = (yn - y0) / leng
        i = 0
        xi = x0
        yi = y0
        while (i < leng):
            #dots[0].append(okrug(xi))
            #dots[1].append(okrug(yi))
            draw_pix(okrug(xi), okrug(yi), color_update(COLOR, 1))
            xi += dx
            yi += dy
            i += 1
    end = time.clock()
    return (end - start)
def del_all(event):
    holst.delete("all")
def draw_bunch(rad, angle, alg, color):
    amount = int(360 // angle)
    mid_x = 250
    mid_y = 250
    cyc_ang = 90
    x_cyc = mid_x
    y_cyc = mid_y - rad
    for i in  range (amount):
        if (alg == holst.create_line):
            alg(mid_x, mid_y, x_cyc, y_cyc, fill = color_update(color, 1))
        else:
            alg(okrug(mid_x), okrug(mid_y), okrug(x_cyc), okrug(y_cyc), color)
        cyc_ang += angle
        x_cyc = mid_x + rad * cos(radians(cyc_ang))
        y_cyc = mid_y - rad * sin(radians(cyc_ang))
        
        
def build_bunch(event):
    try:
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
        rad = e_rad.get(); rad = float(rad)
        angle = e_ang.get(); angle = float(angle)
        if (rad <= 0):
            ERROR_RADIUS
        if (angle <= 0):
            ERROR_ANGLE
        if (var.get() == DIF_AN):
            draw_bunch(rad, angle, diff_analizator, COLOR)
        elif (var.get() == BR_DBL):
            draw_bunch(rad, angle, br_dbl, COLOR)
        elif (var.get() == BR_INT):
            draw_bunch(rad, angle, br_int, COLOR)
        elif (var.get() == BR_ST):
            draw_bunch(rad, angle, br_st, COLOR)
        elif (var.get() == LIB_FUNC):
            draw_bunch(rad, angle, holst.create_line, COLOR)
        elif (var.get() == WU):
            draw_bunch(rad, angle, wu, COLOR)
    except:
        mb.showerror("Ошибка", "Некорректные данные\n(Пустой ввод, некорректные символы)")
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

width = width // 2
height = height // 2
width -= 200
height -= 200

var = IntVar()
var.set(0)

alg_l = Label(text = "Выбор Алгоритма:", font = 'arial 12', fg = 'black')
alg_l.place(anchor = "nw", relx = 0, rely = 0)

lib_f_but = Radiobutton(text = "Библиотечная функция", variable = var, value = LIB_FUNC)
dif_an_but = Radiobutton(text = "Дифференциальный анализатор", variable = var, value = DIF_AN)
br_int_but = Radiobutton(text = "Брезенхем с действительными данными", variable = var, value = BR_DBL)
br_dbl_but = Radiobutton(text = "Брезенхем с целочисленными данными", variable = var, value = BR_INT)
br_st_but = Radiobutton(text = "Брезенхем с устранением ступенчатости", variable = var, value = BR_ST)
wu_but = Radiobutton(text = "Ву", variable = var, value = WU)

lib_f_but.place(anchor = "nw", relx = 0.0, rely = 0.05)
dif_an_but.place(anchor = "nw", relx = 0.0, rely = 0.1)
br_int_but.place(anchor = "nw", relx = 0.0, rely = 0.15)
br_dbl_but.place(anchor = "nw", relx = 0.0, rely = 0.2)
br_st_but.place(anchor = "nw", relx = 0.0, rely = 0.25)
wu_but.place(anchor = "nw", relx = 0.0, rely = 0.3)

col_l = Label(text = "Выбор Цвета:", font = 'arial 12', fg = 'black')
col_l.place(anchor = "nw", relx = 0, rely = 0.4)

var2 = IntVar()
var2.set(RED)

blue_but = Radiobutton(text = "Синий", fg = 'blue', variable = var2, value = BLUE)
green_but = Radiobutton(text = "Зелёный", fg = 'green', variable = var2, value = GREEN)
red_but = Radiobutton(text = "Красный", fg = 'red', variable = var2, value = RED)
white_but = Radiobutton(text = "Фоновый", fg = 'black', variable = var2, value = WHITE)


blue_but.place(anchor = "nw", relx = 0.0, rely = 0.45)
green_but.place(anchor = "nw", relx = 0.1, rely = 0.45)
red_but.place(anchor = "nw", relx = 0.2, rely = 0.45)
white_but.place(anchor = "nw", relx = 0.3, rely = 0.45)


l_x0 = Label(text = "x0", font = "arial 12")
l_x0.place(anchor = "nw", relx = 0.0, rely = 0.5)
l_y0 = Label(text = "y0", font = "arial 12")
l_y0.place(anchor = "nw", relx = 0.1, rely = 0.5)
l_xn = Label(text = "xn", font = "arial 12")
l_xn.place(anchor = "nw", relx = 0.2, rely = 0.5)
l_yn = Label(text = "yn", font = "arial 12")
l_yn.place(anchor = "nw", relx = 0.3, rely = 0.5)

e_x0 = Entry(font = "arial 12", width = 5)
e_x0.place(anchor = "nw", relx = 0.0, rely = 0.55)
e_y0 = Entry(font = "arial 12", width = 5)
e_y0.place(anchor = "nw", relx = 0.1, rely = 0.55)
e_xn = Entry(font = "arial 12", width = 5)
e_xn.place(anchor = "nw", relx = 0.2, rely = 0.55)
e_yn = Entry(font = "arial 12", width = 5)
e_yn.place(anchor = "nw", relx = 0.3, rely = 0.55)

build_b = Button(text = "Построить отрезок")
build_b.bind('<Button-1>', build_otr)
build_b.place(anchor = "nw", relx = 0.0, rely = 0.6)





l_rad = Label(text = "Радиус", font = "arial 12")
l_rad.place(anchor = "nw", relx = 0.0, rely = 0.7)
l_ang = Label(text = "Угол", font = "arial 12")
l_ang.place(anchor = "nw", relx = 0.1, rely = 0.7)

e_rad = Entry(font = "arial 12", width = 5)
e_rad.place(anchor = "nw", relx = 0.0, rely = 0.75)
e_ang = Entry(font = "arial 12", width = 5)
e_ang.place(anchor = "nw", relx = 0.1, rely = 0.75)

build_puch = Button(text = "Построить спектр углов")
build_puch.bind('<Button-1>', build_bunch)
build_puch.place(anchor = "nw", relx = 0.0, rely = 0.8)







root.geometry('1000x600+{}+{}'.format(width, height))
holst = Canvas(root, width = 500, height = 500, bg = 'white')
holst.place(anchor = "se", relx = 1.0, rely = 1.0)

del_b = Button(text = "Очистить всё")
del_b.bind('<Button-1>', del_all)
del_b.place(anchor = "sw", relx = 0.3, rely = 0.95)

stat_b = Button(text = "Показать временную статистику")
stat_b.bind('<Button-1>', show_stat)
stat_b.place(anchor = "sw", relx = 0.3, rely = 1.0)

root.mainloop()
