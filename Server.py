# This is the template code for the CNA337 Final Project
# Dylan McCormack
#Worked with Eric Y, Micheal H and got help from Luma
import os
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        server = os.system("ping -n 4 " + self.server_ip)
        return self.server_ip
