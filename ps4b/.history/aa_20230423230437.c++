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

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1;
            }
        }
    }
    
    return 0;
}