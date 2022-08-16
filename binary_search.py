"""Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.

Your Task:  
You dont need to read input or print anything. Complete the function binarysearch() which takes arr[], N and K as input parameters and returns the index of K in the array. If K is not present in the array, return -1.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.


Constraints:

1 <= N <= 105
1 <= arr[i] <= 106
1 <= K <= 106
View B"""




class Solution:	
    index = 0
	def binarysearch(self, arr, n, k):
		# code here
		
        if(n>1):
            n1 = int(n/2)
            if(arr[n1]>k):
                self.binarysearch(arr[0:n1],n1,k)
            elif(arr[n1]<k): 
                self.index+=n1
                self.binarysearch(arr[n1:n],n-n1,k)
            elif(arr[n1]==k):
                self.index+=n1
        elif(arr[n-1]==k) :
            self.index
        else : 
            self.index = -1
        return self.index
      
      
      
      
""" if __name__ == "__main__":
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split(' ')))
    k = int(input())
    ob = Solution()
    print(ob.binarysearch(arr , n , k)) """
  
  
  
  
  
  
