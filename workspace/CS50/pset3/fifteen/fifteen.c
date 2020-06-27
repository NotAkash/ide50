/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */
 
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
            
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = get_int();
        
        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("[Illegal move]\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(500000);
    }
    
    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO THE GAME OF FIFTEEN\n");
    usleep(2000000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).  
 */
void init(void)
{
    int rd= (d*d)-1;                   //make the end number (d*d)-1 (ie in case of 3: (3*3)-1==8)

    for (int i=0;i<d;i++)            //for i is 0, while i is less than rd ^^ increment by 1 = the row
    {
        for (int j=0; j<d; j++)       //for j is 0 while j is less than d increment by 1  = column
        {
            board[i][j]=rd;         //make the board's row and column the rd ()
            rd--;                   //reduce rd by 1 so the next  number can be reached
            
        }
    }
    if (d%2==0)                     //if d is  divisible by 2 (ie an even number)
    {
        board[d-1][d-3]=1;          //replace the (d -1)'th row and the (d-3)th collumn by 1 
        board[d-1][d-2]=2;          //replace the (d -1)'th row and the (d-2)th collumn by 2 
                                    //ie: replace 2 with 1
    }
}

/**
 * Prints the board in its current state.
 */
void draw(void)
{
    for(int i =0; i<d;i++)          //for i is 0, while i is less than d, increment i
    {
        for(int j=0; j<d;j++)       //for j is 0, while j is less than d increment j
        {
           if (board[i][j] == 0)    //if the board's ith row and jth collumn is 0 (number choosen to represent the blank tile)
           {
               printf("  _");      //print underscore
           }
           else
           {
               printf("%3i",board[i][j]); //else print the tile's assigned value from above with indents for upto 3 places
           }
        }
        printf("\n");                   //print new line twice for a proper grid 
        printf("\n");

    }

}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false. 
 */
bool move(int tile)
{
    for(int i =0; i<d;i++)          //for i is 0, while i is less than d, increment i
    {
        for(int j=0; j<d;j++)       //for j is 0, while j is less than d increment j
        {
            if(board[i][j]==0)
            {
                if(board[i][j-1]==tile)             //Move Left (if the collumn to the left is tile)
                {
                    board[i][j]=board[i][j-1];  //change the current tile the tile to the left
                    board[i][j-1]=0;            //replace the tile to the left to the given value '0' 
                    return true;
                }
                if(board[i-1][j]==tile)             //Move Up (if the row above is the given tile)
                {
                    board[i][j]=board[i-1][j];  //change the current tile with the tile above
                    board[i-1][j]=0;            //replace the tile above to the given value '0'
                    return true;
                }
                if(board[i][j+1]==tile)             //Move Right (if the collumn to the right is the tile)
                {
                    board[i][j]=board[i][j+1];  //change the current tile to the tile to the right
                    board[i][j+1]=0;            //replace the tile to the right to the given value '0'
                    return true;
                }
                if(board[i+1][j]==tile)             //Move Down (if the row below is the tile given)
                {
                    board[i][j]=board[i+1][j];  //change the current tile with the tile below
                    board[i+1][j]=0;            //replace the tile above with 0
                    return true;
                }
                
            }
           
        }
    }
    return false;                               //if move is valid return true; else return false;
}

/**  
 * Returns true if game is won (i.e., board is in winning configuration),  
 * else false.
 */
bool won(void)
{
    int win=1;                                          //start the wincounter with 1
    int rd= (d*d)-1;                                    //make the end number (d*d)-1 (ie in case of 3: (3*3)-1==8)
    for(int i=0;i<d;i++)                                //for i is 0, while i is less than d, increment i
    {
        for(int j=0;j<d;j++)                            //for j is 0, while j is less than d, increment j
        {
            if(board[i][j]==win)                        //if board's value is the win counter
            {
            
                if(win>=rd && board[d-1][d-1]==0)       //if win is more than or equal to rd and the board's [2nd row] and [2nd collumn] is 0
                {
                    return true;                        //return true
                    break;                              //break
                }
                win++;                                  //else increment win
            }
            
        }
    }

    return false;                                           //if at end the list isn't sorted return false;
}