#include <iostream>
#include <string>
using namespace std;
bool flag = false;
void update(int input, int& min, int& max){
    if(!flag){
        min = input;
        max = input;
        flag = !flag;
    }
    if(min >= input) min = input;
    if(max <= input) max = input;
}
int main(){
    int num, pos=0, space, min, max;
    string str;
    getline(cin, str);
    getline(cin, str);
    while((space = str.find(' ', pos)) != string::npos){
        num = atoi(str.substr(pos, space-pos).c_str());
        update(num, min, max);
        pos = space + 1;
    }
    update(atoi(str.substr(pos, str.size()-pos).c_str()), min, max);
    cout << min << " " << max << endl;
}