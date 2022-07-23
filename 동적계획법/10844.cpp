#include <stdio.h>
#define MOD 1000000000
int main(void){
    int arr[101][101] = {0}, num, i, j, sum=0;
    scanf("%d", &num);
    for(i=1; i<=9; ++i){
        arr[1][i] = 1;
    }
    for(i=2; i<=num; ++i){
        for(j=0; j<=9; ++j){
            if(j==0){
                arr[i][j] = arr[i-1][1];
            }
            else if(j==9){
                arr[i][j] = arr[i-1][8];
            }
            else{
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1];
            }
            arr[i][j] %= MOD;
        }
    }
    for(i=0; i<=9; ++i){
        sum = (sum + arr[num][i]) % MOD;
    }
    printf("%d", sum % MOD);
}