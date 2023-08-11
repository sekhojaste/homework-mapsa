 ### arraye haye tekrary bishtar az 2 bar

def tekraryarraye(arr, tool):

   # tool====> tedede ararye
   cheked_arraye = [False for i in range(tool)]
    ### 
   for i in range(tool):

     if (cheked_arraye[i] == True):
        continue
     tekraryarraye = 1
     for j in range(i + 1, tool,1 ):
        if (arr[i] == arr[j]):
          cheked_arraye[j] = True
          tekraryarraye += 1
     if tekraryarraye != 1 :
        print(arr[i])


arr = [8, 0, 3, 11,"b", 11, 1, "b", 4, "b"]
tool = len(arr)
tekraryarraye(arr, tool)