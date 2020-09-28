#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_6_6():
    move_right()
    while wall_is_on_the_right() == 0:
        while wall_is_above() == 0:
            move_up()
            fill_cell()
        else:
            while wall_is_beneath() == 0:
                move_down()
        move_right()
    else:
        while wall_is_above() == 0:
            move_up()
            fill_cell()
        else:
            while wall_is_beneath() == 0:
                move_down()
        while wall_is_beneath():
            move_left()



if __name__ == '__main__':
    run_tasks()
