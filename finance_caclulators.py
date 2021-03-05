
import math

#Write a function that asks the user if they want to essentially restart the program. 
#If the boolean is True program will run again
#If they type anything that doesn't start with an 's', the program will end
#I learnt how to do this from the Udemy Python Zero to Hero Bootcamp
#Use index[0] and .lower() to make sure user capitalisation and spelling does not affect program
#Note, this function is in lieu of an error message because I couldn't figure out how to do it without the error message popping up at the end of the program even when the it was run successfully
def redo():
    
    return input('\nDo you want to calculate any other investment returns or bond payments? Enter Yes or No: ').lower().startswith('y')





#Creating a while loop does two things:
#1. It allows the user to repeat the program if their response to the initial input() question is not valid
#2. If user input was valid, it still allows for them to opt out or repeat the program if they would like
while True:
    
    #Ask user to choose between investment calculator and bond calculator using input()
    #Use \n and/or triple quotation marks two write string on multiple lines. The triple quotation marks made it easier for me to read my own code instead of having it spread out too far like this line
    #I know string spacing looks awful in this code but I did it to make the text line up for the user line the PDF example
    calculation = input('''Choose either 'investment' or 'bond' from the menu below to proceed: 
    \ninvestment    - to calculate the amount of interest you'll earn on your investment \nbond          - to calculate the amount you will have to pay on a home loan \n''')
    
    #Create a total return variable and assign the value of 0 
    #This variable will be used to calculate the results of all the possible formulas
    total_return = 0

    



    #Code for if user selects investment
    #Use index[0] and .lower() to make sure user capitalisation and spelling does not affect program
    if calculation[0].lower() == "i": 
        
        #Amount of money they're depositing
        #Use float() to account for decimal points
        principal_amount = float(input("How much would you like to invest?: "))
    
        #Interest rate 
        interest_rate = float(input("What is your expected interest rate?: "))/100
    
        #Number of years they plan to invest
        #Use int() for simplicity
        num_of_years = int(input("For how many years to you plan on holding this investment?: "))
    
        #Ask them to choose between simple or compound interest then display return for simple interest
        #Note more use of indexing[0] and .lower() to minimise chance of program error
        #Note empty string for spacing to make it more readable for user
        #Use .format() to print out required data within the strings
        #You will recognise here the total_return variable from earlier coming into play
        type_of_interest = input("Would you like an interest that returns compound or simple interest? Enter 'simple' or 'compound': ")
        if type_of_interest[0].lower() == "s":
            total_return = principal_amount*(1+interest_rate*num_of_years)
            simple_interest_earned = total_return - principal_amount
            print ("")
            print ("Total Take Home Amount = R{}".format(total_return))
            print ("Amount Invested = R{}".format(principal_amount))
            print ("Interest Earned on Investment = R{}".format(simple_interest_earned))
            
        #Similar code to above only formula and strings adjusted to display compound interest returns to user        
        elif type_of_interest[0].lower() == "c":
            total_return = round(principal_amount * (math.pow((1 + interest_rate*100/(100*12)), (12*num_of_years))))
            compound_interest_earned = total_return - principal_amount
            print ("")
            print ("Total Take Home Amount = R{}".format(total_return))
            print ("Amount Invested = R{}".format(principal_amount))
            print ("Interest Earned on Investment = R{}".format(compound_interest_earned))
            

            

        

    #Code for if user selects bond:
    #Note more use of indexing[0] and .lower() to minimise chance of program error
    if calculation[0].lower() == "b":
        
        #The present value of the house
        home_value = float(input("What is the current value of your home?: "))
        
        #The interest rate
        bond_interest_rate = float(input("What is the interest rate on the bond?: "))/100
        
        #The number of months they plan to take to repay
        num_of_months = int(input("How long is the bond repayment period in months?: "))
        
        #Calculate how much money the user would have to pay each month and display to user
        monthly_payments = round(((bond_interest_rate/12)*(home_value))/(1 - (1+(bond_interest_rate/12))**(-num_of_months)))
        print("\nMonthly payment = R{}".format(monthly_payments))
        




    
    #Execute function to enable repeat of program in case of user error at initial input question
    #Or enable user to do another calculation should they wish
    #Or enable user to quit the program
    if not redo():
        print ("Thank you. Goodbye!")
        break
       
