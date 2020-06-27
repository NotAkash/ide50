#Mario.py done solely through root python, no import cs50 needed/used


def main():
     #TODO : Get validated input for height
     
     while True:
          try:
               height = int(input("Height: "))    #Get user input for height
          except ValueError:
               continue            #Validate integer
          if height<0 or height>23:          #Valdate block height
               print("Height can't be more than 23 or less than 0")
               continue
          else:
               print("Height is",height)     #validated
               break
     for i in range(height):                 #print blocks
          for a in range(height-(i+1)):
               print(" ",end='')    #Spaces
          for a in range(i+1):
               print("#",end='')   #Block
          print("  ",end='')
          for a in range(i+1):
               print("#",end='')   #Other side block
          print()
     #TODO : Make design for mario blocks
     
     

if __name__ == "__main__":
     main()              #Launch main