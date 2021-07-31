from tkinter import *
from geom import *
from tkinter import messagebox as mb
HOLST_WIDTH = 600
HOLST_HEIGHT = 600
x_arr = []
y_arr = []
def solve_problem(x_arr, y_arr):
    min_ang = 181.0
    min_trg = [0] * 6
    min_mid = [0] * 4
    min_hght = [0] * 4
    for i in range(len(x_arr)):
        for j in range(len(x_arr)):
            for k in range(len(x_arr)):
                if i != j and i != k and j != k and (is_line(x_arr[i], y_arr[i], x_arr[j], y_arr[j], x_arr[k], y_arr[k], )) != True:
                    
                    mid = find_med(x_arr[i], y_arr[i], x_arr[j], y_arr[j], x_arr[k], y_arr[k])
                    hght = find_height(x_arr[i], y_arr[i], x_arr[j], y_arr[j], x_arr[k], y_arr[k])

                    #print("find angle for ", x_arr[i],';',y_arr[i],"   ", x_arr[j],';',y_arr[j],"   ", x_arr[k],';',y_arr[k],"   ",'\n')
                    ang = find_ang(hght, mid)

                    if (ang < min_ang):

                        min_ang = ang

                        min_mid = mid
                        min_hght = hght
                        
                        min_trg[0] = round(x_arr[i],2)
                        min_trg[1] = round(y_arr[i],2)
                        min_trg[2] = round(x_arr[j],2)
                        min_trg[3] = round(y_arr[j],2)
                        min_trg[4] = round(x_arr[k],2)
                        min_trg[5] = round(y_arr[k],2)
    if (min_ang < 180.0):
        print("Ответ:\n")
        print("\tКоординаты полученного треугольника:\n\t (", min_trg[0], ";", min_trg[1],")\n\t (", min_trg[2], ";", min_trg[3], ")\n\t (",min_trg[4], ";", min_trg[5],")\n")
        #print("\tКоординаты медианы: (", round(min_mid[0],2), ";", round(min_mid[1],2), ") (", round(min_mid[2],2), ";", round(min_mid[3],2), ")\n")
        #print("\tКоординаты высоты: (", round(min_hght[0],2), ";", round(min_hght[1],2), ") (", round(min_hght[2],2), ";", round(min_hght[3],2), ")\n")
        print("\tУгол между полученными медианой и высотой:", round(min_ang, 2), " градусов\n")
    return [min_trg, min_mid, min_hght]
def free_zones(x, y):
    if (abs(x) > EPS):
        if (x > 0):
            if (abs(y) > EPS):
                if (y > 0):
                    return "ne"
                else:
                    return "se"
            else:
                return "se"
        else:
            if (abs(y) > EPS):
                if (y > 0):
                    return "nw"
                else:
                    return "sw"
            else:
                return "sw"
    else:
        if (abs(y) > EPS):
            if (y > 0):
                return "nw"
            else:
                return "s"
        else:
            return "n"
        
def del_all(event):
    pass
def draw_dots(init_trg, init_hght, init_med):
    holst.delete("all")
    real_trg = []
    real_med = []
    real_hght = []
    for i in range(len(init_trg)):
        real_trg.append(round(init_trg[i], 2))
    for i in range(len(init_hght)):
        real_hght.append(round(init_hght[i], 2))
    for i in range(len(init_med)):
        real_med.append(round(init_med[i], 2))
    same_m_h = 1
    ans = scale_values(init_trg, init_hght, init_med)
    trg = ans[0]
    med = ans[1]
    hght = ans[2]
    for i in range(len(hght)):
        if (abs(hght[i] - med[i])) > EPS:
            same_m_h = 0
    l_med = Label(text = "- Медиана", fg = 'green',font = "arial 10")
    l_med.place(anchor = "nw",x = 630, y = 480)
    if (same_m_h == 1):
        l_hght = Label(text = "- Высота", fg = 'green',font = "arial 10")
    else:
        l_hght = Label(text = "- Высота", fg = 'red',font = "arial 10")
    l_hght.place(anchor = "nw", x = 630, y = 510)  
    #print(trg, hght, med)
    #holst.create_line(300, 0, 300, 600, fill = 'black')
    #holst.create_line(0, 300, 600, 300, fill = 'black')

    holst.create_polygon((trg[0] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - trg[1]), (trg[2]+ HOLST_WIDTH // 2, HOLST_WIDTH // 2 - trg[3]), (trg[4]+ HOLST_WIDTH // 2, HOLST_WIDTH // 2 -trg[5]), fill = 'white', outline = 'black')
    holst.create_line(hght[0] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - hght[1], hght[2] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - hght[3], fill = 'red', width = 2)
    holst.create_line(med[0] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - med[1], med[2] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - med[3], fill = 'green', width = 2)
    #print("real is ", real_trg, real_med, real_hght)
    holst.create_text((trg[0] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - trg[1]), text = f"({real_trg[0]};{real_trg[1]})", font = 'arial 12', anchor = free_zones(real_trg[0], real_trg[1]))
    holst.create_text((trg[2] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - trg[3]), text = f"({real_trg[2]};{real_trg[3]})", font = 'arial 12', anchor = free_zones(real_trg[2], real_trg[3]))
    holst.create_text((trg[4] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - trg[5]), text = f"({real_trg[4]};{real_trg[5]})", font = 'arial 12', anchor = free_zones(real_trg[4], real_trg[5]))
    #holst.create_text(( hght[2] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - hght[3]), text = f"({real_hght[2]};{real_hght[3]})", anchor = free_zones(real_hght[2], real_hght[3]))
    #holst.create_text(( med[2] + HOLST_WIDTH // 2, HOLST_WIDTH // 2 - med[3]), text = f"({real_med[2]};{real_med[3]})", anchor = free_zones(real_med[2], real_med[3]))
    
def input_n(event):
    global e_input_n, b_next, l_input_n
    l_main.destroy()
    button_begin.destroy()
    l_input_n = Label(text = "Введите количество точек(целое положительное число):", bg = 'white', fg = 'black', font = 'arial 14')
    l_input_n.pack()
    
    e_input_n = Entry(borderwidth  = l_input_n['width'], font = 'arial 14')
    e_input_n.place(anchor = "center", relx = 0.5, rely = 0.5)
    
    b_next = Button(root, text = "Далее", width = 6, height = 1, font = 'arial 14')
    b_next.bind('<Button-1>', main_window)
    b_next.place(anchor = "se", relx = 1, rely = 1)
def check_dots_input(event):
    '''global x_arr, y_arr
    x_arr = []
    y_arr = []
    '''
    while len(x_arr) != 0:
        x_arr.pop()
        y_arr.pop()
    try:
        for i in range (len(e_x)):
                flag_minus_x = 0
                flag_minus_y = 0
                x_arr.append(e_x[i].get())
                y_arr.append(e_y[i].get())
                if x_arr[i] == '' or y_arr[i] == '':
                    pustoy_vvod
                if x_arr[i][0] == '-':
                    flag_minus_x = 1
                if y_arr[i][0] == '-':
                    flag_minus_y = 1
                x_arr[i] = float(x_arr[i])
                y_arr[i] = float(y_arr[i])
                if (flag_minus_x == 1):
                    if (abs(x_arr[i]) <= EPS):
                        minus_noll = 1 // 0
                if (flag_minus_y == 1):
                    if (abs(y_arr[i]) <= EPS):
                        minus_noll = 1 // 0
        
        ans = solve_problem(x_arr, y_arr)
                
        flag = 1
        for i in range(6):
                    if ans[0][i] != 0:
                        flag = 0
        if (flag == 1):
                    mb.showerror("Ошибка!", "Невозможно построить треугольник по данным точкам")
                    holst.delete("all")
                    l_med.destroy()
                    l_hght.destroy()
                    for i in range (len(e_x)):
                            e_x[i].delete(0, END)
                            e_y[i].delete(0, END)
        else:
                    draw_dots(ans[0], ans[1], ans[2])
    except NameError:
        mb.showerror("Ошибка!", "Должны быть заполнены все поля\n")
        holst.delete("all")
        l_med.destroy()
        l_hght.destroy()


        
    except:
        mb.showerror("Ошибка!", "Некорректный ввод вещественных чисел\n");
        holst.delete("all")
        l_med.destroy()
        l_hght.destroy()

        
        for i in range (len(e_x)):
                e_x[i].delete(0, END)
                e_y[i].delete(0, END)
def add_dot(event, koord_x_l_numb):
    global n, koord_y_l_numb
    if n == 10:
        mb.showerror("Ошибка!","Точек должно быть не больше 10\n")
    else:
            l_numb = Label(text = n + 1, font = 'arial 12')
            l_numb.place(anchor = "se", x = koord_x_l_numb, y = koord_y_l_numb)
            l_number.append(l_numb)

            ex = Entry(bd = 3,width = 9, font = 'arial 8')
            ex.place(anchor = "sw", x = 640, y = koord_y_l_numb)
            e_x.append(ex)

            ey = Entry(bd = 3, width = 9, font = 'arial 8')
            ey.place(anchor = "sw", x = 740, y = koord_y_l_numb)
            e_y.append(ey)

            koord_y_l_numb += 40

            n += 1
def del_dot_by_num(event, e_del, koord_x_l_numb, del_win):
    global n, koord_y_l_numb
    ind = e_del.get()
    try:
        ind = int(ind)
        if ind > n or ind < 1:
                mb.showerror("Ошибка!","Введено некорректное значение.Надо от 1 до ", n)
        else:
            if n == 3:
                mb.showerror("Ошибка!","Точек должно быть не меньше 3х\n")
            else:
                koord_y_l_numb = 70
                if len(x_arr) != 0 and ind < len(x_arr):
                    x_arr.remove(x_arr[ind - 1])
                    y_arr.remove(y_arr[ind - 1])
                
                e_x[ind - 1].destroy()
                e_y[ind - 1].destroy()
                e_x.remove(e_x[ind - 1])
                e_y.remove(e_y[ind - 1])


                l_number[n - 1].destroy()
                l_number.pop()
                for i in range(n - 1):
                    l_n = Label(text = (i + 1), font = 'arial 12')
                    l_number[i] = l_n

                n -= 1
                
                for i in range(n):
                            
                        l_number[i].place(anchor = "se", x = koord_x_l_numb, y = koord_y_l_numb)

                        e_x[i].place(anchor = "sw", x = 640, y = koord_y_l_numb)

                        e_y[i].place(anchor = "sw", x = 740, y = koord_y_l_numb)
                        
                        koord_y_l_numb += 40

        del_win.destroy()
    except NameError:
        mb.showerror("Ошибка!", "Должны быть заполнены все поля")
    except:
        mb.showerror("Ошибка!", "Введено некорректное значение")
def del_dot(event, koord_x_l_numb):
    global n, koord_y_l_numb
    if n == 3:
        mb.showerror("Ошибка!", "Точек должно быть не меньше 3х\n")
    else:
        del_win = Toplevel()
        l_del = Label(del_win, text = "Введите номер удаляемой точки\n")
        l_del.pack()
        e_del = Entry(del_win, width = 10, font = 'arial 8')
        e_del.pack()
        b_del = Button(del_win, width = 10, text = "Ok", font = 'arial 8')
        b_del.bind('<Button-1>', lambda e: del_dot_by_num(e, e_del, koord_x_l_numb, del_win))
        b_del.pack()
        
def main_window(event):
    global  e_x, e_y, holst, l_number, l_med, l_hght
    global n, koord_y_l_numb
    try:
        n = e_input_n.get()
        n = int(n)
        #print(n)
        if (n < 3):
            mb.showerror("Ошибка!", "Точек должно быть не меньше 3\n")
        elif (n > 10):
            mb.showerror("Ошибка!", "Точек должно быть не больше 10\n")
        else:
            e_input_n.destroy()
            b_next.destroy()
            l_input_n.destroy()
            root.geometry('850x600+{}+{}'.format(width - 100,height - 100))
            holst = Canvas(root, width = HOLST_WIDTH, height = HOLST_HEIGHT, bg = 'white')
            holst.place(relx = 0, rely = 0)
            l_x = Label(text = "X", font = 'arial 14')
            l_y = Label(text = "Y", font = 'arial 14')
            l_med = Label()
            l_med.place(anchor = "nw",x = 630, y = 480)
            l_hght = Label()
            l_hght.place(anchor = "nw", x = 630, y = 510)  
            l_x.place(x = 660, y = 10)
            l_y.place(x = 750, y = 10)
            l_number = []
            e_x = []
            e_y = []
            koord_x_l_numb = 630
            koord_y_l_numb = 70
            for i in range(n):
                l_numb = Label(text = (i + 1), font = 'arial 12')
                l_numb.place(anchor = "se", x = koord_x_l_numb, y = koord_y_l_numb)
                l_number.append(l_numb)

                ex = Entry(bd = 3,width = 9, font = 'arial 8')
                ex.place(anchor = "sw", x = 640, y = koord_y_l_numb)
                e_x.append(ex)

                ey = Entry(bd = 3, width = 9, font = 'arial 8')
                ey.place(anchor = "sw", x = 740, y = koord_y_l_numb)
                e_y.append(ey)
                
                koord_y_l_numb += 40
            b_action = Button(text = "Запуск", font = 'arial 12')
            b_add_dot = Button(text = "Добавить точку", font = 'arial 12')
            b_del_dot = Button(text = "Удалить точку", font = 'arial 12')
            #b_del_all = Button(text = "Очистить всё", font = 'arial 12')
            
            b_action.bind('<Button-1>', check_dots_input)
            b_add_dot.bind('<Button-1>', lambda e:  add_dot(e, koord_x_l_numb))
            b_del_dot.bind('<Button-1>', lambda e: del_dot(e, koord_x_l_numb))
            '''
            b_del_all.bind('<Button-1>', delete_all)
            '''
            b_action.place(anchor = "se", x = 850, y = 600)
            b_add_dot.place(anchor = "se", x = 850, y = 560)
            b_del_dot.place(anchor = "se", x = 850, y = 520)
           # b_del_all.place(anchor = "se", x = 850, y = 480)
            
    except:
        mb.showerror("Ошибка!", "Введено некорректное число,\n повторите попытку\n")
        e_input_n.delete(0,END)
        
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

width = width // 2
height = height // 2

width -=200
height-=200

root.geometry('500x250+{}+{}'.format(width,height))


button_begin = Button(root, text = "Начать", width = 6, height = 1, font = 'arial 14')
l_main = Label(text = "На плоскости дано множество точек.\n Найти такой треугольник с вершинами в этих точках,\n у которого угол, образованный высотой и медианой,\n исходящих из одной вершины, минимален", bg = 'white', fg = 'black', font = 'arial 14')
l_main.pack()
button_begin.bind('<Button-1>', input_n)
button_begin.place(anchor = "se", relx = 1, rely = 1)
root.mainloop()
