#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int amount = 18;
    // 金币
    int coins[] = {1,5,10,20};
    // count = f(amount);
    int dp[20];
    // 初始化
    for(int i = 0; i < amount + 1; i++){
        dp[i] = amount + 1;
    }
    dp[0] = 0; 

    // 状态
    for(int i = 1; i <= amount;i++){
        // 选择
        for(int j=0; j < 4;j++){
            if(coins[j] <= i){
                dp[i] = min(dp[i],dp[i - coins[j]] + 1);
            }
        }

    }

    cout << "count: " << dp[amount] << endl;
}
