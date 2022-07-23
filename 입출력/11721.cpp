#include <stdio.h>
int main(){
    char str[100] = {0, };
    int index = 0;
    scanf("%s", str);
    while(str[index] != '\0'){
        putchar(str[index++]);
        if(index != 0 && index % 10 == 0)
            putchar('\n');
    }
}