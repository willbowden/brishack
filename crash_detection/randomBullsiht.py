import os
import random
from os.path import isfile, join


def get_non_accidents():
    fileNames = [f for f in os.listdir("./data/test/Non Accident/") if isfile(join("./data/test/Non Accident", f))]
    fileNames.append([f for f in os.listdir("./data/train/Non Accident/") if isfile(join("./data/train/Non Accident", f))])
    
    return fileNames

def get_accidents():
    fileNames = [f for f in os.listdir("./data/test/Accident/") if isfile(join("./data/test/Accident", f))]
    fileNames.append([f for f in os.listdir("./data/train/Accident/") if isfile(join("./data/train/Accident", f))])
    
    return fileNames

def 
