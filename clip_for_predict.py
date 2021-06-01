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
