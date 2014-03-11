import paramiko, sys
from forward import forward_tunnel

remote_host = "eblackboard-193040.mysql.binero.se"
remote_port = 3306
local_port  = 3306
ssh_host    = "ssh.binero.se"
ssh_port    = 22

user     = "193040_raspuser"
password = "3'kj}/rT[HM[XEp"

transport = paramiko.Transport((ssh_host, ssh_port))

# Command for paramiko-1.7.7.1
transport.connect(hostkey  = None,
                  username = user,
                  password = password,
                  pkey     = None)

try:
	print("trying to create tunnel")
	forward_tunnel(local_port, remote_host, remote_port, transport)
	print("tunnel created")
except KeyboardInterrupt:
    print 'Port forwarding stopped.'
    sys.exit(0)
