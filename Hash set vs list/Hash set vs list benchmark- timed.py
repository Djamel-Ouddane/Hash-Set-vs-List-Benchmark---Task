import time

# Defines a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
  
    # Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    
    test_item = 10**6 + 1  # This item is not in our set or list
    start_time = time.time()
    # Time the 100 consecutive operations of checking whether `test_item` is in `data_set` and print the result and time taken
    set_result = [test_item in data_set for _ in range(100)]
    # Time the 100 consecutive operations of checking whether `test_item` is in `data_list` and print the result and time taken
    #Elapsed time for set
    set_time = time.time() - start_time
    start_time = time.time()
    list_result = [test_item in data_list for _ in range(100)]
    # Elapsed time for list
    list_time = time.time() - start_time
    print(f"Set result:",set_result, "Time taken:", set_time)
    print(f"List result:",list_result, "Time taken:", list_time)
compare_operations()
