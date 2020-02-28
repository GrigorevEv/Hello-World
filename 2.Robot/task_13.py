#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while wall_is_on_the_right()==0:

        if wall_is_above()==0 and wall_is_beneath()==0:
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()

        elif wall_is_beneath()==0:
            move_down()
            fill_cell()
            move_up()
        elif wall_is_above()==0:
            move_up()
            fill_cell()
            move_down()
        move_right()

    else:
        if wall_is_above()==0 and wall_is_beneath()==0:
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()

        elif wall_is_beneath()==0:
            move_down()
            fill_cell()
            move_up()
        elif wall_is_above()==0:
            move_up()
            fill_cell()
            move_down()




if __name__ == '__main__':
    run_tasks()
