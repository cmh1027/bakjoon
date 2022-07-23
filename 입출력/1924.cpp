#include <stdio.h>
#include <string>
int month[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
std::string yoil[] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
int main(){
    int m, d, i, day;
    scanf("%d %d", &m, &d);
    day = d - 1;
    if(m == 1){
        puts(yoil[day%7].c_str());
    }
    else{
        for(int i=1; i<m; i++){
            day += month[i];
        }
        puts(yoil[day%7].c_str());
    }
}