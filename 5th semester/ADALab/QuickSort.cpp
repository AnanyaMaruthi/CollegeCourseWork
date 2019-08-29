#include <iostream>
using namespace std;

int *quickSort(int arr[], int low, int high)
{
    if (low >= high)
    {
        return arr;
    }
    int pivot = low;
    int i = low + 1;
    int j = high + 1;
    int temp;
    while (i < j)
    {
        if (arr[i] > arr[pivot])
        {
            j -= 1;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        else
        {
            i += 1;
        }
    }
    temp = arr[pivot];
    arr[pivot] = arr[i - 1];
    arr[i - 1] = temp;
    pivot = i - 1;
    arr = quickSort(arr, low, pivot - 1);
    arr = quickSort(arr, pivot + 1, high);
    return arr;
}

int main()
{
    int n;
    cout << "Enter number of element: ";
    cin >> n;
    int arr[n];
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    int *sortedArray;
    sortedArray = quickSort(arr, 0, n - 1);
    cout << "The sorted array is: ";
    for (int i = 0; i < n; i++)
        cout << sortedArray[i] << " ";
}