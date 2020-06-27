#include <cs50.h>
#include <stdio.h>
#include <math.h>
int main(void)
{
    float money;
    do
    {
        printf("O hai! How much change is owed?: \n");
        money = get_float();
    }
    while(money<0);
    int newnum = (int) round(money*100);
    printf("%i\n",newnum);
    int count=0;
        while (newnum>=25)
        {
            newnum=(newnum-25);
            count= count+1;
        }
        while (newnum>=10)
        {
            newnum=(newnum-10);
            count= count+1;
        }
        while (newnum>=5)
        {
            newnum=(newnum-5);
            count= count+1;
        }
        while (newnum>=1)
        {
            newnum=(newnum-1);
            count= count+1;
        }
    printf("%i\n",count);
}