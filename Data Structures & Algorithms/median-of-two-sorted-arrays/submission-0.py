class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
    
        sum = 0
        
        l, r = 0, 0
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                arr.append(nums1[l])
                l += 1
            else:
                arr.append(nums2[r])
                r += 1

        while l < len(nums1):
            arr.append(nums1[l])
            l += 1
            
        while r < len(nums2):
            arr.append(nums2[r])
            r += 1
        
        if len(arr) % 2 == 1:
            return arr[int((len(arr)-1)/2)]
        else:
            return (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1])/2