def quicksort(arr = []):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            tmp = arr[0]
            arr[0] = arr[1]
            arr[1] = tmp
        return arr
    if len(arr) > 2:
        al = []
        ar = []
        base_index = len(arr) // 2
        base = arr.pop(base_index)
        for item in arr:
            if item <= base:
                al.append(item)
            else:
                ar.append(item)
        return quicksort(al) + [base] + quicksort(ar)