#include <bits/stdc++.h>
using namespace std;

int squareRoot(int num){
	int low = 1;
	int high = num;
	int mid;
	while(low <= high){
//		cout << low << " " << high << endl;
		mid = (low + high) / 2;
		if(num == mid * mid){
			return mid;
		}
		else if(num < mid * mid){
			high = mid - 1;
		}
		else{
			low =  mid + 1;
		}
	}
	return -1;
}

int main(){
	int num, root;
	cout << "Enter number ";
	cin >> num;
	root = squareRoot(num);
	if(root == -1){
		cout << "\nRoot is not an integer" << endl;
	}
	else{
		cout << "\nThe square root is " << root << endl;
	}
	
}