def ternary_search(first,last,key,arr):
    while(last>first):
        mid1=first+(last-first)//3
        mid2=last-(last-first)//3

        #check if the key to be found is equal to any of the mids
        if(key==arr[mid1]):
            return mid1
        if(key==arr[mid2]):
            return mid2
        #if they key matches neither of the two mids
        #then check for its region

        if(key<arr[mid1]):
            last=mid1-1          #region is between 0 to mid1
        elif(key>arr[mid2]):
            first=mid2+1
        else:
            first=mid1+1
            last=mid2-1
    print("key not found")                   #that means key notfound
arr=[4,2,78,34,45,12,9]
arr.sort()
first=0
last=len(arr)-1
key=22
found=ternary_search(first,last,key,arr)
print("Index of",key,"found in array is",found)