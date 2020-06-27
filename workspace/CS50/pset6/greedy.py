#greedy.py done solely through root python, no import cs50 needed/used


#quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)
def main():    #Main
     while True:
          try:
               change = float(input("O hai! How much change is owed?: "))    #Get user input for height
          except ValueError:
               continue            #Validate integer
          if change<=0:
               continue
          else:
               print("Change owed Is:",change)     #validated
               break

     newchange = round(change,2)
     newchange= newchange*100
     count=0
     while(newchange!=0):
          while(newchange>=25):
               # Quarter reduced from newchange incriment count
               newchange-= 25
               count+=1

          while(newchange>=10):
               # Dime reduced from newchange incriment count
               newchange-= 10
               count+=1

          while(newchange>=5):
               # Nickel reduced from newchange incriment count
               newchange-= 5
               count+=1

          while(newchange>=1):
               # Penny reduced from newchange incriment count
               newchange-= 1
               count+=1


     print(count, "coins")
     return(True)
if __name__ == "__main__":
     main()