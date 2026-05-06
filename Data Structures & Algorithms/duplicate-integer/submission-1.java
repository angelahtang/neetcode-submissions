class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> count = new HashMap<>();

        for (int i:nums) {
            if (count.containsKey(i)) {
                return true;
            }
            count.put(i,1);
        }

        return false;
    }
}