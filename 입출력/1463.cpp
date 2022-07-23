#include <stdio.h>
#define SIZE 1000000
int main(void){
    int num;
    int d[SIZE+1];
    scanf("%d", &num);
    d[1] = 0;
    for(int i=2; i<=num; ++i){
        d[i] = d[i-1] + 1;
        if(i % 2 == 0){
            d[i] = d[i] > d[i/2]+1 ? d[i/2]+1 : d[i];
        }
        if(i % 3 == 0){
            d[i] = d[i] > d[i/3]+1 ? d[i/3]+1 : d[i];
        }
    }
    printf("%d", d[num]);
}