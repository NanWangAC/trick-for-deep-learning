import numpy as np

# predict
y_pred = model.predict(data)

# bound for predict clipping
lower_bound, upper_bound = 0.025, 0.975
y_pred_clip = np.clip(y_pred, lower_bound, upper_bound)
