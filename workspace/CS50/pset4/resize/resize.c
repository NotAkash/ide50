/**
 * Resizes a BMP piece by piece, just because.
 */
       
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "bmp.h"
int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./copy key infile outfile\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];
    int n = atoi(argv[1]);

    if (n < 1 || n > 100)
    {
        printf("n must be a number between [1 and a 100]\n");
        return 2;
    }

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 5;
    }

    int owidth = bi.biWidth;
    int oheight = bi.biHeight;
    bi.biWidth = owidth * n;
    bi.biHeight = oheight * n;
    int oldpadding;
    oldpadding = (4 - (owidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    bi.biSizeImage= (bi.biWidth*sizeof(RGBTRIPLE)+padding) * abs(bi.biHeight);
    bf.bfSize = (bi.biSizeImage) + 54; //54 is num of bits
    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

	for (int i = 0; i < abs(oheight); i++)
    {
        for (int j = 0; j < n; j++)
        {   
           fseek(inptr, (54 + ((owidth*3 + oldpadding) * i)), SEEK_SET);
            for (int ip = 0; ip < owidth; ip++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // write RGB triple to outfile
                for (int pj = 0; pj < n; pj++){
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);   
                }
            }
            // add padding
            for (int pad = 0; pad < padding; pad++)
            {
                fputc(0x00, outptr);                
            }

        }
    }
    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // done boi
    return 0;
}
