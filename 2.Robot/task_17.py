#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while cell_is_filled()==0:
        move_up()
    else:
        move_right()
        if cell_is_filled()==0:
            move_left(2)

if __name__ == '__main__':
    run_tasks()
