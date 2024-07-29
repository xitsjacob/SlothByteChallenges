def advanced_sort(unsorted_list) -> None:
  sorted_list = []
  for num in unsorted_list:

    found = False
    for sublist in sorted_list:

      if num == sublist[0]:
        sublist.append(num)
        found = True
        break
    if not found:
      sorted_list.append([num])
      
  return sorted_list
    

if __name__ == "__main__":
  tests = [
    [2, 1, 3, 5, 3, 2],
    [5, 5, 5, 5, 1, 2, 3, 3],
    ['a', 'b', 'c', 'c', 'b'],
    ['a', 'b', 'c', 'a', 'b'],
    [2, 'a', 3, 'b', 2, 'a', 'b', 3],
    ['a', 2, 'b', 2, 'c', 'b', 'a', 2]
  ]
  for test in tests:
    result = advanced_sort(test)
    print(result)
