#include <stdio.h>
#include <vector>
int main(void){
    int cnt, a, b, i;
    std::vector<int> arr;
    scanf("%d", &cnt);
    for(i=0; i<cnt; i++){
        scanf("%d %d", &a, &b);
        arr.push_back(a+b);
    }
    for(i=0; i<cnt; i++){
        printf("%d\n", arr[i]);
    }
}