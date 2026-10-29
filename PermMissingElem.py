def solution(A):
  """Return the missing number from a list of 1 to N + 1.

  Args:
    A (list[int]): A list of N distinct integers from 1 to N + 1,
      with exactly one value missing.

  Returns:
    int: The missing value.
  """
  n = len(A)

  # The numbers 1 to N + 1 add up to (N + 1) * (N + 2) / 2
  # Floor division keeps the result as an int.
  expected_sum = (n + 1) * (n + 2) // 2

  # Whatever is left after subtracting the actual sum is the missing value.
  return expected_sum - sum(A)
  
