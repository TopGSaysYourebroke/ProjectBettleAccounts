import datetime
import os

# Project Bettle By Joshua Philipsen

# Collects Current Time for call hold specifications
Hold = datetime.datetime.now()
Call = str(Hold)

print("\n" * 30)
print("**************************************************************")
print("WELCOME TO PROJECT BETTLE (ACCOUNTS) - CREATED BY JOSHUA PHILIPSEN")
print("**************************************************************")

phonenumber = input("Please Enter Phone Number : ")
print("\n" * 30)
print("**************************************************************")

fullname = input("Please Enter full name : ")
print("\n" * 30)
print("**************************************************************")
print("Have you Completed an ID Check on the caller ?")
print("(1) ID Check Completed")
print("(2) No ID Checked")
print("**************************************************************")
idcheck = int(input("ID Checked: "))
print("\n" * 30)
print("**************************************************************")

if idcheck == 1:
    idcheck = "Yes"
    print("What Permissions Does the caller have for SkyMesh ?")
    print("(1) Account Holder")
    print("(2) Accounts Owner")
    print("(3) Representative - Spouse")
    print("(4) Representative - Family")
    print("(5) Representative - Other")
    print("(6) Advocate - Technical Only")
    print("**************************************************************")
    Authorization = int(input("Please Enter Authorization: "))
    print("**************************************************************")

    if Authorization == 1:
        Authorization = "Account Holder"
    if Authorization == 2:
        Authorization = "Accounts Owner"
    if Authorization == 3:
        Authorization = "Representative - Spouse"
    if Authorization == 4:
        Authorization = "Representative - Family"
    if Authorization == 5:
        Authorization = "Representative - Other"
    if Authorization == 6:
        Authorization = "Advocate - Technical Only "
if idcheck == 2:
    idcheck = "No"
    Authorization = "None "
print("\n" * 30)
print("**************************************************************")
print("Please Select Call reason:")
print("**************************************************************")
print("(1) Update Account Details")
print("(2) Update Payment method")
print("(3) Pay overdue Account")
print("(4) Rebook Installation Appointment")
print("(5) Review Data Usage and Change Plan")
print("(6) Change Service (LTS > SMP) (SMP > LTS)")
print("(7) Check on sales application")

print("**************************************************************")
callreason = int(input("Please Select a call reason: "))
print("**************************************************************")
print("\n" * 30)
# Call Reasons
if callreason == 1:
    callreason = "Update Account Details"
if callreason == 2:
    callreason = "Update Payment method"
if callreason == 3:
    callreason = "Pay overdue Account"
if callreason == 4:
    callreason = "Rebook Installation Appointment"
if callreason == 5:
    callreason = "Review Data Usage and Change Plan"
if callreason == 6:
    callreason = "Change Service (LTS > SMP) (SMP > LTS)"
if callreason == 7:
    callreason = "Check on sales application"


def callactions():
    print("**************************************************************")
    print("Please Select Actions Taken in Order:")
    print("**************************************************************")
    print("(1) Performed MFA - 2 Step Verification ")
    print("(2) Removed Billing Information ")
    print("(3) Turned Off Call Recording")
    print("(4) Added New Biller Information")
    print("(5) Turned on Call Recording: ")
    print("(6) Advised Customer Owing Balance")
    print("(7) processed manual payment ")
    print("(8) Processed Plan Change")
    print("(9) (press multiple times to skip to after call actions ")

# Open note and write above input
skynoteAC = open("skynoteAC.txt", "w")
skynoteAC.write("\n**************************************************************")
skynoteAC.write("\nPhone Number: " + phonenumber)
skynoteAC.write("\nFull Name: " + fullname)
skynoteAC.write("\nidchecked: " + idcheck)
skynoteAC.write("\nAuthorization: " + Authorization)
skynoteAC.write("\n**************************************************************")
skynoteAC.write("\nReason For Call: " + callreason)
skynoteAC.write("\n**************************************************************")
skynoteAC.write("\nActions Taken ")
skynoteAC.write("\n**************************************************************")
skynoteAC.write("\n")
skynoteAC.close()  # closes skynote.txt text file

# end of input note , does not include actual actions taken

actionstaken0 = ""

# Agent's First Action
print("\n" * 30)
print("**************************************************************")
print("Action One / Ten")
callactions()
actionstaken0 = int(input("Please enter First of Ten Actions: "))
if actionstaken0 == 1:
    actionstaken0 = "Performed MFA - 2 Step Verification"

if actionstaken0 == 2:
    actionstaken0 = "Removed Billing Information"

if actionstaken0 == 3:
    actionstaken0 = "Turned Off Call Recording: " + Call

if actionstaken0 == 4:
    actionstaken0 = "Added New Biller Information"

if actionstaken0 == 5:
    actionstaken0 = "Turned on Call Recording: " + Call

if actionstaken0 == 6:
    actionstaken0 = "Advised Customer Owing Balance"

if actionstaken0 == 7:
    actionstaken0 = "Processed Manual Payment"

if actionstaken0 == 8:
    actionstaken0 = "Processed Plan Change "

if actionstaken0 == 9:
    actionstaken0 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken0)
skynoteAC.close()  # closes skynote.txt text file

# Agent's Second Action
print("\n" * 30)
print("**************************************************************")
print("Action Two / Ten")
callactions()
actionstaken1 = int(input("Please enter Second of Ten Actions: "))
if actionstaken1 == 1:
    actionstaken1 = "Performed MFA - 2 Step Verification"

if actionstaken1 == 2:
    actionstaken1 = "Removed Billing Information"

if actionstaken1 == 3:
    actionstaken1 = "Turned Off Call Recording: " + Call

if actionstaken1 == 4:
    actionstaken1 = "Added New Biller Information"

if actionstaken1 == 5:
    actionstaken1 = "Turned on Call Recording: " + Call

if actionstaken1 == 6:
    actionstaken1 = "Advised Customer Owing Balance"

if actionstaken1 == 7:
    actionstaken1 = "Processed Manual Payment"

if actionstaken1 == 8:
    actionstaken1 = "Processed Plan Change "

if actionstaken1 == 9:
    actionstaken1 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken1)
skynoteAC.close()  # closes skynoteAC.txt text file

# Agent's Third Action
print("\n" * 30)
print("**************************************************************")
print("Action Three / Ten")
callactions()
actionstaken2 = int(input("Please enter Third of Ten Actions: "))
if actionstaken2 == 1:
    actionstaken2 = "Performed MFA - 2 Step Verification"

if actionstaken2 == 2:
    actionstaken2 = "Removed Billing Information"

if actionstaken2 == 3:
    actionstaken2 = "Turned Off Call Recording: " + Call

if actionstaken2 == 4:
    actionstaken2 = "Added New Biller Information"

if actionstaken2 == 5:
    actionstaken2 = "Turned on Call Recording: " + Call

if actionstaken2 == 6:
    actionstaken2 = "Advised Customer Owing Balance"

if actionstaken2 == 7:
    actionstaken2 = "Processed Manual Payment"

if actionstaken2 == 8:
    actionstaken2 = "Processed Plan Change "

if actionstaken2 == 9:
    actionstaken2 = ""


skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken2)
skynoteAC.close()  # closes skynoteAC.txt text file


# Agent's Fourth Action
print("\n" * 30)
print("**************************************************************")
print("Action Four / Ten")
callactions()
actionstaken3 = int(input("Please enter Fourth of Ten Actions: "))
if actionstaken3 == 1:
    actionstaken3 = "Performed MFA - 2 Step Verification"

if actionstaken3 == 2:
    actionstaken3 = "Removed Billing Information"

if actionstaken3 == 3:
    actionstaken3 = "Turned Off Call Recording: " + Call

if actionstaken3 == 4:
    actionstaken3 = "Added New Biller Information"

if actionstaken3 == 5:
    actionstaken3 = "Turned on Call Recording: " + Call

if actionstaken3 == 6:
    actionstaken3 = "Advised Customer Owing Balance"

if actionstaken3 == 7:
    actionstaken3 = "Processed Manual Payment"

if actionstaken3 == 8:
    actionstaken3 = "Processed Plan Change "

if actionstaken3 == 9:
    actionstaken3 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken3)
skynoteAC.close()  # closes skynoteAC.txt text file

# Agent's Fifth Action
print("\n" * 30)
print("**************************************************************")
print("Action Five / Ten")
callactions()
actionstaken4 = int(input("Please enter Fifth of Ten Actions: "))
if actionstaken4 == 1:
    actionstaken4 = "Performed MFA - 2 Step Verification"

if actionstaken4 == 2:
    actionstaken4 = "Removed Billing Information"

if actionstaken4 == 3:
    actionstaken4 = "Turned Off Call Recording: " + Call

if actionstaken4 == 4:
    actionstaken4 = "Added New Biller Information"

if actionstaken4 == 5:
    actionstaken4 = "Turned on Call Recording: " + Call

if actionstaken4 == 6:
    actionstaken4 = "Advised Customer Owing Balance"

if actionstaken4 == 7:
    actionstaken4 = "Processed Manual Payment"

if actionstaken4 == 8:
    actionstaken4 = "Processed Plan Change "

if actionstaken4 == 9:
    actionstaken4 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken3)
skynoteAC.close()  # closes skynoteAC.txt text file


# Agent's Sixth Action
print("\n" * 30)
print("**************************************************************")
print("Action Six / Ten")
callactions()
actionstaken5 = int(input("Please enter Sixth of Ten Actions: "))
if actionstaken5 == 1:
    actionstaken5 = "Performed MFA - 2 Step Verification"

if actionstaken5 == 2:
    actionstaken5 = "Removed Billing Information"

if actionstaken5 == 3:
    actionstaken5 = "Turned Off Call Recording: " + Call

if actionstaken5 == 4:
    actionstaken5 = "Added New Biller Information"

if actionstaken5 == 5:
    actionstaken5 = "Turned on Call Recording: " + Call

if actionstaken5 == 6:
    actionstaken5 = "Advised Customer Owing Balance"

if actionstaken5 == 7:
    actionstaken5 = "Processed Manual Payment"

if actionstaken5 == 8:
    actionstaken5 = "Processed Plan Change "

if actionstaken5 == 9:
    actionstaken5 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken4)
skynoteAC.close()  # closes skynoteAC.txt text file


# Agent's Seventh Action
print("\n" * 30)
print("**************************************************************")
print("Action Seven / Ten")
callactions()
actionstaken6 = int(input("Please enter Seventh of Ten Actions: "))
if actionstaken6 == 1:
    actionstaken6 = "Performed MFA - 2 Step Verification"

if actionstaken6 == 2:
    actionstaken6 = "Removed Billing Information"

if actionstaken6 == 3:
    actionstaken6 = "Turned Off Call Recording: " + Call

if actionstaken6 == 4:
    actionstaken6 = "Added New Biller Information"

if actionstaken6 == 5:
    actionstaken6 = "Turned on Call Recording: " + Call

if actionstaken6 == 6:
    actionstaken6 = "Advised Customer Owing Balance"

if actionstaken6 == 7:
    actionstaken6 = "Processed Manual Payment"

if actionstaken6 == 8:
    actionstaken6 = "Processed Plan Change "

if actionstaken6 == 9:
    actionstaken6 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken5)
skynoteAC.close()  # closes skynoteAC.txt text file



# Agent's Eighth Action
print("\n" * 30)
print("**************************************************************")
print("Action Eight / Ten")
callactions()
actionstaken7 = int(input("Please enter Eighth of Ten Actions: "))
if actionstaken7 == 1:
    actionstaken7 = "Performed MFA - 2 Step Verification"

if actionstaken7 == 2:
    actionstaken7 = "Removed Billing Information"

if actionstaken7 == 3:
    actionstaken7 = "Turned Off Call Recording: " + Call

if actionstaken7 == 4:
    actionstaken7 = "Added New Biller Information"

if actionstaken7 == 5:
    actionstaken7 = "Turned on Call Recording: " + Call

if actionstaken7 == 6:
    actionstaken7 = "Advised Customer Owing Balance"

if actionstaken7 == 7:
    actionstaken7 = "Processed Manual Payment"

if actionstaken7 == 8:
    actionstaken7 = "Processed Plan Change "

if actionstaken7 == 9:
    actionstaken7 = ""


skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken6)
skynoteAC.close()  # closes skynoteAC.txt text file

# Agent's Ninth Action
print("\n" * 30)
print("**************************************************************")
print("Action Nine / Ten")
callactions()
actionstaken8 = int(input("Please enter Ninth of Ten Actions: "))
if actionstaken8 == 1:
    actionstaken8 = "Performed MFA - 2 Step Verification"

if actionstaken8 == 2:
    actionstaken8 = "Removed Billing Information"

if actionstaken8 == 3:
    actionstaken8 = "Turned Off Call Recording: " + Call

if actionstaken8 == 4:
    actionstaken8 = "Added New Biller Information"

if actionstaken8 == 5:
    actionstaken8 = "Turned on Call Recording: " + Call

if actionstaken8 == 6:
    actionstaken8 = "Advised Customer Owing Balance"

if actionstaken8 == 7:
    actionstaken8 = "Processed Manual Payment"

if actionstaken8 == 8:
    actionstaken8 = "Processed Plan Change "

if actionstaken8 == 9:
    actionstaken8 = ""


skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken7)
skynoteAC.close()  # closes skynoteAC.txt text file



# Agent's Tenth Action
print("\n" * 30)
print("**************************************************************")
print("Action Ten / Ten")
callactions()
actionstaken9 = int(input("Please enter Tenth of Ten Actions: "))
if actionstaken9 == 1:
    actionstaken9 = "Performed MFA - 2 Step Verification"

if actionstaken9 == 2:
    actionstaken9 = "Removed Billing Information"

if actionstaken9 == 3:
    actionstaken9 = "Turned Off Call Recording: " + Call

if actionstaken9 == 4:
    actionstaken9 = "Added New Biller Information"

if actionstaken9 == 5:
    actionstaken9 = "Turned on Call Recording: " + Call

if actionstaken9 == 6:
    actionstaken9 = "Advised Customer Owing Balance"

if actionstaken9 == 7:
    actionstaken9 = "Processed Manual Payment"

if actionstaken9 == 8:
    actionstaken9 = "Processed Plan Change "

if actionstaken9 == 9:
    actionstaken9 = ""

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n")
skynoteAC.write(actionstaken8)
skynoteAC.close()  # closes skynoteAC.txt text file

print("\n" * 30)
print("**************************************************************")
print("Please Select After Call Action - one only")
print("(1) EOC - Customer Happy - Resolving Ticket")
print("(2) EOC - Emailing Customer - Stalling Ticket")
print("(3) EOC - Assistance Required - Stalling Ticket")
print("(4) EOC - Additional Work Required For Customer - Stalling Ticket")
print("(5) D&D")

aftercall = int(input("Please Now Select Your After Call Chosen Action: "))
if aftercall == 1:
    aftercall = "EOC - Customer Happy - Resolving Ticket"
if aftercall == 2:
    aftercall = "EOC - Emailing Customer - Stalling Ticket"
if aftercall == 3:
    aftercall = "EOC -Assistance Required - Stalling Ticket"
if aftercall == 4:
    aftercall = "EOC - Additional Work Required For Customer - Stalling Ticket"
if aftercall == 5:
    aftercall = "EOC -Dungeons & Dragons"

print("Creating File")

skynoteAC = open("skynoteAC.txt", "a")
skynoteAC.write("\n**************************************************************")
skynoteAC.write("\nAfter Call Actions ")
skynoteAC.write("\n**************************************************************")
skynoteAC.write("\n")
skynoteAC.write(aftercall)
skynoteAC.close()  # closes skynote.txt text file

os.system('cmd /k "start skynoteAC.txt"')  # opens txt file
exit()
