#include <stdio.h>
#include <vector>
int main(void){
    int a, b, i;
    std::vector<int> arr;
    while(scanf("%d %d", &a, &b) != EOF){
        printf("%d\n", a+b);
    } 
}