
from cal import do_addition,do_sub,do_dividion
from muliply import do_multipli
from area import area_rec
def main():
    
    print("welcome to te ar")
    print("efc erfvd ervfd")
    
    user_input=input("select the part system  1: add  2: subtrat 3: multiply 4: didicde")
    a=int(input("A"))
    b=int(input("B"))
        
    
    if user_input=="1":
        result=do_addition(a,b)
        
    elif user_input=="2":
        result=do_sub(a,b)
        
    elif user_input=="3":
        result=do_multipli(a,b)
        
    elif user_input=="4":
        result=do_dividion(a,b)
    print(result)
    
    
if __name__=="__main__":
    main()
    
    
    
        
        
    
    