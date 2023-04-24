#include <iostream>
using namespace std;
int main() {


    // edit distance

    std::string s1 = "abc"; 
    std::string s2 = "ab";

    int m = s1.size();
    int n = s2.size();

    int dp[m+1][n+1];

    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }

    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    
    return 0;
}