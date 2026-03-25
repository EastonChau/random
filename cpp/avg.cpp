#include <iostream>
using namespace std;

int main(){
    double inum; //input number
    double sum = 1; //set for while loop
    int n = -1; //set for while loop
    while (inum != -1){
        cin >> inum;
        sum += inum;
        n += 1;
    }

    double avg = sum/n;
    cout << avg;
}
        

