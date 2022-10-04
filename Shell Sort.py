number = []
for i in range(10):
    print("Input element ", i+1, end = ": ")
    inp = int(input())
    number.append(inp)
print("Elements: ", end = " ")
for k in range(10):
    print(number[k], end = " ")
   
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval = interval-1
        print("\nInterval ", interval+1, ": ", end = " ")
        for l in range(10):
            print(number[l], end = " ")
        
        
shellSort(number, 10)
print("\nSorted: ", end = " ")
for l in range(10):
    print(number[l], end = " ")

