#include <bits/stdc++.h>
using namespace std;

void kMax(int array[], int n, int k){
	cout << "\n" << k << " largest elements are: ";
	for(int i = 0; i <= k - 1; i++){
		int maxIndex = i;
		for(int j = i + 1; j <= n - 1; j++){
			if(array[j] > array[maxIndex]){
				maxIndex = j;
			}
		}
		if(maxIndex != i){
			int temp = array[maxIndex];
			array[maxIndex] = array[i];
			array[i] = temp;
		}
		cout << array[i] << "  ";
	}
	
}

int main(){
	int n, k;
	cout << "Enter size: ";
	cin >> n;
	int array[n];
	cout << "\nEnter elements" << endl;
	for(int i = 0; i < n; i++){
		cin >> array[i];
	}
	cout << "\nEnter k: " ;
	cin >> k;
	kMax(array, n, k);
	
}