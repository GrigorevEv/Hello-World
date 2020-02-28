#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while wall_is_above() or wall_is_beneath():
        if wall_is_above()==0:
            fill_cell()
        move_right()
        if wall_is_on_the_right() and wall_is_above()==0:
            fill_cell()
            break
        elif wall_is_on_the_right():
            break


if __name__ == '__main__':
    run_tasks()
