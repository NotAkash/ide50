import sys

def main():
     #TODO
     while True:
          try:
              key = int(sys.argv[1])
              plain = str(input("What is the plaintext? "))
          except IndexError:
              print("Usage: ./caesar k")
              return(False)

          else:
              break
     for i in range(len(plain)):
         if plain[i].isalpha()==True:
             if plain[i].isupper()==True:
                 #Todo print("%c",(((plain[i]-65+s)%26)+65));
                 print("%c"%(( ord(plain[i]) - 65 + key) % 26 + 65), end='')
             elif plain[i].islower()==True:

                 print("%c" %(( ord(plain[i]) - 97 + key) % 26 + 97), end='')
                 #Todo print("%c",((plain[i]-97+s)%26)+97);
         else:
             print(plain[i],end='')
     print()
     return(True)


if __name__ == "__main__":
     main()