def palindrome(string):
  """
  Returns True or False if the given string is a palindrome

  Args:
      string (str): the string to check
  """
  normalize_string = "".join(ch.lower() for ch in string if ch.isalnum())
  return normalize_string == normalize_string[::-1]
