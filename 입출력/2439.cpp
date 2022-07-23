#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i=1; i<=num; i++){
        for(int j=1; j<=num-i; j++) 
            putchar(' ');
        for(int k=1; k<=i; k++) 
            putchar('*');
        putchar('\n');
    }
}