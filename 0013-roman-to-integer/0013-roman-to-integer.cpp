class Solution {
public:
int val(char c){
    if(c == 'I') return 1;
    if(c == 'V') return 5;
    if(c == 'X') return 10;
    if(c == 'L') return 50;
    if(c == 'C') return 100;
    if(c == 'D') return 500;
    if(c == 'M') return 1000;
   return 0; 
}
    int romanToInt(string s) {
        int ans=0;
        for(int i=0; i<s.length(); i++){
            int curr= val(s[i]);
            if(i+1 < s.length() && curr < val(s[i+1]) ){
                ans -= curr;
            }
            else{
                ans += curr;
            }
        }
        return ans;
        
    }
};