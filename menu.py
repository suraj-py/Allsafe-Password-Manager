import colorama
from colorama import Fore, Back, Style
from tabulate import tabulate
from authentication import addMasterPassword, getHash, getAllsafeUsername
from database_manager import storePassword, getPassword, getUserDetails
from password_generator import password_generator

# Initializing colorama
colorama.init(autoreset=False)

RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

# Start Menu
def allsafe():
    print(CYAN)
    print('-'*30)
    print(' Welcome to Allsafe ')
    print('-'*30)

    print(GREEN)
    print('1 - Press "1" to Log-in')
    print('2 - Press "2" if you dont have an account and want to Create new')
    print(YELLOW)
    user_input = input('Select (1 or 2 ) : ')
    print()
    if(user_input == '1'):
        login()
        print()
    elif(user_input == '2'):
        register()
        print()
    else:
        print(RED +"Something went wrong. Try again")


# Login Function
def login():
    print(CYAN + '* * * * Log In * * * *')
    print(GREEN)
    email_id = input('Please provide your email address : ')
    master_password = input('Enter your master password : ')

    # Checking Enter password with hash password
    result = getHash(email_id, master_password)
    if result == True:
        menu()
    else:
        print('Try again')
        login()


# Register Function
def register():
    print(CYAN +'* * * * Register * * * *')
    print(GREEN)
    email_id = input('Please provide your email address : ')

    # checking wheather the username already exists or not
    while True:
        allsafe_username = input('Please create Allsafe username : ')
        check = getAllsafeUsername(allsafe_username)
        if check:
            print('Username already exists. Please provide new one.')
        else:
            break

    master_password = input('Create a strong master password :')

    # adding detail's to the authentication database
    addMasterPassword(email_id, allsafe_username, master_password)
    login()

# Start Menu
def menu():
    while True:
        print(CYAN)
        print('* * * * Menu * * * *')
        print()
        print('1 - Add new app or site to Allsafe.')
        print('2 - Find password for an app or site. ')
        print('3 - Get list of all apps')
        print('4 - Exit.')
        print()
        choice = input(YELLOW +'Enter choice : ')
        print()
        if choice == '1':
            addPassword()
        elif choice == '2':
            findPassword()
        elif choice == '3':
            findAllApps()
        elif choice == '4':
            exit()
        else:
            print(RED +'Sorry wrong input.')
            exit()

# Adding User detail's and Password to the database
def addPassword():
    print(CYAN +'* * * * Add New App * * * *')
    print(GREEN)
    while True:
        allsafe_username = input('Please provide Allsafe username : ')
        check = getAllsafeUsername(allsafe_username)
        if check:
            break
        else:
            print()
            print('Wrong Allsafe username, Enter the right one.')
    print()
    app_name = input('Please provide the name of the app or site : ')
    print()
    email_id = input('Please provide the email of the app or site : ')
    print()
    user_name = input('Please provide the username of the app or site : ')
    print()
    print('1. Do you want to generate your own password.')
    print('OR')
    print('2. Do you want to generate a strong and safe password with Allsafe.')
    ans = input(YELLOW +'Select (1 or 2) : ')
    print()
    if '1' == ans:
        passwd = input('Provide your password : ')
        # adding app name, username, email, password to password password manager database
        storePassword(allsafe_username, app_name, email_id, user_name, passwd)
        print('Success')
    elif '2' == ans:
        passwd = password_generator()
        storePassword(allsafe_username, app_name, email_id, user_name, passwd)
        print('Your stong and safe password is generated.')
        print()
    else:
        print(RED +'Sorry something went wrong. Try again')
    menu()


# find a particular app password
def findPassword():
    print(CYAN +'* * * * Find App Password * * * *')
    print(GREEN)
    app_name = input('Please provide the app name or site name of which you want to find password : ')
    password = getPassword(app_name) # getting password from the database
    print(f'Your password for {app_name.upper()} is {password} ')

# get all app detail's
def findAllApps():
    print(Fore.CYAN +"* * * * Find All App Names and it's Detail's * * * *")
    print(Fore.GREEN)
    allsafe_username = input('Please provide the Allsafe username : ')
    result = getUserDetails(allsafe_username)
    print(tabulate(result, headers = ['Id',
                                      'Allsafe Username',
                                      'App name',
                                      'Email id',
                                      'Username',
                                      'Password'])
            )

# Running the app
allsafe()
