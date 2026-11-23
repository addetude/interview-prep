class Solution {
    public boolean isPalindrome(int intx) {
        String x = intx+"";
        int length = x.length();
        String arr [] = x.split("");
        
        int a = 0;
        int b = length-1;
        while(a<b){
            if(!arr[a].equals(arr[b])){
                return false;
            }else{
                a++;
                b--;
            }
        }
        return true;

    }
}