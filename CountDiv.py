def solution(A, B, K):
  """Return how many integers from A to B (inclusive) are divisible by K.

  Args:
    A (int): The start of the range.
    B (int): The end of the range (A <= B).
    K (int): The divisor.

  Returns:
    int: the number of integers in [A, B] divisible by K.
  """
  # B // K counts multiples of K up to B; A // K counts those up to A.
  # Subtracting leaves the multiples in the range above A, until B.
  count = B // K - A // K

  # A itself was excluded above, so add it back if it is a multiple of K.
  if A % K == 0:
    count += 1

  return count
