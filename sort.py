# arr = [12,3,45,7,32,1]
# li = []
# max = arr[0]
# li.append(max)
# i=1
# while i < len(arr):
#     if max < arr[i]:
#         max=arr[i]
#         li.append(max)
#     i +=1
# print(li)
arr = [12, 3, 45, 7, 32, 1]
li = []
max_val = arr[0]
li.append(max_val)  # Append the initial max

for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
        li.append(max_val)

print(li)




