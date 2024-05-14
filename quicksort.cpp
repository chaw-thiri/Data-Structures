// divide, conquer & combine
# include <iostream>
using namespace std;


// prototype 
int partition(int arr[], int i, int h);
void quickSort(int a[], int l, int h);


int main() {
	int arr[] = { 45,9,10,75,80,21 };
	int size = sizeof(arr) / sizeof(arr[0]);
	quickSort(arr, 0, size);
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
		
	}
	return 0;
}

void quickSort(int arr[], int l, int h) {
	// l = low, h = height
	int pivot = partition(arr, l, h);
	if (l < h) {
		quickSort(arr, l, pivot);
		quickSort(arr, pivot + 1, h);
	}
}
int partition(int arr[], int l, int h) {
	int pivot = arr[l];
	int i = l;
	int j = h;
	while (i < j) {
		do {
			i++;
		} while (arr[i] <= pivot);
		do {
			j--;
		} while (arr[j] > pivot);
		if (i < j) {
			swap(arr[i], arr[j]);
		}

	
	
	}
	swap(arr[l], arr[j]);
	return j;
}
