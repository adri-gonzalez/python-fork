########################################
#          Concurrent server           #
########################################

import os
import socket
import time
import signal
import errno

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def grim_reaper(signum, frame):
    pid, status = os.wait()
    print(
        'Child {pid} teminated with status {status}\n'.format(
            pid=pid,
            status=status
        )
    )


def handle_request(client_connection):
    print('##### HANDLE REQUEST #####')
    request = client_connection.recv(1024)
    print(
        'Child PID: {pid}. Parent PID {ppid}'.format(
            pid=os.getpid(),
            ppid=os.getppid()
        )
    )

    print(request.decode())
    http_response = b"""
        HTTP/1.1 200 OK
    
        Hello, World!
    """

    client_connection.sendall(http_response)
    time.sleep(3)


def server_forever():
    print('##### SERVER FOR EVER #####')
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)

    print('Serveing HTTP on address {address} ...'.format(address=SERVER_ADDRESS))
    print('Serveing HTTP on port {port} ...'.format(port=PORT))
    print('Parent PID (PPID): {pid}\n'.format(pid=os.getpid()))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            if code == errno.EINTR:
                continue
            else:
                raise
        pid = os.fork()

        if pid == 0:  # clild
            listen_socket.close()
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:
            client_connection.close()


if __name__ == '__main__':
    server_forever()
