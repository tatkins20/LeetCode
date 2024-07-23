class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> countMap = new HashMap<>();
        for (char c : magazine.toCharArray()){
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }
        for (char c : ransomNote.toCharArray()){
            if (!countMap.containsKey(c) || countMap.get(c) == 0){
                return false;
            }else{
                countMap.put(c, countMap.get(c) - 1);
            }
        }
       return true;
    }
}
