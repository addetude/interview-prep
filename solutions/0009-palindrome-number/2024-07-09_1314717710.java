class Solution {
    public boolean isPalindrome(int intx) {
        String x = intx+"";
        int length = x.length();
        String arr [] = new String[length];
        for(int i = 0; i < length; i++){
            arr[i] = x.substring(i,i+1);
        }
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