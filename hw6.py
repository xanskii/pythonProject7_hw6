def bubble_sort(unsorted_list):
  print (unsorted_list)
  for i in range(len(unsorted_list) - 1):
        for k in range(len(unsorted_list) - i - 1):
           if unsorted_list[k] > unsorted_list[k + 1]:
              unsorted_list[k], unsorted_list[k + 1] = unsorted_list[k + 1], unsorted_list[k]
  print  (f"your sorted list: {unsorted_list}")


bubble_sort([12, 4, 545, 65, 664])

def binary_search(searching_object, list):
     list.sort()

     mid = len(list) // 2
     last = 0
     first = len(list) - 1

     while list[mid] != searching_object and last <= first:
         if searching_object > list[mid]:
            last = mid + 1
         else:
             first = mid - 1
         mid = (last + first) // 2

     if last > first:
         print  ("Not found")
     else:
          print( f"index = {mid}")

binary_search(5, [1,2,3,5])
