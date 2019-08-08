#include <bits/stdc++.h>
using namespace std;

int binarySearch(int element, int array[], int size){
	int low = 0;
	int high = size - 1;
	int mid;
	while(low <= high){
		mid = (low + high) / 2;
		if(array[mid] == element){
			return mid;
		}
		else if(array[mid] < element){
			low = mid + 1;
		}
		else{
			high = mid - 1;
		}
	}
	return -1;
}

int main(){
	int array[10];
//	cout << "Enter elements: " << endl;
	for(int i = 0; i < 10; i++){
		array[i] = rand() % 10000;
	}
	cout << "Array elements are: " << endl;
	for(int i = 0; i < 10; i++){
		cout << array[i] << " ";
	}
	int element;
	cout << endl;
	cout << "Enter element";
	cin >> element;
	int position;
	position = binarySearch(element, array, 10);
	if(position < 0){
		cout << "Element not found";
	}
	else{
		cout << "Element found at " << position << endl;
	}
}
