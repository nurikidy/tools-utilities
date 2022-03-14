#
# Tested using Python 3.9.10 on macOS Big Sur 11.6.4
# checking SSL cert expiration days of list of domains
#
from queue import Empty
from urllib.request import ssl, socket
import datetime, smtplib

def get_expiration_days(hostname, port):
    context = ssl.create_default_context()
    days_expiration = 0
    with socket.create_connection((hostname, sslport)) as sock:
        with context.wrap_socket(sock, server_hostname = hostname) as ssock:
            certificate = ssock.getpeercert()
            cert_expires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
            days_expiration = (cert_expires - datetime.datetime.now()).days
    return days_expiration

sslport = '443'
sourcelist = 'hostnames.txt'


with open(sourcelist, 'r') as domains:
    for hostname in domains.read().splitlines():
        if hostname != "":            
            expire = get_expiration_days(hostname, sslport)
            print("%s --- %d days to expire" % (hostname, expire))
