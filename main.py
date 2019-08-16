from graphics import *
from math import pi
from math import cos
from math import sin

WIN_WIDTH = 500
WIN_HEIGHT = 500

TRUNK_X = WIN_WIDTH/2
TRUNK_Y = WIN_HEIGHT

INIT_LENGTH = 125;
INIT_THICKNESS= 10;
MID_BRANCH_LENGTH_MULTIPLIER = 1/4
LEFT_BRANCH_LENGTH_MULTIPLIER = 1/2
RIGHT_BRANCH_LENGTH_MULTIPLIER = 2/5
LENGTH_MULTIPLIER = 2/3
THICKNESS_MULTIPLIER  = 2/3

INIT_ROT_ADDITION = 0
INIT_TRUNK_ANGLE = pi/2
INIT_MID_BRANCH_ANGLE = pi/14
INIT_LEFT_BRANCH_ANGLE = pi/4
INIT_RIGHT_BRANCH_ANGLE = pi/6

win = GraphWin("Fractal Tree", WIN_WIDTH, WIN_HEIGHT)

def main():
    quit = False
    while not quit:
        n = int(input("Input size of tree (0, 1, 2, 3...): "))
        draw_tree(TRUNK_X, TRUNK_Y, INIT_LENGTH, INIT_THICKNESS, INIT_ROT_ADDITION, n, 0)
        if input("Continue? (y/n) ") != "y":
            quit = True
        if not quit:
            clear()

def draw_tree(x, y, line_length, line_thickness, additional_rot, n, num_rec_calls):

    base_x = x + line_length*cos(INIT_TRUNK_ANGLE+ additional_rot)
    base_y = y - line_length*sin(INIT_TRUNK_ANGLE + additional_rot)

    point1 = Point(x, y)
    point2 = Point(base_x, base_y)
    line1 = Line(point1, point2)
    line1.setWidth(line_thickness)
    line1.draw(win)

    point3 = Point(base_x - line_length * MID_BRANCH_LENGTH_MULTIPLIER * sin(INIT_MID_BRANCH_ANGLE + additional_rot), 
                   base_y - line_length * MID_BRANCH_LENGTH_MULTIPLIER * cos(INIT_MID_BRANCH_ANGLE + additional_rot))
    line2 = Line(point2, point3)
    line2.setWidth(2*line_thickness/3)
    line2.draw(win)

    point4 = Point(base_x - line_length * LEFT_BRANCH_LENGTH_MULTIPLIER * sin(INIT_LEFT_BRANCH_ANGLE + additional_rot), 
                   base_y - line_length * LEFT_BRANCH_LENGTH_MULTIPLIER * cos(INIT_LEFT_BRANCH_ANGLE+ additional_rot))
    line3 = Line(point2, point4)
    line3.setWidth(2*line_thickness/3)
    line3.draw(win)

    point5 = Point(base_x + line_length * RIGHT_BRANCH_LENGTH_MULTIPLIER * sin(INIT_RIGHT_BRANCH_ANGLE - additional_rot), 
                   base_y - line_length * RIGHT_BRANCH_LENGTH_MULTIPLIER * cos(INIT_RIGHT_BRANCH_ANGLE - additional_rot))
    line4 = Line(point2, point5)
    line4.setWidth(2*line_thickness/3)
    line4.draw(win)

    if num_rec_calls == n:
        return

    draw_tree(point2.x, point2.y, 
              line_length * LENGTH_MULTIPLIER, line_thickness * THICKNESS_MULTIPLIER, 
              INIT_MID_BRANCH_ANGLE  + additional_rot, 
              n, 
              num_rec_calls + 1)
    draw_tree(point2.x, point2.y, 
              line_length * LENGTH_MULTIPLIER, line_thickness * THICKNESS_MULTIPLIER, 
              INIT_LEFT_BRANCH_ANGLE + additional_rot, 
              n, 
              num_rec_calls + 1)
    draw_tree(point2.x, point2.y, 
              line_length * LENGTH_MULTIPLIER, line_thickness * THICKNESS_MULTIPLIER, 
              -INIT_RIGHT_BRANCH_ANGLE + additional_rot, 
              n, 
              num_rec_calls + 1)

def clear(win):
    for item in win.items[:]:
        item.undraw()

main()
