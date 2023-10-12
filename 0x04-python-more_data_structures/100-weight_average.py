#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mul = 0
        sum = 0
        for i in my_list:
            mul = mul + i[0] * i[1]
            sum = sum + i[1]
        return (mul / sum)
    else:
        return (0)
