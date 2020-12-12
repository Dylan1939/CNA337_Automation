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

# Dylan McCormack CNA 337
# ssh automate
# Worked with Eric Y, Got help from Matthew W, Luma N and Micheal H

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('18.218.16.191', port=22, username='ec2-user', password='', key_filename='id_rsa')

stdin, stdout, stderr = ssh.exec_command('''sudo yum-get update
                                         sudo yum-get upgrade -y
                                         ''')
data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()
