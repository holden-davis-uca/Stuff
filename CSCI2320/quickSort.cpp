#include "quickSort.h"

quickSort::quickSort()
{

}

void quickSort::swap(int* a, int* b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int quickSort::breaker(int data[], int lower, int higher)
{
    int pivot = data[higher];
    int lowerindex = (lower - 1);
    for (int i = lower; i <= higher - 1; i++)
    {
        if (data[i] <= pivot)
        {
            lowerindex++;
            swap(&data[lowerindex], &data[i]);
        }
    }
    swap(&data[lowerindex + 1], &data[higher]);
    return lowerindex + 1;
}

void quickSort::Sort(int data[], int lower, int higher)
{
    if (lower < higher)
    {
        int breakerindex = breaker(data, lower, higher);
        Sort(data, lower, breakerindex - 1);
        Sort(data, breakerindex + 1, higher);
    }
}