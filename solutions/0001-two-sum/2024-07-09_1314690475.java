import java.util.Hashtable;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable <Integer, Integer> map = new Hashtable<>();
        for(int i = 0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                int[] array = new int[2];
                array[0] = map.get(nums[i]);
                array[1] = i;
                return array;
            }else{
                map.put(target-nums[i], i);
            }
        } 
        return null;
    }
}