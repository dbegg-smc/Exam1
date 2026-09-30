def is_sorted(list):
  """
  ### add to the docstring including additional doctests

  >>> is_sorted([1,3,5.6,7])
  True
  >>> is_sorted([7,5.6,3,1])
  True
  >>> is_sorted([1])
  ### what should the answer be?
  """
  increasing = all(list[i] <= list[i+1] for i in range(len(list)-1))
  decreasing = all(list[i] >= list[i-1] for i in range(len(list)-1))
  return increasing or decreasing
