#include <stdio.h>
int main(){
    int num, space, star, i, j;
    scanf("%d", &num);
    for(i=1; i<=num; ++i){
        space = num - i;
        star = 2 * i - 1;
        for(j=0; j<space; ++j) printf(" ");
        for(j=0; j<star; ++j) printf("*");
        printf("\n");
    }
}