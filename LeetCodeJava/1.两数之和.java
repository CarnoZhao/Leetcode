import java.util.Hashtable;

/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ret = new int[2];
        int num;
        Hashtable<Integer, Integer> dic = new Hashtable<Integer, Integer>();
        for (int i = 0; i < nums.length; i ++) {
            num = nums[i];
            if (dic.containsKey(num)) {
                ret[0] = dic.get(num);
                ret[1] = i;
                break;
            } else {
                dic.put(target - num, i);
            }
        }
        return ret;
    }
}

