#include "timSort.h"

const int RUNSIZE = 32;

timSort::timSort()
{

}

int timSort::findMin(int x, int y)
{
	if (x < y)
		return x;
	else return y;
}

void timSort::insertionSort(int data[], int left, int right)
{
	for (int i = left + 1; i <= right; i++)
	{
		int temp = data[i];
		int j = i - 1;
		while (j >= left && data[j] > temp)
		{
			data[j + 1] = data[j];
			j--;
		}
		data[j + 1] = temp;
	}
}

void timSort::Merge(int data[], int left, int middle, int right)
{
	int length1 = middle - left + 1;
	int length2 = right - middle;
	int* leftarray = new int[length1];
	int* rightarray = new int[length2];
	for (int i = 0; i < length1; i++)
		leftarray[i] = data[left + i];
	for (int i = 0; i < length2; i++)
		rightarray[i] = data[middle + 1 + i];
	int i = 0;
	int j = 0; 
	int k = left;
	while (i < length1 && j < length2)
	{
		if (leftarray[i] <= rightarray[j])
		{
			data[k] = leftarray[i];
			i++;
		}
		else
		{
			data[k] = rightarray[j];
			j++;
		}
		k++;
	}
	while (i < length1)
	{
		data[k] = leftarray[i];
		k++;
		i++;
	}
	while (j < length2)
	{
		data[k] = rightarray[j];
		k++;
		j++;
	}
	delete[] leftarray;
	delete[] rightarray;
}

void timSort::Sort(int data[], int arraysize)
{
	for (int i = 0; i < arraysize; i += RUNSIZE)
		insertionSort(data, i, findMin((i + RUNSIZE - 1), (arraysize - 1)));
	for (int size = RUNSIZE; size < arraysize; size = 2 * size)
	{
		for (int left = 0; left < arraysize; left += 2 * size)
		{
			int middle = left + size - 1;
			int right = findMin((left + 2 * size - 1), (arraysize - 1));
			if (middle < right)
			{
				Merge(data, left, middle, right);
			}
		}
	}
}