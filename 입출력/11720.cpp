#include <stdio.h>
int main(){
    int a, sum=0;
    scanf("%d\n");
    while((a = getchar()) != '\n'){
        sum += a - '0';
    }
    printf("%d", sum);
}