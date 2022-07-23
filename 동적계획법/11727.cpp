#include <stdio.h>
int main(void){
    int arr[1001], num;
    arr[1] = 1;
    arr[2] = 3;
    scanf("%d", &num);
    for(int i=3; i<=num; ++i){
        arr[i] = (2 * arr[i-2] + arr[i-1])%10007;
    }
    printf("%d", arr[num]);
}