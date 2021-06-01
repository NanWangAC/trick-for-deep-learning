# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   clip_for_predict.py
@Time    :   2021/06/01 14:43:22
@Author  :   Nan Wang
@Version :   1.0
@Contact :   nanwang.ac@gmail.com
@License :   (C)Copyright 2021
"""
import numpy as np

"""
clipping explain:
If you predict something to be true when it turns out to be false, your error score increases infinitely.  
If we can keep the probability between 0.05 and 0.95(or other feasible value), 
then we can never be quite sure about the prediction.  
In this case, we do not see a large increase in error functions.  
"""
# predict
y_pred = model.predict(data)

# bound for predict clipping make performance better
lower_bound, upper_bound = 0.025, 0.975
y_pred_clip = np.clip(y_pred, lower_bound, upper_bound)
