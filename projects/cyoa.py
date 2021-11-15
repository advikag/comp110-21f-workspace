"""Shopping cart program!"""
__author__ = "730519109"


points: int 
player: str
s1: list[int] = list()
s2: list[str] = list()


def main()->None :
    """main method"""
 
    points = 0
    greet() 
    input() 
    print(" Welcome to Advika Mart! ")
    print("*************************")
    print("1. Shop Now" + " \U0001F6CD")
    print("2. Quit" + " " + "\U0001F44B")
    print("3. Shopping cart" + "\U0001F6D2")
    print("4. Checkout" + "\U0001F4B0")
  
    print("****************************************************")
    f:int = int(input("Enter the number of the action you would like to perform "))
    if(f == 1) :
        mm(points)
    elif(f==2) :
        bye()
    elif(f==3) :
        cart()
    elif(f==4) :
        check(points)
    else :
        print("invalid input")
        main()

def greet()->None :
    """Greet the user"""
    player = input("Please enter your name ")
    print("Hi! "+ player +", Welcome to Advika Mart!"+" \U0001F6CD")
    print("Press the enter key after every step to proceed")
    input()
    print("\U0001F911"+player+", We are proud to announce that a hundered percent of proceeds go towards Adviks's College Fund"+" \U0001F911	")

def mm(h:int)-> None:
    """Main Menu of the store"""
    points = h
    print("   \U0001F6CD"+"   Main Menu   "+"\U0001F6CD")
    print("********************")
    print("  1. College Merch")
    print("  2. Fruits")
    print("  3. Vegetables") 
    print("  4. Beverages")
    print("  5. Breakfast food")
    print("********************")
    a:int = int (input("Enter the number of the category you want to select "))
    print("*************************")
    if(a == 1):
        cm(points)
    elif(a == 2):
       fru(points)
    elif(a == 3):
        veg(points)
    elif(a == 4):
        bev(points)
    elif( a == 5):
        bre(points)
    else:
        print("Invalid Input")
        print("Press enter to return to the main menu")
        input()
        main()

def cm(x:int)->None:
    y:int = x
    print("\U0001F455"+" Carolina Sweatshirt       $200")
    print("\U0001F9E2"+" UNC hat                    $70") 
    print("\U0001F40F"+" Ramesy stuffed animal      $80")
    print("\U0001F645"+" Beat Duke T-shirt        $100")
    print("************************************8*******")
    print("Enter the name of the item you wish to purchase")
    b:str = input()
    if(b[0]=='c' or b[0]=='C'):
        s1.append(200)
        s2.append("Carolina Sweatshirt")
        points = y + 200
        cart()
    elif(b[0] == 'u' or b[0] == 'U'):
        s1.append(170)
        s2.append(" UNC Hat")
        cart()
        points = y + 70 
    elif(b[0] == 'r' or b[0] == 'R'):
        s1.append(80)
        s2.append("Ramesy Stuffed Animal")
        cart()
        points = y + 80
    elif(b[0] == 'B' or b[0] == 'b'):
        s1.append(100)
        s2.append("Beat Duke T-Shirt")
        cart()
        points = y + 100
    else:
        print("INVALID INPUT")
        print("press enter to return to the main menu")
        input()
        main()
def fru(x:int)-> int:
    """fruit section of the store"""
    y:int = x
    print("Welcome to the fruits section")
    print("Enter the name of the item you want to buy ")
    print("\U0001F34E" + " Apples           $2")
    print("\U0001F34C" + " Bananas          $5") 
    print("\U0001F34A" + " Oranges          $10")
    print("\U0001F351" + " Peaches          $11")
    b:str = input()
    if(b[0]=='a' or b[0]=='A'):
        s1.append(2)
        s2.append("Apples")
        points = y + 2
        cart()
        return points
    elif(b[0] == 'b' or b[0] == 'B'):  
        s1.append(5)
        s2.append("Bananas")
        points = y + 5
        cart()
        return points
    elif(b[0] == 'o' or b[0] == 'O'):
        s1.append(10)
        s2.append("Oranges")
        points = y + 10
        cart()   
        return points
    elif(b[0] == 'p' or b[0] == 'P'):
        s1.append(11)
        s2.append("Peaches")
        points = y + 11
         cart()   
         return points
    else:
        print("INVALID INPUT")
        print("press enter to return to the main menu")
        input()
        main()
        return 0


def veg(x:int)->None:
    """vegetable section"""
    y:int = x 
    print("Welcome to the vegetable section")
    print("Enter the name of the item you want to buy ")
    print("\U0001F952" + " Zuchini       $10")
    print("\U0001F9C5" +" Onions          $15") 
    print("\U0001F952" +" Cucumber        $11")
    print("\U0001FAD1"+ " Bell Peppers    $10") 
    b:str = input()
    if(b[0]=='z' or b[0]=='Z'):
        s1.append(10)
        s2.append("Zuchini")
        cart()
        points = y + 10  
    elif(b[0] == 'o' or b[0] == 'O'):  
        s1.append(15)
        s2.append("Onions")
        cart()
        points = y + 15
    elif(b[0] == 'c' or b[0] == 'C'):
        s1.append(11)
        s2.append("Cucumber")
        cart()
        points = y + 11
    elif(b[0] == 'B' or b[0] == 'b'):
         s1.append(10)
         s2.append("Bell peppers")
         cart()
         points = y + 10
    else:
        print("INVALID INPUT")
        print("press enter to return to the main menu")
        input()
        main()


def bev(x:int)->None:
    """beverage section"""
    y:int = x 
    print("Welcome to the Beverage section")
    print("Enter the name of the item you want to buy ")
    print("\U0001F9C3"+"Caprisun          $5")
    print("\U0001F9CB"+"Lemonade          $6") 
    print("\U0001F379"+"Orange juice      $4")
    print("\U0001F9C9"+"Apple juice       $8")
    b:str = input()
    if(b[0]=='c' or b[0]=='C'):
        s1.append(5)
        s2.append("Caprisun")
        cart()
        points = y + 5  
    elif(b[0] == 'l' or b[0] == 'L'):
        s1.append(6)
        s2.append("Lemonade")
        cart()
        points = y + 6
    elif(b[0] == 'o' or b[0] == 'O'):
        s1.append(4)
        s2.append("Orange juice")
        cart()
        points = y + 4
    elif(b[0] == 'a' or b[0] == 'A'):
        s1.append(8)
        s2.append("Apple Juice")
        cart()
        points = y + 8
    else:
        print("INVALID INPUT")
        print("press enter to return to the main menu")
        input()
        main()


def bre(x:int)->None:
    """breakfast section"""
    y:int = x  
    print("Welcome to the breakfast section")
    print("Enter the name of the item you want to buy ")
    print("\U0001F95E"+"Pancake batter        $12")
    print("\U0001F95A"+"Eggs                  $5") 
    print("\U0001F95B"+"Almond Milk           $8")
    print("\U0001F372"+"Lucky Charms cereal   $11")
    b:str = input()
    if(b[0]=='p' or b[0]=='P'):
        s1.append(12)
        s2.append("Pancake batter")
        cart()
    elif(b[0] == 'e' or b[0] == 'E'):
        s1.append(5)
        s2.append("Eggs")
        cart()
    elif(b[0] == 'a' or b[0] == 'A'):
        s1.append(8)
        s2.append("Almond Milk")
        cart()
    elif(b[0] == 'l' or b[0] == 'L'):
        s1.append(11)
        s2.append("Lucky charms cereal")
        cart()
    else:
        print("INVALID INPUT")
        print("press enter to return to the main menu")
        input()
        main()

def cart()-> None:
     """shopping cart"""
     z: int = 0
     sum:int = 0 ;
     print(" \U0001F6D2"+"Shopping Cart"+" \U0001F6D2")
     print("*****************************************")
     while(z<len(s1)):
         print(s2[z]+ "     " +"$"+str(s1[z])  )
         sum = sum + s1[z]
         z = z+1
         points = sum
         print("Total Bill :"+"$" +str(points))
         print("*****************************************")
         k:str = input ("press c to checkout or press any other key to continue shopping ")
         print("***********************")
         if(k == 'c' or k == 'C'):
              check(sum)
         else:
              mm(points)


def check(l:int)-> None:
    """checkout function"""
    points=l
    print("Thank You For Shopping With Us Today"+"\U0001F499")
    print("\U0001F911"	+"Additionally you will be charged a fee of a 100 Dollars that will go to The Advika Organization"+" \U0001F911	")
    print("*********************************************")
    print("\U0001F4B0"+"Your total bill is $"+ str(points+100)+"\U0001F4B0")
    print("Have A Nice Day!")

def bye()->None:
    print("Bye!")
    print("Thank You For Shopping With Us Today")
   
if __name__ == "__main__":
    main()



  
    