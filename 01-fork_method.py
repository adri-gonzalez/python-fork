# Python program to explain os.fork() method

# importing os module
import os

# Crear un proceso hijo
# usando el método os.fork ()
pid = os.fork()

# pid mayor que 0 representa
# el proceso padre
if pid > 0:
    print("I am parent process:")
    print("Process ID:", os.getpid())
    print("Child's process ID:", pid)

# pid igual a 0 representaciones
# el proceso hijo creado
else:
    print("\nI am child process:")
    print("Process ID:", os.getpid())
    print("Parent's process ID:", os.getppid())

# Si se produjo algún error mientras
# usando el método os.fork ()
# Se generará OSError
