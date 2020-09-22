# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:16:13 2020

@author: ryanchan
"""

import numpy as np 
from PIL import Image
import os


def meta_data(ds_path, path_folder_L):
    
    name_L = []
    labels_L = []

    for i in path_folder_L:
        path = os.path.join(ds_path, i)
        name = os.listdir(path)
        labels = [i]*len(name)
        name_L += name
        labels_L += labels 
        
    uni_class = list(np.unique(labels_L))
    
    return name_L, labels_L, uni_class

def img_process(ds_path, name, path, size, channel):
    
    data = []
  
    for i in range(len(name)):
        img_path = os.path.join(ds_path, path[i], name[i])
        try:
            image = Image.open(img_path)
            image = image.convert(channel)
            image = image.resize(size)
            image = np.array(image)
            data.append(image)
        except:
            print(img_path)
            print("Error loading image")
  
    data = np.array(data)
    return data

def dict_create(L):
    start = 0
    dict_raw = {}
    for i in L:
        dict_raw[i] = start
        start += 1    
    return dict_raw



def json2dict(js):
    mapper = {}
    start = 0
    for i in js:
        mapper[start] = i
        start+=1
    return mapper