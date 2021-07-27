import os
import random
import datetime
from time import sleep


def bank():
    print(f'Welcome to the Bank of ABC')
    sleep(1.0)
    print(f'Its easy to change for those who you love,Together we can')
    sleep(1.0)
    print(f'Let\'s build a better life for you')
    sleep(1.0)
    print(f'And be the part of better world')
    sleep(1.0)
    costumer = ['no match' , 'abc' , 'xyz']
    pas = 'pass@123'
    name = input('Name: ')
    paswd = input('Password: ')
    if name in costumer and paswd == pas:
        print('Enjoy your banking experience with world\'s best bank')
        print('For Checking your Balance Press 1\nFor Deposite Press 2\nFor Withdrawl Press 3')
        Choice = int(input('Enter Your Choice: '))
        if Choice < 4:
            Username = input('Enter Your Username: ')
            Password = input('Enter Password: ')
        else:
            print(f'Please enter valid choice')
        CurrentBalance = random.randint(100, 100000)
        try:
            if Choice == 1:
                dt = datetime.datetime.now()
                print(f'Your current balance is: {CurrentBalance}')
                if Username == name and Password == paswd:
                    if not os.path.exists(f'{Username}Log.txt'):
                        with open(f'{Username}Log.txt' , 'wt') as f:
                            f.write(f'\nLogged in at: {dt}\nAnd {Username}\'s current balance is: {CurrentBalance}\n')
                    else:
                        with open(f'{Username}Log.txt' , 'at') as f:
                            f.write(f'\nLogged in at: {dt}\nAnd {Username}\'s Balance is:{CurrentBalance} \n ')
                else:
                    print(f'Username or Password is incorrect\nCheck your Credentials')
            elif Choice == 2:
                if Username == name and Password == paswd:
                    dt = datetime.datetime.now()
                    try:
                        increment = int(input('Enter the amount you want to deposite: '))
                    except Exception:
                        print(f'Enter valid amount please')
                    print(f'Your current balance is: {CurrentBalance+increment}')
                    if not os.path.exists(f'{Username}Log.txt'):
                        with open(f'{Username}Log.txt' , 'wt') as f:
                            f.write(f'\nLogged in at: {dt}\nAnd {Username}\'s balance after deposit is: {CurrentBalance+increment}\n ')
                    else:
                        with open(f'{Username}Log.txt' , 'at') as f:
                            f.write(f'\nLogged in at: {dt}\nAnd {Username}\'s balance after deposit is: {CurrentBalance+increment}\n')
                else:
                    print(f'Username or Password is incorrect\nCheck your Credentials')
            elif Choice == 3:
                if Username == name and Password == paswd:
                    dt = datetime.datetime.now()
                    try:
                        decrement = int(input('Enter the amount you want to withdrawl: '))
                    except Exception:
                        print(f'Enter valid amount please.')
                    print(f'Your current balance is: {CurrentBalance-decrement}')
                    if not os.path.exists(f'{Username}Log.txt'):
                        with open(f'{Username}Log.txt','wt') as f:
                            f.write(f'\nLogged in at: {dt}\nAnd {Username}\'s balance after withdrawl is: {CurrentBalance-decrement}\n')
                    else:
                        with open(f'{Username}Log.txt','at') as f:
                            f.write(f'\nLogged in at: {dt}\nAnd {Username}\'s balance after withdrawl is: {CurrentBalance-decrement}\n')
                else:
                    print(f'Username or Password is incorrect\nCheck your Credentials')
            else:
                print('This process can not be processed.')
        except Exception as e:
            print(f'There seems to be some problem.\n{e}')
    else:
        print(f'There seems to be some problem with your credentials\nPlease check your credential and try again')

if __name__ == '__main__':
    bank()