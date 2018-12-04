from __future__ import print_function
import argparse

def _argparse():
    parser = argparse.ArgumentParser(description="A Python-MySQL client")
    parser.add_argument('--host', action='store', dest='server', default="localhost", help='connect to host')
    parser.add_argument('-t', action='store_true', default=False, dest='boolean_switch', help='Set a switch to true')
    parser.add_argument('-u', '--user', action='store', dest='user', required=True, help='user for login')
    parser.add_argument('-p', '--password', action='store', dest='password', required=True, help='password to use when connecting to server')
    parser.add_argument('-P','--port',action='store', dest='port', default='3306', type=int, help='port number to use for connection or 3306 for default')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()

def main():
    """docstring for main"""
    parser = _argparse()
    conn_args = dict(host=parser.host, user=parser.user, password=parser.password, port=parser.port)
    print(conn_args)
    print(parser)
    print('host = ', parser.server)
    print('boolean_switch=', parser.boolean_switch)

if __name__ == '__main__':
    main()
