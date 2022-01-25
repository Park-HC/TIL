def is_red(squre_string):
    return True if squre_string[-1] == '1' else False

def string_to_coord(squre_string):
    coords = []
    numbers = list(map(int, squre_string.split(' ')))
    coords.append((numbers[0], numbers[1]))
    coords.append((numbers[2], numbers[3]))
    return coords

def cal_area(ord_l, ord_r):
    return abs(ord_r[0] - ord_l[0]) * abs(ord_l[1] - ord_r[1])

def cal_coverlap(red_squre, blue_squre):
    red_area = cal_area(*red_squre)
    blue_area = cal_area(*blue_squre)

    if blue_squre[0][0] <= red_squre[0][0] <= blue_squre[1][0]:
        if blue_squre[0][1] >= red_squre[0][1] >= blue_squre[1][1]:
            return min((red_area, blue_area, cal_area((red_squre[0][0],red_squre[0][1]), (blue_squre[1][0],blue_squre[1][1]))))
        elif blue_squre[0][1] >= red_squre[1][1] >= blue_squre[1][1]:
            return min((red_area, blue_area, cal_area((red_squre[0][0],red_squre[1][1]), (blue_squre[1][0],blue_squre[0][1]))))
        else:
            print('1')
            return 0
    elif blue_squre[0][0] <= red_squre[1][0] <= blue_squre[1][0]:
        if blue_squre[0][1] >= red_squre[0][1] >= blue_squre[1][1]:
            return min((red_area, blue_area, cal_area((red_squre[1][0],red_squre[0][1]), (blue_squre[0][0],blue_squre[1][1]))))
        elif blue_squre[0][1] >= red_squre[1][1] >= blue_squre[1][1]:
            return min((red_area, blue_area, cal_area((red_squre[1][0],red_squre[1][1]), (blue_squre[0][0],blue_squre[0][1]))))
        else:
            print('2')
            return 0
    else:
        print('3')
        return 0

def coverlap(num_squre, *squre_string):
    blue_squres = []
    red_squres = []
    area_overlap = 0

    for i in range(num_squre):
        if is_red(squre_string[i]):
            red_squres.append(string_to_coord(squre_string[i]))
        else:
            blue_squres.append(string_to_coord(squre_string[i]))

    for red_squre in red_squres:
        for blue_squre in blue_squres:
            area_overlap += cal_coverlap(red_squre, blue_squre)

    return area_overlap


print(coverlap(2, '2 2 4 4 1', '3 3 6 6 2'))
print(coverlap(3, '1 2 3 3 1', '3 6 6 8 1', '2 3 5 6 2'))
print(coverlap(3, '1 4 8 5 1', '1 8 3 9 1', '3 2 5 8 2'))