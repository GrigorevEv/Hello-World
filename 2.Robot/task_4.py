#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_above() == 0:
        move_up()
    else:
        if wall_is_on_the_right() == 0:
            move_right()
        else:
            if wall_is_beneath() == 0:
                move_down()
            else:
                if wall_is_on_the_left() == 0:
                    move_left()



if __name__ == '__main__':
    run_tasks()
