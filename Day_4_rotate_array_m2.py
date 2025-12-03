class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
    
        # Handle the case where d > size of array
        d %= n
    
        # Reverse the remaining n-d elements
        reverse(arr, d, n - 1)
    
        # Reverse the entire array
        reverse(arr, 0, n - 1)
    
    # Function to reverse a portion of the array
def reverse(arr, start, end):
     while start < end:
         arr[start], arr[end] = arr[end], arr[start]
         start += 1
         end -= 1
         
arr = [1, 2, 3, 4, 5]
d = 2
sol = Solution()
sol.rotateArr(arr,d)
print(arr)
    
    