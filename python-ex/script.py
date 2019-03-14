#!/usr/bin/env/python3
"""moving files with sftp"""

import os ## allows us to low level agnostic access
import paramiko ## make ssh connection

def main():
    t = paramiko.Transport('10.10.2.3',22) ## connection object IP/port
    t.connect(username='bender', password='alta3')

    sftpobj = paramiko.SFTPClient.from_transport(t)

    sftpobj.put("fake.conf", "fake.move.conf")

    sftpobj.close()

    t.close()
