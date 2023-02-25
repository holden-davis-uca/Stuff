#include "radixSort.h"

radixSort::radixSort()
{

}

int radixSort::retrieveHigher(int data[], int arraysize)
{
	int highest = data[0];
	for (int i = 0; i < arraysize; i++)
		if (data[i] > highest)
			highest = data[i];
	return highest;
}

void radixSort::countSort(int data[], int arraysize, int digitindex)
{
	int* outdata = new int[arraysize];
	int i, count[10] = { 0 };
	for (int i = 0; i < arraysize; i++)
		count[(data[i] / digitindex) % 10]++;
	for (int i = 1; i < 10; i++)
		count[i] += count[i - 1];
	for (int i = arraysize - 1; i >= 0; i--)
	{
		outdata[count[(data[i] / digitindex) % 10] - 1] = data[i];
		count[(data[i] / digitindex) % 10]--;
	}
	for (int i = 0; i < arraysize; i++)
		data[i] = outdata[i];
	delete[] outdata;
}

void radixSort::Sort(int data[], int arraysize)
{
	int maximum = retrieveHigher(data, arraysize);
	for (int i = 1; maximum / i > 0; i *= 10)
		countSort(data, arraysize, i);
}