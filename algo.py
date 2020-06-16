def max(values):

  _max = values[0]

  for val in values:
      if val > _max:
          _max = val

  return _max


def min(values):

  _min = values[0]

  for val in values:
      if val < _min:
          _min = val

  return _min

def fib(n):
  old, new = 0, 1
  for _ in range(n):
      old, new = new, old + new
  return old
