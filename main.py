##
## EPITECH PROJECT, 2023
## B-CNA-500-BAR-5-1-neuralnetwork-thomas.laprie
## File description:
## main.py
##


import sys

def usage():
    print("USAGE\n"
"   ./my_torch [--new IN_LAYER [HIDDEN_LAYERS...] OUT_LAYER | --load LOADFILE]\n"
"  [--train | --predict] [--save SAVEFILE] FILE\n"
"DESCRIPTION\n"
"   --new Creates a new neural network with random weights.\n"
"Each subsequent number represent the number of neurons on each layer, from left\n"
"to right. For example, ./my_torch –new 3 4 5 will create a neural network with\n"
"an input layer of 3 neurons, a hidden layer of 4 neurons and an output layer of 5\n"
"neurons.\n"
"   --load Loads an existing neural network from LOADFILE.\n"
"   --train Launches the neural network in training mode. Each board in FILE\n"
"must contain inputs to send to the neural network, as well as the expected output.\n"
"   --predict Launches the neural network in predictin mode. Each board in FILE\n"
"must contain inputs to send to the neural network, and optionally an expected\n"
"output.\n"
"   --save Save neural network internal state into SAVEFILE.\n"
"   FILE FILE containing chessboards")


def check_save(args):
    if (args[0] == "--save" and len(args) == 3):
        print("save")
        exit(0)
    elif (len(args) == 1):
        print("no save")
        exit(0)
    else:
        print("error")
        exit(84)


def trainOrPredict(args):
    match args[0]:
        case "--train":
            print("train")
        case "--predict":
            print("predict")
        case _:
            print("error")
            exit(84)
    check_save(args[1:])

def main(args):
    match args[1]:
        case "--help":
            usage()
            exit(0)
        case "--new":
            print("new")
            trainOrPredict(args[5:])
        case "--load":
            print("load")
            trainOrPredict(args[3:])
        case _:
            print("error")
            exit(84)


if __name__ == "__main__":
    main(sys.argv)
