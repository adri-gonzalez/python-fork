import sys
import os

print("Process id antes de forking: {}".format(os.getpid()))

forks = 3
if len(sys.argv) == 2:
    forks = int(sys.argv[1])

for i in range(forks):
    try:
        pid = os.fork()
    except OSError:
        sys.stderr.write("no se pudo crear el child process\n")
        continue

    if pid == 0:
        print("El child process {} tiene el process ID {}".format(i + 1, os.getpid()))
        exit()
    else:
        print("en el proceso padre despues de forking el proceso hijo {}".format(pid))

print("dentro del proceso padre desps de forkear {} los hijos".format(forks))

for i in range(forks):
    finished = os.waitpid(0, 0)
    print(finished)
