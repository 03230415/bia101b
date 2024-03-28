input_arr = [6, 3, 1, 5, 0]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print('inside first forloop')
        print()
        for k in range(0, n - 1): 
            print("inside second forloop")
            print()         #forloop inside forloop
            element = arr[k]
            elementright = arr[k+1]
            print("elementright: ",elementright)
            print("element: ",element)
            print("=====================")
            # swap
            if element > elementright:
                arr[k] = elementright
                arr[k+1] = element
                print("swapped", arr)
                print("======================")
    print("final", arr)
bubble_sort(input_arr)
    