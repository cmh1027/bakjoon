#include <stdio.h>
#define MAX 10000
int main(void){
    int cnt, max=-1, num, i;
    int input[MAX] = {0};
    int arr[MAX] = {0};
    scanf("%d", &cnt);
    for(i=0; i<cnt; ++i){
        scanf("%d", &num);
        if(num > max) max = num;
        input[i] = num;
    }
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    for(i=4; i<=max; ++i){
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1];
    }
    for(i=0; i<cnt; ++i){
        printf("%d\n", arr[input[i]]);
    }
}