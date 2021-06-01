# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   flood.py
@Time    :   2021/06/01 17:55:41
@Author  :   Nan Wang
@Version :   1.0
@Contact :   nanwang.ac@gmail.com
@License :   (C)Copyright 2021
"""

# flood can effectively avoid overfitting with a smallest boundary( param b) for loss
import torch

criterion = torch.nn.CrossEntropyLoss()
predict = model(data)
loss = criterion(predict, label)
loss_flood = (loss - b).abs() + b
loss_flood.backward()