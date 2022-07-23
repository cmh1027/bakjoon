#include <stdio.h>
int main(){
    int num, asterisk, space, i, j;
    scanf("%d", &num);
    for(i=1; i<=num; i++){
        asterisk = i;
        space = 2 * (num - i);
        for(j=0; j<asterisk; j++) putchar('*');
        for(j=0; j<space; j++) putchar(' ');
        for(j=0; j<asterisk; j++) putchar('*');
        putchar('\n');
    }
    for(int i=num-1; i>=1; i--){
        asterisk = i;
        space = 2 * (num - i);
        for(j=0; j<asterisk; j++) putchar('*');
        for(j=0; j<space; j++) putchar(' ');
        for(j=0; j<asterisk; j++) putchar('*');
        putchar('\n');
    }