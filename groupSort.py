arr = [13,1,6,5,15,142,9,1,5,11,1,4,13,11,5,12,17,1,17,14,7]

#selection sort 

def sortValue(arr): 
    for i in range(len(arr)): 
        freq = arr[i][1]
        min_index = i
        j = i + 1
        while j < len(arr) and arr[j][1] == freq: 
            if arr[min_index][0] > arr[j][0]: 
                min_index = j 
            j += 1
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        
def sortFrequency(arr): 
    for i in range(len(arr)): 
        maximum_index = i
        for j in range(i + 1, len(arr)): 
            if arr[maximum_index][1] < arr[j][1]: 
                maximum_index = j 
    
        arr[i], arr[maximum_index] = arr[maximum_index], arr[i]
def groupSort(arr):
    freq_arr = []
    unique_value = [] 
    
    for i in range(len(arr)): 
        if arr[i] not in unique_value: 
            unique_value.append(arr[i])
            count = 1
            for j in range(i + 1, len(arr)): 
                if arr[i] == arr[j]:
                    count += 1
            freq_arr.append([arr[i], count])
    print(freq_arr)
    sortFrequency(freq_arr)
    sortValue(freq_arr)
    
    return freq_arr
    
print(groupSort(arr))