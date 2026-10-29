def solution(A, K):
  """Return a copy of the array A rotated to the right K times.

  Args:
    A (list[int]): The list of integers to rotate.
    K (int): The number of times to rotate the list right.

  Returns:
    list[int]: A new list containing the rotated elements.
  """
  n = len (A)
  
  # An empty list has nothing to rotate
  if n == 0:
    return A
    
  # Rotating a list of length n by n steps returns the original list.
  # Only the remainder of K divided by n actually matters.
  k = K % n
  
  # Take the last k elements and put them in front of the rest.
  return A[-k:] + A[:-k]
