#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while wall_is_on_the_right()==0:
        if wall_is_above()==0 and wall_is_beneath():
            fill_cell()
        move_right()
    else:
        if wall_is_above()==0 and wall_is_beneath():
            fill_cell()

if __name__ == '__main__':
    run_tasks()
