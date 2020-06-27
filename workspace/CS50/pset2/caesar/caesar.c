#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
int main(int argc, string argv[])
{
    if (argc!=2)
    {
        printf("Usage: ./caesar k\n");      //error message 1
        return 1;
    }
    
                                
    int s;
    s = atoi(argv[1]);                      //gets integer s and converts the string into number
    string mess; 
    printf("plaintext: ");
    mess= get_string();                     //get a message
    printf("ciphertext: ");
    for (int i=0; i<strlen(mess);i++)       //for loop to continue till the entire word isn't cyphered
    {
        if (isalpha(mess[i]))               //if (mess[i] which is) the character is alphabet
        {
            if (isupper(mess[i]))           //if (mess[i] which is) the character is upper case
            {
                printf("%c",(((mess[i]-65+s)%26)+65)); //print the character which is the i'th character -65 +key mod 26 +65 (65 is the ascii "A")
            }
            if (islower(mess[i]))           //if (mess[i] which is) the character is lower case
            {
                printf("%c",((mess[i]-97+s)%26)+97);  //print the character which is the i'th character -97 +key mod 26 +key (97 is the ascii "A")
            }
        }
        else
        {
            printf("%c",mess[i]);           //else if it is not a character print as such
        }
    }
    printf("\n");                           //new line 
    return 0;                               // no error
}