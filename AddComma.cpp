#include <iostream>
using namespace std;

int main(){
    int num;
    cin >> num;
    int digit[5];

    for (int i = 0; i <= 4; ++i) {
        digit[i] = num % 10;
        num /= 10;
    }
    
    //concat
    string ooooo = to_string(digit[4]);

    for (int i = 3; i>=0; --i){
        ooooo = ooooo + "," + to_string(digit[i]);
    }
    cout << ooooo;
    
}
        