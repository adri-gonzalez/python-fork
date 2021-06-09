# Python code to create child process
import os


def parent_child():
    n = os.fork()

    # n mayor que 0 significa proceso padre
    if n > 0:
        print("Parent process and id is : ", os.getpid())

    # n equals to 0 means child process
    else:
        print("Child process and id is : ", os.getpid())


# Driver code
parent_child()
