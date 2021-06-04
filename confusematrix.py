# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   confusematrix.py
@Time    :   2021/06/04 16:36:30
@Author  :   Nan Wang
@Version :   1.0
@Contact :   nanwang.ac@gmail.com
@License :   (C)Copyright 2021
"""

import matplotlib.pyplot as plt
import numpy as np
import itertools

def confuse_matirx():
    x = np.array([[96.89, 0,0,0,0,0,0,3.11,0,0],
                  [0.52,96.39,1.55,0,0,0.52,0.52,0.52,0,0],
                  [0,4.06,92.39,1.52,0,0,0,0.51,1.52,0],
                  [0,0,6.63,85.71,5.10,0,2.04,0,0.51,0],
                  [0,0,0,9.23,90.26,0,0.51,0,0,0],
                  [0,0,0,0,0,95.88,3.61,0.51,0,0],
                  [0.51,0,0,0,0,0,99.50,0,0,0],
                  [7.11,0.51,0,0,0,0,0.51,90.86,0.51,0.51],
                  [6.15,0,1.54,1.03,1.03,0,1.03,0.51,86.15,2.56],
                  [0,0,0,0,0,0,1.52,1.02,0,97.46]])
                  
    x_ntu = np.array([[100.00, 0,0,0,0,0,0,0,0,0],
                [0,100.00,0,0,0,0,0,0,0,0],
                [0,0,100.00,0,0,0,0,0,0,0],
                [0,0,0,100.00,0,0,0,0,0,0],
                [0,0,0,0,100.00,0,0,0,0,0],
                [0,0,0,0,0,100.00,0,0,0,0],
                [0,5.00,0,5.00,0,0,90.00,0,0,0],
                [0,0,0,0,0,0,0,100.00,0,0],
                [0,0,0,0,0,0,0,0,95.00,5.00],
                [0,0,0,0,0,0,0,0,0,100.00]])

    x_bd = np.array([[100.00, 0,0,0,0,0,0,0,0,0],
                [0,100.00,0,0,0,0,0,0,0,0],
                [0,0,95.29,0,0,7.41,0,0,0,0],
                [0,0,0,100.00,0,0,0,0,0,0],
                [0,0,15.63,0,65.63,15.63,0,0,0,0],
                [0,0,13.33,0,23.33,63.33,0,0,0,0],
                [0,5.00,0,5.00,0,0,100.00,0,0,0],
                [0,0,5.26,2.63,2.63,7.89,0,81.58,0,0],
                [0,0,0,0,0,0,0,0,100.00,0],
                [0,0,0,0,0,0,0,0,0,100.00]])

    cmap = plt.cm.binary
    plt.figure(figsize=(12,10), dpi= 600)
    plt.imshow(x_ntu,cmap=cmap)
    plt.colorbar()
    cls = ['one','two', 'three', 'four', 'five', 'six', 'fist', 'like', 'okay', 'plam']
    ntu_cls = ['zero', 'one','two', 'three', 'four', 'five', 'six', 'eight', 'nine', 'seven']
    bd_cls = ['fist', 'pinch','flip','telephone', 'r-swipe','l-swipe','td-swipe','dt-swipe','thumb','index']
    tick_marks = np.arange(len(ntu_cls))
    plt.xticks(tick_marks, ntu_cls)
    plt.yticks(tick_marks, ntu_cls)
    for i, j in itertools.product(range(x_ntu.shape[0]), range(x_ntu.shape[1])):
        plt.text(j,i, x_ntu[i,j], horizontalalignment='center', color='r')
    plt.grid(False)
    plt.savefig(r'D:cmntu.jpg')

confuse_matirx()

