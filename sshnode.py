#! /bin/python

import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description='Create an SSH session into one of the nodes')
parser.add_argument('port', metavar='p', type=int, nargs='?', default=None,
                   help='Port of rackattack node')
parser.add_argument('local', metavar='l', type=int, nargs='?', default=None,
                   help='When running virtual, the last part of ip of local VM')
args = parser.parse_args()
site = os.environ['RACK_SITE'] if 'RACK_SITE' in os.environ else None
natServer = 'rackattack-nat' if site is None or site != 'bezeq'  else 'rackattack-nat.dc1.strato'

if args.port and args.port != 22:
    host = natServer
    port = args.port
elif args.local:
    host = "192.168.124.%d" % args.local
    port = 22
else:
    host = "192.168.124.11"
    port = 22

print "connecting via %s" % natServer 
cmd = ["sshpass", "-p", "rackattack", "ssh", "-o", "ServerAliveInterval=5",
    "-o", "ServerAliveCountMax=1", "-o", "StrictHostKeyChecking=no", "-o UserKnownHostsFile=/dev/null",
    "-p", str(port), "root@%s" % host]
print "Command is %s"%' '.join(cmd)
subprocess.Popen(cmd).communicate()
