# This is the template code for the CNA337 Final Project
# Dylan McCormack
#Worked with Eric Y, Micheal H and got help from Luma
# CNA 337 Fall 2020
from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Dylan")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    DylanLaunchWizard27 = Server('18.218.16.191')
    # TODO - Call Ping method and print the results
    print(DylanLaunchWizard27.ping())
