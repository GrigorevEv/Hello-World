truck_weight = int(input())
platform_height = int(input())
piano_weight = int(input())
piano_height = int(input())
fridge_weight = int(input())
fridge_height = int(input())
max_weight_on_the_bridge = int(input())
max_height_on_the_tunnel = int(input())

if truck_weight + piano_weight + fridge_weight > max_weight_on_the_bridge :
    if platform_height + fridge_height > max_height_on_the_tunnel or platform_height + piano_height > max_height_on_the_tunnel:
        print('NO')
    else:
        if truck_weight + piano_weight > max_weight_on_the_bridge :
            print('NO')
        else:
            print('YES')
else:
    if platform_height + fridge_height > max_height_on_the_tunnel:
        print('NO')
    else:
        print('YES')
