#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string arg = argv[1];
    if (argc!=2)
    {
        printf("Usage: ./caesar k\n");      //error message 1 (To Many Arguments)
        return 1;
    }
    for (int alpac=0; alpac<strlen(arg); alpac++)
    {
        if (isalpha(arg[alpac]))
        {
            continue;
        }
        else
        {
            printf("Usage: ./caesar k\n");      //error message 1 (To Many Arguments)
            return 1; 
        }
    }
                                //gets integer s and converts the string into character <key> and that - 48 to get integer
    printf("plaintext: ");
    string mess= get_string();         //get a message
    printf("ciphertext: ");
    
    int j=0;
    for (int i=0; i<strlen(mess);i++)
    {
        if (isalpha(mess[i]))
        {
            if (isupper(mess[i])) 
            {
                if (isupper(arg[j]))
                {
                    printf("%c",((mess[i]-65+(arg[j]-65))%26)+65);
                }
                else
                {
                    printf("%c",((mess[i]-65+(arg[j]-97))%26)+65);
                }
            }
            if (islower(mess[i]))
            {
                if (islower(arg[j]))
                {
                    printf("%c",((mess[i]-97+(arg[j]-97))%26)+97);
                }
                else
                {
                    printf("%c",((mess[i]-97+(arg[j]-65))%26)+97);
                }
            }
        j++;
        j=j%strlen(arg);
        }
        else
        {
            printf("%c",mess[i]);
        } 
    }
    printf("\n");
    return 0;
}