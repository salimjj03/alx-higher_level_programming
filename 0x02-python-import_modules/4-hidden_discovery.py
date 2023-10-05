#!/usr/bin/python3
import hidden_4
name = dir(hidden_4)
if __name__ == "__main__":
    for i in range(len(name)):
        if name[i][1] == '_':
            pass
        else:
            print(name[i])
