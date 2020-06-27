/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    if (n<=0) //if n is less than or is 0 return false,
    {
    return false;
    }
    int first;     
    int last;        //First is 0 last is the term -1
    int midpoint;
    first=0;
    last= n-1;
    while (first<=last)// while first is less than or equal to last 
    {
        midpoint= (first+last)/2; //midpoint is first+last divided by 2. This gives us the middle element
        if (midpoint[values]==value)
        {
            return true;        //if midpoint'th term of list is the given number return true|| break loop
        }
        if (midpoint[values]>value)
        {
            last=midpoint-1;    //if midpoint'th term of list is less than value make the last term 1 less than midpoint (eliminate everything ahead of midpoint)
        }
        else
        {
            first=midpoint+1; //else make first the term after midpoint (eliminate everything behind midpoint)
        }
        
    }
    return false; //if at end of loop true is not returned, then return false
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement an O(n^2) sorting algorithm
    int swap;
    swap = 0;                          //swap counter is 0
    for (int j=0;j<n-1;j++)             //initialise j to be 1 less than n
    {                                   //n-1 is the number of elements
        for(int pl=0;pl<n-1-j;pl++)     //initialise pl(placement) to be 1 less than n-1
        {
            if (values[pl]>values[pl+1]) //if the current placement'th value is less than the next value
            {
                int temp = values[pl];              //make a temp variable for that element to go to
                values[pl] = values[pl+1];          //make the (placement+1) element the placement
                values[pl+1] = temp;                // make the current placement placement+1
                swap++;                             //add 1 to swap
            }
            if (swap==0)
            {   
                break;                              //if nothing is swapped (list is sorted) then break
            }
        }
        
    }
    return;
}
