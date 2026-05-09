class Solution {
public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0, right = arr.length - k;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] >= x) {
                right = mid;
            } else if (arr[mid + k] <= x) {
                left = mid + 1;
            } else if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }                
        }     
        
        List<Integer> res = new ArrayList(k);
        for (int i = 0; i < k; i++) {
            res.add(arr[left + i]);
        }
        return res;
    }
}
