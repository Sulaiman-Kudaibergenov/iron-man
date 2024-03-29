import turtle
import turtle as t
from random import randint
from turtle import *
color('red','#E4A424')

size = 10
t.Screen().bgcolor("#1298B9")


def pen_fun(t_1, line_1):
    t.penup()
    t.goto(line_1[0][0]*size,line_1[0][1]*size)
    t.pendown()
    t.color("red")
    
    for i in range(1, len(line_1)):
        t.goto(line_1[i][0]*size,line_1[i][1]*size)
    t.hideturtle()
    
#Line 1: 
t_1 = turtle.Pen()

line_1 = [(2, -3), (-2, -3), (-4, -1), (-5, 1), (-6, 5),
          (-6, 15), (-5, 17), (-3, 18), (3, 18), (5, 17), (6, 15),
          (6, 5), (5, 1), (4, -1), (2, -3)]

pen_fun(t_1, line_1)

#Line 2:
t_2 = turtle.Pen()

line_2 = [(-4, -1), (-4, 3), (-6, 6), (-5, 9), (-5, 15), 
          (-3, 16), (-2, 16), (-1, 11), (1, 11), (2, 16), 
          (3, 16), (5, 15), (5, 9), (6, 6), (4, 3), (4, -1)]

pen_fun(t_2, line_2)

#Line 3:
t_3 = turtle.Pen()

line_3 = [(-4, 1), (-3, 0), (-2, 1), (2, 1), (3, 0), (4, 1)]

pen_fun(t_3, line_3)

#Line 4:
t_4 = turtle.Pen()

line_4 = [(-4, 8), (-1, 7), (1, 7), (4, 8), (5, 7), (4, 6),
          (2, 6), (1, 7), (-1, 7), (-2, 6), (-4, 6), (-5, 7), (-4, 8)]

pen_fun(t_4, line_4)

#Line 5:
t_5 = turtle.Pen()

line_5 = [(-6, 5), (-9, 5), (-11, 4), (-11, 3), (-15, 3), (-20, 1)]

pen_fun(t_5, line_5)

#Line 6:
t_6 = turtle.Pen()

line_6 = [(6, 5), (9, 5), (11, 4), (11, 3), (15, 3), (20, 1)]

pen_fun(t_6, line_6)

#Line 7:
t_7 = turtle.Pen()

line_7 = [(-13, -20), (-14, -16), (-13, -13), (-14, -10), (-15, -13), 
          (-16, -17), (-18, -20)]

pen_fun(t_7, line_7)

#Line 8:
t_8 = turtle.Pen()

line_8 = [(13, -20), (14, -16), (13, -13), (14, -10), (15, -13), 
          (16, -17), (18, -20)]

pen_fun(t_8, line_8)

#Line 9:
t_9 = turtle.Pen()

line_9 = [(-13, -11), (-12, -10), (-12, -8), (-11, -8), (-10, -6), 
          (-8, -6), (-2, -9), (2, -9), (8, -6), (10, -6), (11, -8), (12, -8), (12, -10), (13, -11)]

pen_fun(t_9, line_9)

#Line 10:
t_10 = turtle.Pen()

line_10 = [(-2, -14), (-1, -13), (1, -13), (2, -14), (2, -17), 
          (1, -18), (-1, -18), (-2, -17), (-2, -14)]

pen_fun(t_10, line_10)

#Line 11:
t_11 = turtle.Pen()

line_11 = [(6, 4), (7, 1), (6, -5), (8, -2), (10, -3), (11, -5), (11, -6), 
           (12, -6), (14, -3), (17, -3), (20, -4), (17, -3), (14, -3), (14, 1), (13, 3)]

pen_fun(t_11, line_11)

#Line 12:
t_12 = turtle.Pen()

line_12 = [(-6, 4), (-7, 1), (-6, -5), (-8, -2), (-10, -3), (-11, -5), (-11, -6), 
           (-12, -6), (-14, -3), (-17, -3), (-20, -4), (-17, -3), (-14, -3), (-14, 1), (-13, 3)]

pen_fun(t_12, line_12)

#Line 13:
t_13 = turtle.Pen()

line_13 = [(5, -13), (6, -14), (6, -17), (3, -20), (2, -19), (-2, -19), (-2, -19), 
           (-4, -17), (-4, -14), (-2, -12), (2, -12), (4, -9), (8, -8), (11, -8)]

pen_fun(t_13, line_13)

#Line 14:
t_14 = turtle.Pen()

line_14 = [(-5, -13), (-6, -14), (-6, -17), (-3, -20), (-2, -19), (2, -19), (2, -19), 
           (4, -17), (4, -14), (2, -12), (-2, -12), (-4, -9), (-8, -8), (-11, -8)]

pen_fun(t_14, line_14)

#Line 15:
t_15 = turtle.Pen()

line_15 = [(-5, -4), (-2, -5), (-1, -6), (1, -6), (2, -5), (5, -4)]

pen_fun(t_15, line_15)

#Line 16:
t_16 = turtle.Pen()

line_16 = [(-20, -20), (20, -20), (20, 20), (-20, 20), (-20, -20)]

pen_fun(t_16, line_16)    
