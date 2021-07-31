from math import *
EPS = 1e-6
def find_med(x_beg, y_beg, x1, y1, x2, y2):
    med = []
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    med.append(x_beg)
    med.append(y_beg)
    med.append(x)
    med.append(y)
    return med
def find_height(x_beg, y_beg, x1, y1, x2, y2):
    #Вывел эти формулы из формул уравнения  прямой и формулы коэффициента наклона прямой.
    x = (x1 * x1 * x_beg - 2 * x1 * x2 * x_beg + x2 * x2 * x_beg + x2 *\
            (y1 - y2) * (y1 - y_beg) - x1 * (y1 - y2) * (y2 - y_beg)) / ((x1 - x2) *\
                    (x1 - x2) + (y1 - y2) * (y1 - y2))
    y = (x2 * x2 * y1 + x1 * x1 * y2 + x2 * x_beg * (y2 - y1) - x1 *\
            (x_beg * (y2 - y1) + x2 * (y1 + y2)) + (y1 - y2) * (y1 - y2) * y_beg) / ((\
                        x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    hght = []
    hght.append(x_beg)
    hght.append(y_beg)
    hght.append(x)
    hght.append(y)
    return hght
def find_ang(hght, med):
    x1 = hght[2] - hght[0]
    y1 = hght[3] - hght[1]
    x2 = med[2] - med[0]
    y2 = med[3] - med[1]
    #print("find angle for ", hght, med,'\n')
    angle = (x1 * x2 + y1 * y2)/(sqrt(x1 * x1 + y1 * y1) * sqrt(x2 * x2 + y2 * y2))
    #print(angle)
    if (angle > 0):
        if (abs(angle - 1.0) <= EPS):
            angle = 1.0
           # print("was 1\n")
    elif (angle < 0):
        if (abs(angle + 1.0) <= EPS):
            angle = -1.0
            #print("was -1\n")
    angle = acos(angle)
    angle = degrees(angle)
    #print("angle is ", angle)
    return angle
def is_line(x1,y1,x2,y2,x3,y3):
    return (1 / 2 * ((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))) <= EPS
def scale(maxi, holst_size, scaled_val):
    return (holst_size * scaled_val) / maxi
def scale_values(trg, hght, med):
    maxi = trg[0]
    for i in range(len(trg)):
        if abs(trg[i]) > maxi:
            maxi = abs(trg[i])
    holst_size = 290
    for i  in range(len(trg)):
        trg[i] = scale(maxi, holst_size, trg[i])
    for i in range(len(hght)):
        hght[i] = scale(maxi, holst_size, hght[i])
    for i in range(len(med)):
        med[i] = scale(maxi, holst_size, med[i])
    return [trg, hght, med]
    
    
'''
x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())

print(find_height(x1,y1,x2,y2,x3,y3))
print(find_ang(find_height(x1,y1, x2,y2,x3,y3), find_med(x1,y1,x2,y2,x3,y3)))
'''
