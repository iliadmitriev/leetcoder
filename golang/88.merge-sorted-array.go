/*

1. inverse problem:
instead of trying to build smaller to greater from the beggining of array
try to build greater to smaller from the end of the array 

k = insert point starging from end of the result moving to the beggining
i = read point from ten end of nums1
j = read point from the end of nums2
             i     k
nums1 = [1,2,3,0,0,0]
             j
nums2 = [2,5,6]

*/
func merge(nums1 []int, m int, nums2 []int, n int) {
  k := n + m - 1 
	i, j := m - 1, n -1

	for i >= 0 && j >= 0 {
		if nums1[i] >= nums2[j] {
			nums1[k] = nums1[i]
      i--
		} else {
      nums1[k] = nums2[j]
      j--
    }
    k--
	}

  for j >= 0 {
    nums1[k] = nums2[j]
    j--
    k--
  }
}