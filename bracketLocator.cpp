#include <iostream>
using namespace std;
#include <vector> 
#include <algorithm> 


//brace1:();brace2:[];brace3{}

void error(){
    cout << "Error";
}

void checking(string str){
    cout << "checking :" << str << endl;
}

vector<int> blendVect(vector<int> V1, vector<int> V2, vector<int> V3){
    vector<int> blended;

    blended.insert(blended.begin(), V1.begin(), V1.end());
    blended.insert(blended.begin(), V2.begin(), V2.end());
    blended.insert(blended.begin(), V3.begin(), V3.end());
    int b_size = blended.size();
    /*
    vector<int> v1 = {0,1,2,4}; 
    vector<int> v2 = {3,5};
    vector<int> v3 = {6,7};
    */
    vector<int> oblended;
    for (int i = 0; oblended.size() < b_size; i++){
        for (int j = 0; j < blended.size(); j += 2){
            if (blended[j] == i){
                oblended.push_back(blended[j]);
                oblended.push_back(blended[j+1]);
                blended.erase(blended.begin() + j, blended.begin() + j + 2);
                /*
                cout << i << ","<< j<<endl;
                cout << "blended" << blended.size() << endl;
                cout << "output" << oblended.size() << endl;
                */
                break;
            } 
        }
    }
    
    return oblended;
}




void result(vector<int> postVect){
    int sizeVect = postVect.size();
    cout << "OK" <<endl;
    for (int i = 0; i < sizeVect; i += 2){
        if (i == sizeVect - 2){
            cout << "(" << postVect[i] << ", "<< postVect[i+1] << ")";
        } else {
            cout << "(" << postVect[i] << ", "<< postVect[i+1] << ") ";
        }
        
    }
}

bool count_bracket(char open, char close, string str){
    int count_open = 0;
    int count_close = 0;
    for (char c: str){
        if (c == open){
            count_open ++;
        } else if (c == close){
            count_close ++;
        }
    }
    //cout << count_open << ','<< count_close << endl;
    if (count_open == count_close){
        return true;
    } else {
        return false;
    }
}

string V2S(vector <int> anyVect){
    string str = "";
    for (int value: anyVect){
        if (str == ""){
            str = to_string(value);
        } else {
            str = str + ',' + to_string(value);
        }
        
    }
    return str;
}

void check(string c, int i, vector <int> PV, vector <int> OV, vector <int> CV, int ONo, int CNo){
    cout << "c:" <<c << " i"<< i << " postVect:"<< V2S(PV) << " O Vect:" << V2S(OV) << " C Vect:"<< V2S(CV) << " ONo:"<< ONo <<" Cno:"<< CNo << endl;
}

vector <int> postVector(string str, int bracket_type){
    char open_bracket;
    char close_bracket;
    if (bracket_type == 1){
        open_bracket = '(';
        close_bracket = ')';
    } else if (bracket_type == 2){
        open_bracket = '[';
        close_bracket = ']';

    } else if (bracket_type == 3){
        open_bracket = '{';
        close_bracket = '}';
    }

    //cout << "start"<<endl;
    int len_str = str.length();
    int bracketStart = 0;
    int bracketEnd = 0;
    bool bracketPre = false; // 0: don't have a previous brace
    bool multibracket = false; // 0: don't have >2 (
    vector <int> postVect = {};
    vector <int> open = {};
    vector <int> close = {};
    int num_open = 0; // number of open (
    int num_close = 0; // number of close )
    /*
    void check(int c, int i, vector <int> PV, vector <int> OV, vector <int> CV, int ONo, int CNo){
        cout << "c:" << i << " postVect:"<< V2S(PV) << " O Vect:" << V2S(OV) << " C Vect:"<< V2S(CV) << " ONo:"<< ONo <<" Cno:"<< CNo << endl;
    }
    */

    for (int i = 0; i <= len_str; i++){
        
        if ((str[i] == open_bracket) && (bracketPre == false) && (multibracket == false)){ // condition 1: (
            bracketStart = i;
            open.push_back(bracketStart); // open: {1}
            bracketPre = true; // means initiation of (
            num_open++;
            //check("(1", i, postVect, open, close, num_open, num_close);
            
        } else if ((str[i] == close_bracket) && (bracketPre == true) && (multibracket == false)){ // condition 2: ()
            bracketEnd = i;
            postVect.push_back(bracketStart);
            postVect.push_back(bracketEnd);
            open = {};
            num_open--;
            bracketPre = false;
            //check("(2)", i, postVect, open, close, num_open, num_close);

        } else if ((str[i] == open_bracket) && (bracketPre == true) && (multibracket == false)){ // condition3: ((
            num_open = 2;
            bracketStart = i;
            open.push_back(bracketStart); // open: {1,2}
            multibracket = true; // more than 1 (( status
            //check("((3", i, postVect, open, close, num_open, num_close);

        } else if ((str[i] == close_bracket) && (bracketPre == true) && (multibracket == true)){ // condition 4: (((3)
            bracketEnd = i;
            close.push_back(bracketEnd); // close: {4}
            int num_close = 1;
            int j2;
            for (int j = i + 1; num_close < num_open; j++){ 
                if (str[j] == close_bracket){
                    bracketEnd = j;
                    close.push_back(bracketEnd);
                    num_close ++;
                    //cout << "close_no looping" << num_close << endl;
                    //cout << "j:" << j << endl;
                }
                j2 = j;
            }
            i = j2;

            //check("((4))before put inV", i, postVect, open, close, num_open, num_close);

            reverse(close.begin(), close.end());
            for (int ij = 0; ij < num_open; ij++){
                //cout << ij << endl;
                postVect.push_back(open[ij]);
                postVect.push_back(close[ij]);
            }
            //check("((4))before F", i, postVect, open, close, num_open, num_close);

            open = {}; //reset
            close = {};
            num_open = 0;
            num_close = 0;
            multibracket = false;
            bracketPre = false;
            //check("((4))final", i, postVect, open, close, num_open, num_close);

        } else if ((str[i] == open_bracket) && (bracketPre == true) && (multibracket == true)){ //condition 5: ((((
            num_open++;
            bracketStart = i;
            open.push_back(bracketStart);
            //check("(((((5", i, postVect, open, close, num_open, num_close);
        } else if ((str[i] == close_bracket) && (bracketPre == false)){ // condition 6: 123) (multibracket not relevant)
            postVect[1] = 0;
            //cout << "pre():" << i << endl;
            break;
        }
        
    }
    //cout << "start end"<<endl;

    return postVect;
}


int main(){
    //cout << "should be first line" << endl;
    /*
    vector<int> v1 = {0,1,2,4}; // 0 1 2 4 3 5 6 7
    vector<int> v2 = {3,5};
    vector<int> v3 = {6,7};
    */
    
    
    string istr;
    cin >> istr;
    if ((count_bracket('(', ')', istr) == false) ||
    (count_bracket('[', ']', istr) == false ) ||
    (count_bracket('{', '}', istr) == false )) {
        error();
        //cout << "not match no" << endl;
    } else {
        //cout << "before postV" << endl;
        vector<int> v1 = postVector(istr, 1);
        vector<int> v2 = postVector(istr, 2);
        vector<int> v3 = postVector(istr, 3);
        vector<int>blendV = blendVect(v1,v2,v3);
        
        if ((v1[1] == 0)||
        (v2[1] == 0)||
        (v3[1] == 0)||
        (blendV.empty())){
            error();
        } else {
            result(blendV);

        }
    }
    
    



}

