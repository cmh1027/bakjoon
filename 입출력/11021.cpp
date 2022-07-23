#include <stdio.h>
int main(void){
    int a, b, cnt=1;
    scanf("%d", &a);
    while(scanf("%d %d", &a, &b) != EOF){
        printf("Case #%d: %d\n", cnt++, a+b);
    } 
}