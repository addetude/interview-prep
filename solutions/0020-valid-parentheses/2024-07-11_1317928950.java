import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack <Character> st = new Stack<Character>();
        int length = s.length();
        for(int i = 0; i < length; i++){
            char a = s.charAt(i);
            if(a == '(' || a == '[' || a == '{'){
                st.push(a);
            }else{
                if(st.empty() == true){
                    return false;
                }else if(st.peek() == '(' && a == ')' || st.peek() == '[' && a == ']' || st.peek() == '{' && a == '}'){
                    st.pop();
                }else{
                    return false;
                }
            }
        }
        return st.empty();
    }
}