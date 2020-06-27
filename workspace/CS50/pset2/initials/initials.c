#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string n = get_string();                        //get a user string
    if (n!=NULL)                                    //make sure n is valid
    {
        
        for (int i=0,stl=strlen(n); i< stl;i++)     //for loop to iterate of the "i" and make the loop last while its less than the string lenth (n)
        {
            
            char s;
            s=' ';                                  //space character to cross check with each typed input
            
            if (i==0 && n[i]!=s)                    //if i is 0(first initial can't be before a space) and i isn't space
            {
                printf("%c",toupper(n[i]));         //print that character 
            }
            
            if (n[i-1]==s && n[i]!=s)               //if the last character is space AND this character isn't space
            {
                printf("%c",toupper(n[i]));         //print character
            }
            
        }    
    }
    printf("\n");                                   //New line
}