def answer(data, n):
  occurrence_map = {}
  for task_id in data:
    if task_id in occurrence_map:
      occurrence_map[task_id] += 1
    else:
      occurrence_map[task_id] = 1
  # because the list takes less than 100 ints
  # space complexity is not a very big issue
  # we could have also just done data.delete()
  new_data = []
  for task_id in data:
    if occurrence_map[task_id] <= n:
      new_data.append(task_id)
  return new_data

def main():
  data = [5, 10, 15, 10, 7]
  n = 1
  data = answer(data, n)
  print(data)

if __name__ == '__main__':
  main()
