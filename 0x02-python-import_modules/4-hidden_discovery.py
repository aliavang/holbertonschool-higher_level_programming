#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][0:2] == "__":
            continue
        else:
            print(dir(hidden_4)[i])
