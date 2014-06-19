import socket
from mpi4py import MPI

try:
    from tools.serial import get_pattern
except ImportError:
    "el nodo con ip" + socket.gethostbyname(socket.gethostname()) +"y rank "+str(MPI.COMM_WORLD.rank)+ "no reconoce las librerias" 