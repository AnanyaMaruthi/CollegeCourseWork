#include <bits/stdc++.h>
using namespace std;

int kMin(int array[], int n, int k){
	for(int i = 0; i <= k - 1; i++){
		int minIndex = i;
		for(int j = i + 1; j <= n - 1; j++){
			if(array[j] < array[minIndex]){
				minIndex = j;
			}
		}
		if(minIndex != i){
			int temp = array[minIndex];
			array[minIndex] = array[i];
			array[i] = temp;
		}
	}
	return array[k - 1];
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
	int kmin = kMin(array, n, k);
	cout << "\n" << k << " smallest element is " << kmin << endl;
}