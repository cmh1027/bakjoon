#include <stdio.h>
int main(){
    int num, i, j;
    scanf("%d", &num);
    for(i=1; i<=num; i++){
        for(j=1; j<i; j++) putchar(' ');
        for(j=1; j<=num-i; j++) putchar('*');
        putchar('*');
        for(j=1; j<=num-i; j++) putchar('*');
        putchar('\n');
    }
    for(i=num-1; i>=1; i--){
        for(j=1; j<i; j++) putchar(' ');
        for(j=1; j<=num-i; j++) putchar('*');
        putchar('*');
        for(j=1; j<=num-i; j++) putchar('*');
        putchar('\n');
    }
}