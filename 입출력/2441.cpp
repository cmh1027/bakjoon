#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i=1; i<=num; i++){
        for(int j=1; j<i; j++) 
            putchar(' ');
        for(int k=1; k<=num-i+1; k++) 
            putchar('*');
        putchar('\n');
    }
}