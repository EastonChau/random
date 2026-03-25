#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double weight;
    double height;
    cin >> weight >> height;
    double base = height;
    int exponent = 2;

    double bmi = weight/(pow(base,exponent));
    cout << "Your BMI = " << bmi << endl;
    cout << "BMI VALUES"<< endl;
    cout << "Underweight: less than 18.5"<< endl;
    cout << "Normal: between 18.5 and 24.9"<< endl;
    cout << "Overweight: between 25 and 29.9"<< endl;
    cout << "Obese: 30 or greater"<< endl;

}
        

