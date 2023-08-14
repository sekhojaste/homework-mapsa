

array1 = [1,2,3,4]
array2 = [1,44,22,33,44,3,4]
if len(array2) > len (array1):
    result = set(array2) - set(array1)
else :
    result = set(array1) - set(array2)  ### vaghti len(array1)>len(array2) ==> dos not work 
print(sorted(result))
