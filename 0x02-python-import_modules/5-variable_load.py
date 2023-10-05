#!/usr/bin/python3
import variable_load_5
var = dir(variable_load_5)
if __name__ == "__main__":
    for i in range(len(var)):
        if var[i] == 'a':
            print(variable_load_5.a)
