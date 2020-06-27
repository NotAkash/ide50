#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num;
    do{
        printf("Height: ");
        num = get_int();
    }
    while(num<0 || num>23);
    {
    }
    
    for (int i =0; i< num; i++)
    {
        for(int a=0; a<(num-(i+1));a++)
        {
            printf(" ");//spaces
        }
        for(int b=0; b<(i+1); b++)
        {
            printf("#");//pyramid blocks
        }
        printf("  ");
         for(int c=0; c<(i+1); c++)
        {
            printf("#");//pyramid blocks
        }
        printf("\n");

    }
    
}