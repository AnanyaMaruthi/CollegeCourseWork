#include <bits/stdc++.h>
using namespace std;

int max(int array[], int size){
	int max = array[0];
	for(int i = 1; i < size; i++){
		if(array[i] > max){
			max = array[i];
		}
	}
	return max;
}

int main(){
	int array[5];
//	cout << "Enter array elements: " << endl;
	for(int i = 0; i < 5; i++){
		array[i] = rand() % 10000;
	}
	cout << "Array elements are: " << endl;
	for(int i = 0; i < 5; i++){
		cout << array[i] << " ";
	}
	cout << "The maximum element is " << max(array, 5);
	return 0;
}