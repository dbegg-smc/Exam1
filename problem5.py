import numpy as np

def estimate_pi(n):
  """
  positive number -> positive number 
  n = number of randomly generated points
  estimate_pi estimates the value of pi using n randomly generated points, 
  a larger n yields, on average, a better approximation of pi.
  """
  points = np.random.uniform(0, 2, size=(n, 2))
  inside = np.sum((points[:, 0] - 1) ** 2 + (points[:, 1] - 1) ** 2 <= 1)
  return 4 * inside / n
