#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() == 0:
        move_down()
    else:
        while wall_is_beneath():
            move_right()
        else:
            move_down()
            move_left()
    while wall_is_above():
        move_left()
        if wall_is_on_the_left():
            break


if __name__ == '__main__':
    run_tasks()
