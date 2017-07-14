def answer(data, t):
  if not data:
    return [-1, 1]
  sum = data[0]
  i, j = 0, 0
  while j < len(data)-1:
    if sum == t:
      return [i, j]
    elif sum < t:
      j += 1
      sum += data[j]
    else:
      if i == j:
        j += 1
      sum -= data[i]
      i += 1
  return [-1, -1]

def main():
  data = [4,3,5,7,8]
  target = 12
  print answer(data, target)

if __name__ == '__main__':
  main()
