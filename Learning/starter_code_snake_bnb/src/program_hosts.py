from colorama import Fore
from dateutil import parser

from infrastructure.switchlang import switch
import infrastructure.state as state
import services.data_service as svc


def run():
    print(' ****************** Welcome host **************** ')
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('a', log_into_account)
            s.case('l', list_cages)
            s.case('r', register_cage)
            s.case('u', update_availability)
            s.case('v', view_bookings)
            s.case('m', lambda: 'change_mode')
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)

        if action:
            print()

        if s.result == 'change_mode':
            return


def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('Login to your [a]ccount')
    print('[R]egister a cage')
    print('[U]pdate cage availability')
    print('[V]iew your bookings')
    print('[L]ist Cages')
    print('Change [M]ode (guest or host)')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()


def create_account():
    print(' ****************** REGISTER **************** ')
    # TODO: Get name & email
    # TODO: Create account, set as logged in.
    name = input("What is your name ")
    email = input("What is your email ").strip().lower()

    old = svc.find_account_by_email(email)
    if old:
        error_msg(f"Error: Account with same email {email} exists")
        return
    state.active_account = svc.create_account(name, email)
    success_msg(f"Created account with Id {state.active_account.id}")


def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input("What is your email: ").strip().lower()
    old = svc.find_account_by_email(email)
    if not old:
        error_msg(f"Error: Account with email {email} does not exists")
        return
    state.active_account = old
    success_msg("Logged in successfully")


def register_cage():
    print(' ****************** REGISTER CAGE **************** ')

    meters = input("how many meters? ")
    if not meters:
        error_msg("Cancelled")
        return

    meters = float(meters)
    carpeted = input("is Carpeted? (y/n) ").lower().startswith('y')
    has_toys = input("Has Toys? (y/n) ").lower().startswith('y')
    allow_dangerous = input("Allow dangerous snake? (y/n) ").lower().startswith('y')
    name = input("give your cage Name: ")
    price = input("give your cage Price: ")
    price = float(price)

    cage = svc.register_cage(state.active_account,name,allow_dangerous,has_toys,carpeted,meters,price)

    state.reload_account()
    success_msg(f"Cage saved {cage.id}!")


def list_cages(suppress_header=False):
    if not suppress_header:
        print(' ******************     Your cages     **************** ')

    if not state.active_account:
        error_msg("Requires login")
        return

    cages = svc.find_cages_for_account(state.active_account)

    print(f"You have {len(cages)} cages.")
    for idx, c in enumerate(cages):
        print(f' {idx+1}. {c.name} is {c.square_meters} meters.')
        for b in c.bookings:
            print('      * Booking: {}, {} days, booked? {}'.format(
                b.check_in_date,
                (b.check_out_date - b.check_in_date).days,
                'YES' if b.booked_date is not None else 'no'
            ))


def update_availability():
    print(' ****************** Add available date **************** ')

    if not state.active_account:
        error_msg("Requires login")
        return
    list_cages(suppress_header=True)

    cage_number = input("What Cage do you want? ")
    if not cage_number.strip():
        error_msg("Enter valid cage number")
        return
    cage_number = int(cage_number)
    cages = svc.find_cages_for_account(state.active_account)
    selected_cage = cages[cage_number-1]

    start_date = parser.parse(
        input("Enter start date [yyyy-mm-dd]: ")
    )
    days = int(input("how many days? "))
    svc.add_available_date(
        selected_cage,
        start_date,
        days
    )

    state.reload_account()



def view_bookings():
    print(' ****************** Your bookings **************** ')

    # TODO: Require an account
    # TODO: Get cages, and nested bookings as flat list
    # TODO: Print details for each

    print(" -------- NOT IMPLEMENTED -------- ")


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
