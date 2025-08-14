import os # Import the os module for interacting with the file system
import socket # Provides low-level networking interfaces. It allows you to create and manage network connections using protocols like TCP and UDP.
import termcolor # Enables developers to print colored text, highlight text with different background colors, and apply various text attributes like bold, underline, dark, blink, reverse, and concealed.

def target(host):
    try:
        resolved_ip = socket.gethostbyname(host.strip())  # Resolves domain or confirms IP
        print(f'Resolved {host} to {resolved_ip}')
        port_scan(resolved_ip)
    except socket.error:
        print('Invalid IPv4 address.')
    except KeyboardInterrupt:
        print(termcolor.colored('\nScan cancelled.', 'yellow'))

def port_scan(target_scan):
    print(termcolor.colored(f'Starting full port scan on {target_scan}', 'light_blue'))

    for port in range(0, 65536):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) # Set the timeout for socket operations to 5 seconds
            s.connect((target_scan, port))
            print(termcolor.colored(f'[+] Port {port} is OPEN on {target_scan}', 'green'))
            s.close()
        except socket.error:
            pass  # Silently ignore closed/filtered ports
        except KeyboardInterrupt:
            print(termcolor.colored('\nScan cancelled by user.', 'yellow'))
            break

try:
    while True:
        targets_input = input('Please enter your target(s) (separate with commas): ')
        targets = targets_input.split(',')

        for t in targets:
            target(t.strip())  # strip() removes extra spaces

except OSError:
    print('Something is wrong! please check your command again.')
    raise OSError
except socket.error:
    print('Sorry, I\'m not able to connect to the target')