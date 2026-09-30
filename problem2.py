def funct_applied_to_list(list, funct):
  """
    ### don't forget the docstring which doesn't count in line count
    funct_applied_to_list([1,2,3,4,6],### you add this)
  """
  return [funct(x) for x in list]
