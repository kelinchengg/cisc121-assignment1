def solution(A):
  """Return the value in A that does not have a matching pair.

  Args:
    A (list(int)): A non-empty list with an odd number of elements, 
      where every value except one appears an even number of times.

  Returns:
    int: The unpaired value.
  """
  unpaired = set()

  # unpaired holds the values seen an odd number of times so far.
  # Seeing a value again pairs it off, so it is removed.
  for value in A:
    if value in unpaired:
      unpaired.remove(value)
    else:
      unpaired.add(value)

  # Every pair has cancelled out, leaving only the unpaired value.
  return unpaired.pop()
