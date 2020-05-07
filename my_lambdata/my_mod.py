
#my_mod.py

def enlarge(n):
    return n*100

if __name__ == "__main__":
  #only run the code below if executed from command line
  # otherwise dont run it for eg if we are trying to import it 
 x = 5
 print(enlarge(x))    
 y = int(input("Please choose a number(eg.5):"))
 print(enlarge(y))
