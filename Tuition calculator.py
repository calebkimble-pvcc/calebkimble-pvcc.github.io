# Name: Caleb Kimble, Tre Williams
# Prog Purpose: This program find the cost of tuition
# Price for in state tuiiton: 156.61
# Price of out of state tuition: 336.21
# Price of capital fee: 23.50
# Price of institutional fee: 1.75
# Price of activity fee: 2.90

import datetime

# define goal variables #
# define tax rate, service fee, and prices
RATE_TUITION_IN = 156.61
RATE_TUITUION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in state, 2 means out-of state
num_credits = 0
scholarship = 0

tuition_amt = 0
inst_fee = 0
act_fee = 0
cap_fee = 0
total = 0
balance = 0

# define program funcitons
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student? : (Y or N)")
        if yesno == "N" or yesno =="n":
            another_student = False

def get_user_data():
    global inout,num_credits,scholarship
    inout = int(input("Enter a 1 for IN-STATE; enter 2 for OUT-OF-STATE: "))
    num_credits = int(input("Number of credits registered for: "))
    scholarship = int(input("Scholarship amount recieved: "))

def perform_calculations():
    global tuition_amt,inst_fee,act_fee,cap_fee,total,balance,scholarship

    if inout == 1: 
        tuition_amt = RATE_TUITION_IN*num_credits
        cap_fee = 0
    else:
        tuition_amt = RATE_TUITUION_OUT*num_credits
        cap_fee = RATE_CAPITAL_FEE*num_credits

    inst_fee = RATE_INSTITUTION_FEE*num_credits
    act_fee = RATE_ACTIVITY_FEE*num_credits
    total = tuition_amt + inst_fee + act_fee + cap_fee
    balance = total - scholarship

def display_results():
    global tuition_amt,inst_fee,act_fee,cap_fee,total,balance,scholarship
    currency = '8,.2f'
    print('-------------------------------')
    print('----------PVCC Tuituion--------')
    print('-------------------------------')
    print('Tuition            $ ' + format(tuition_amt,currency))
    print('Institutional fee  $ ' + format(inst_fee,currency))
    print('Activity fee       $ ' + format(act_fee,currency))
    print('Capital fee        $ ' + format(cap_fee,currency))
    print('Scholarship        $ ' + format(scholarship,currency))
    print('Total              $ ' + format(total,currency))
    print('Balance            $ ' + format(balance,currency))
    print('------------------------------')
    print(str(datetime.datetime.now()))


#### Call on main program to execute
main()