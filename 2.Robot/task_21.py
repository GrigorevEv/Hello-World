#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    k=1
    for i in range(7):
        move_down()
        for p in range(k):
            move_right()
            fill_cell()
        move_right()
        move_down()
        for t in range(k):
            if k==13:
                move_left()
            else:
                fill_cell()
                move_left()
                fill_cell()
        move_left()
        k+=2
    move_right()




if __name__ == '__main__':
    run_tasks()
