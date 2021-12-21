#include "md5.h"
#include <iostream>

using namespace std;

int main(){
	    string input;
    string encrypted; 
    string username = "userattack";
    cout << "Enter the password: ";
    cin >> input;
    input = input + username;
    encrypted = md5(input);
    if(encrypted == "668493d10d22f9d2b4caa79b8ff79fdb"){
        cout << "Access granted";
    }
    else{
        cout << "Wrong password";
    }

	return 0;
}
