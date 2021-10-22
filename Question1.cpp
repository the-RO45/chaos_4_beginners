
using namespace std;
#include <string>
#include <iostream>

int solution(int n){
    // code here
	int unit1,unit2;
    	int temp=n/3;
	if(n%3==2){
		unit1=temp;
		unit2=(n-unit1)/2;
	}
	else{
		unit2=temp;
		unit1=n-(2*unit2);
	}

	return unit1 + unit2;
	
}

/*  Do not edit below code */
int main() {
	int n;
	cin >> n;	
    int answer=solution(n);
	cout << answer << endl;	
}
