# Name: Caleb Kimble
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edy/tuition-and-fees

import datetime
# define tuition & fee rates 
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

#create output file
outfile = 'tuition-webpage.html'

##########  define program functions #########

def main():

    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        yesno = input("\nWould you like to calculate tuition & fees for another student ( Y or N )?")
        if yesno == "n" or yesno == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Tuition Webpage </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #b2ac88; background-image: url(wp-tuition.jpeg); color: #013220;">\n')

def get_user_data():
    global inout,numcredits,scholarship_amt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount recieved: "))

def perform_calculations():
    global tuition_amt, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE
    total = tuition_amt + inst_fee + cap_fee + act_fee
    balance = total - scholarship_amt

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today [0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp= '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3" style="background-color: #b2ac88; font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2> TUITION WEBPAGE</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Tuition Costs Report ***\n')

    f.write(tr + 'Tuition'+ endtd + format(tuition_amt,currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + format(cap_fee,currency) + endtr)
    f.write(tr + 'Institutional Fee' + endtd + format(inst_fee,currency)  + endtr)
    f.write(tr + 'Activity Fee' + endtd + format(act_fee,currency)  + endtr)
    f.write(tr + 'Total' + endtd + format(total,currency)  + endtr)
    f.write(tr + 'Balance' + endtd + format(balance,currency)  + endtr)

    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


############# call on main program to execute ##########
main()


    
