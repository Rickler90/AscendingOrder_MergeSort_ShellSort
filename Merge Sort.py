import random
numbers = []
count = 0
while count<20:
    num = random.randint(10,50)
    numbers.append(num)
    count+=1
print("Generated Random Numbers:",numbers)
dv=list(dict.fromkeys(numbers))
print("Distinct Values:",dv)
newList = dv[:4] + dv[-4:]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
 
        R = arr[mid:]
        print("Sublist: ", L, R)
        
        mergeSort(L)
 
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print("\nCompare, Swap and Combine: ",L,R)   
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
print("Elements to sort: ", end=" ")
printList(newList)
mergeSort(newList)
print("Sorted Elements: ", end=" ")
printList(newList)
