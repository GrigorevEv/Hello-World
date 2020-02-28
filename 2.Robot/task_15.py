#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
        while wall_is_beneath()==0 and wall_is_on_the_right()==0:
            move_down()
            move_right()
    elif wall_is_above() and wall_is_on_the_right():
        while wall_is_beneath()==0 and wall_is_on_the_left()==0:
            move_down()
            move_left()
    elif wall_is_beneath() and wall_is_on_the_right():
        while wall_is_above()==0 and wall_is_on_the_left()==0:
            move_up()
            move_left()
    elif wall_is_beneath() and wall_is_on_the_left():
        while wall_is_above()==0 and wall_is_on_the_right()==0:
            move_up()
            move_right()


if __name__ == '__main__':
    run_tasks()
