def solution(X, A):
  """Return the earliest time the frog can cross the river.

  Args:
    X (int): The number of positions that must be covered (1 to X).
    A (list[int]): A[K] is the position where a leaf falls at time K.

  Returns:
    int: The earliest time all positions 1 to X are covered.
      or -1 if that never happens.
  """
  covered = set()

  for time, position in enumerate(A):
    # A set ignores duplicates, so it only grows for new positions.
    covered.add(position)

    # Once X distinct positions are covered, the frog can cross.
    if len(covered) == X:
      return time

  # The loop ended without covering every possible position.
  return -1
