#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    fill_cell()
    while wall_is_beneath() == 0:
        fill_cell()
        while wall_is_on_the_right() == 0:
            move_right()
            fill_cell()
        else:
            move_down()
            fill_cell()
        while wall_is_on_the_left() == 0:
            move_left()
            fill_cell()
        else:
            if wall_is_beneath():
                break
            else:
                move_down()
                fill_cell()
    else:
        while wall_is_on_the_right() == 0:
            move_right()
            fill_cell()
        while wall_is_on_the_left() == 0:
            move_left()



if __name__ == '__main__':
    run_tasks()
