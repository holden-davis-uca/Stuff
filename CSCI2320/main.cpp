#include <iostream>
#include <ctime>
#include <chrono>
#include "quickSort.h"
#include "radixSort.h"
#include "timSort.h"

using namespace std;

void generateUnsortedArray(int* a, int capacity);
void cloneArray(int* source, int* dest, int capacity);
void printFirstElements(int* a, int numOfElements);
void startTiminigs();
double endTimings();

const int MINIMUM_ELEMENTS = 1000;

chrono::steady_clock::time_point start;

int main() {

	int* unsortedArray1 = new int[MINIMUM_ELEMENTS];
	int* unsortedArray2 = new int[MINIMUM_ELEMENTS];
	int* unsortedArray3 = new int[MINIMUM_ELEMENTS];

	quickSort* quick_sort = new quickSort();
	radixSort* radix_sort = new radixSort();
	timSort* tim_sort = new timSort();

	generateUnsortedArray(unsortedArray1, MINIMUM_ELEMENTS);
	cloneArray(unsortedArray1, unsortedArray2, MINIMUM_ELEMENTS);
	cloneArray(unsortedArray1, unsortedArray3, MINIMUM_ELEMENTS);

	startTiminigs();
	quick_sort->Sort(unsortedArray1, 0, MINIMUM_ELEMENTS - 1);
	cout << "Quick Sort on unsorted array took " << endTimings() << " ms" << endl;
	printFirstElements(unsortedArray1, 15);

	startTiminigs();
	radix_sort->Sort(unsortedArray2, MINIMUM_ELEMENTS);
	cout << "Radix Sort on unsorted array took " << endTimings() << " ms" << endl;
	printFirstElements(unsortedArray2, 15);

	startTiminigs();
	tim_sort->Sort(unsortedArray3, MINIMUM_ELEMENTS);
	cout << "Tim Sort on unsorted array took " << endTimings() << " ms" << endl;
	printFirstElements(unsortedArray3, 15);

	startTiminigs();
	quick_sort->Sort(unsortedArray1, 0, MINIMUM_ELEMENTS - 1);
	cout << "Quick Sort on sorted array took " << endTimings() << " ms" << endl;
	printFirstElements(unsortedArray1, 15);

	startTiminigs();
	radix_sort->Sort(unsortedArray2, MINIMUM_ELEMENTS);
	cout << "Radix Sort on sorted array took " << endTimings() << " ms" << endl;
	printFirstElements(unsortedArray2, 15);

	startTiminigs();
	tim_sort->Sort(unsortedArray3, MINIMUM_ELEMENTS);
	cout << "Tim Sort on sorted array took " << endTimings() << " ms" << endl;
	printFirstElements(unsortedArray3, 15);

	delete[] unsortedArray1;
	delete[] unsortedArray2;
	delete[] unsortedArray3;
	delete quick_sort;
	delete radix_sort;
	delete tim_sort;
	
}

void generateUnsortedArray(int* a, int capacity) {
	srand(time(NULL)); // Set randomization seed every array generation

	for (int i = 0; i < capacity; i++) {
		a[i] = rand() % 1000 + 1; // Set the array value at index i to a random value between 1 and 1000.
	}
}

void cloneArray(int* source, int* dest, int capacity) {
	for (int i = 0; i < capacity; i++) {
		dest[i] = source[i];
	}
}

void printFirstElements(int* a, int numOfElements) {
	for (int i = 0; i < numOfElements; i++) {
		cout << a[i] << ", ";
	}
	cout << endl;
}

void startTiminigs() {
	start = chrono::steady_clock::now(); // set the begin timestamp of time execution
}

double endTimings() {
	return chrono::duration <double, milli>(chrono::steady_clock::now() - start).count();
}
