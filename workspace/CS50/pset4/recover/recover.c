/**
 * Recovers a JPG piece by piece, just because.
 */
#include <stdio.h>
#include <stdint.h>
int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover infile\n");
        return 1;
    }
              
    char* infile = argv[1]; //Infile Is The First (Second) Argument
    FILE *fp= fopen(infile, "r"); //Open Infile
    
	if ((fp = fopen("card.raw", "r")) == NULL)
    {
        fprintf(stderr,"Error opening file...");        //If Card Is Empty
        return 2;
    }
    uint8_t buf[512];           //a type of unsigned integer of length 8 bits which is 512
  
    char aname[10];             //cons char for filenamez
   
    FILE* tp = NULL; 
    int count = 0;
    // until file ends
    while (!feof(fp))
    {
       
        if (buf[0] == 0xff && buf[1] == 0xd8 && buf[2] == 0xff && (buf[3] == 0xe0 || buf[3] == 0xe1))
        {
            // if already there, get rid of file
            if (tp != NULL)
            {
                fclose(tp);
            }
            sprintf(aname,"%03i.jpg",count); //set new name
            tp = fopen(aname, "w");         
            fwrite(buf, sizeof(buf), 1, tp);
            count++;                        //increase count


        }
        else if (count > 0)
        {

            fwrite(buf, sizeof(buf), 1, tp);            
            
        }
        fread(buf,512, 1, fp);
    
    }

    return 0;
}
    
   
