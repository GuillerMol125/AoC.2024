import numpy as np

def read_txt(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]

def read_txt_np_int(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [np.array(line.strip().split()).astype(int) for line in lines]