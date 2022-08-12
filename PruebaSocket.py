import socket

SERVER_ADDRESS = '192.168.88.128'
import socket

SERVER_ADDRESS = '192.168.88.128'

SERVER_PORT = 55555

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((SERVER_ADDRESS, SERVER_PORT))

s.listen(5)

print("Escuchando en la dirección %s. Detenga el servidor con Ctrl-C" %
str((SERVER_ADDRESS, SERVER_PORT)))

while True:
    c, addr = s.accept()
    print("\nConexion recibida desde %s" % str(addr))

    while True:
        data = c.recv(2048)
        if not data:
            print("Fin de trasmision desde el cliente. Reiniciando")
            break


        data = data.decode()

        print("Inormacion recibida '%s' desde el cliente" % data)

        data = "Hola, " + str(addr) + ". Tu me enviaste esto: '" + data + "'"

        data = data.encode()

        c.send(data)

c.close()


SERVER_PORT = 22222

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((SERVER_ADDRESS, SERVER_PORT))

s.listen(5)

print("Escuchando en la dirección %s. Detenga el servidor con Ctrl-C" %
str((SERVER_ADDRESS, SERVER_PORT)))

while True:
    c, addr = s.accept()
    print("\nConexion recibida desde %s" % str(addr))

    while True:
        data = c.recv(2048)
        if not data:
            print("Fin de trasmision desde el cliente. Reiniciando")
            break

        data = data.decode()

        print("Inormacion recibida '%s' desde el cliente" % data)

        data = "Hola, " + str(addr) + ". Tu me enviaste esto: '" + data + "'"

        data = data.encode()

        c.send(data)

c.close()