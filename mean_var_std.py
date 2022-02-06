import numpy as np
import sys

def calculate(list):
  if len(np.array(list))<9:
     raise ValueError("List must contain nine numbers.")
     sys.exit(1)
  Y = np.array(list).reshape(3,3)

  mean_axis1 = Y.mean(axis=0)
  mean_axis2 = Y.mean(axis=1)
  mean_flattened = Y.mean()

  variance_axis1 = Y.var(axis=0)
  variance_axis2 = Y.var(axis=1)
  variance_flattened = Y.var()

  std_axis1 = Y.std(axis=0)
  std_axis2 = Y.std(axis=1)
  std_flattened = Y.std()

  max_axis1 = Y.max(axis=0)
  max_axis2 = Y.max(axis=1)
  max_flattened = Y.max()

  min_axis1 = Y.min(axis=0)
  min_axis2 = Y.min(axis=1)
  min_flattened = Y.min()

  sum_axis1 = Y.sum(axis=0)
  sum_axis2 = Y.sum(axis=1)
  sum_flattened = Y.sum()

  list_mean = [mean_axis1.tolist(), mean_axis2.tolist(), mean_flattened.tolist()]
  list_variance = [variance_axis1.tolist(), variance_axis2.tolist(), variance_flattened.tolist()]
  list_std = [std_axis1.tolist(), std_axis2.tolist(), std_flattened.tolist()]
  list_max = [max_axis1.tolist(), max_axis2.tolist(), max_flattened.tolist()]
  list_min = [min_axis1.tolist(), min_axis2.tolist(), min_flattened.tolist()]
  list_sum = [sum_axis1.tolist(), sum_axis2.tolist(), sum_flattened.tolist()]

  calculations = {'mean':list_mean,
         'variance':list_variance,
         'standard deviation': list_std,
         'max': list_max,
         'min': list_min,
         'sum': list_sum}

  return calculations