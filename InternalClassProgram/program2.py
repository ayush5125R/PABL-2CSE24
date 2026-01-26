'''You are given an array of integers arr[]. You have to reverse the given array. 
Note: Modify the array in place. 
Examples: 
 Input: arr = [1, 4, 3, 2, 6, 5] 
Output: [5, 6, 2, 3, 4, 1] 
Explanation: The elements of the array are [1, 4, 3, 2, 6, 5]. After reversing the 
array, the first element goes to the last position, the second element goes to the 
second last position and so on. Hence, the answer is [5, 6, 2, 3, 4, 1].'''

def reverseArray(arr):
        left, right =0,len(arr)-1
        while left<right:
         arr[left] ,arr[right] = arr[right] ,arr[left]
         left +=1
         right-=1


#for example
arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)

'''def reverseArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)'''


            