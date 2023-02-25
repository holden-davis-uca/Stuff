#pragma once
class timSort
{
public:
	timSort();
	int findMin(int x, int y);
	void insertionSort(int data[], int leftindex, int rightindex);
	void Merge(int data[], int left, int middle, int right);
	void Sort(int data[], int arraysize);
};