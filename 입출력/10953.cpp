#include <stdio.h>
int main(void){
    int a, b;
    scanf("%d", &a);
    while(scanf("%d,%d", &a, &b) != EOF){
        if(a!=0 || b!=0)
            printf("%d\n", a+b);
    } 
}