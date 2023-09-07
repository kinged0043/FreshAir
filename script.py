# aim of this project is to write a script that automates download from pahe.li site
import os
from selenium import webdriver
parent = r'c:\Users\KingED\Downloads'

def make_dir(dir_name):
    path = os.path.join(parent, dir_name)
    os.mkdir(path=path, dir_fd=None)
