import socket
import threading

# Funzione per ricevere messaggi dal server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connessione persa.")
            client_socket.close()
            break

# Funzione principale per avviare il client
def start_client():
    host = input("Inserisci l'indirizzo IP dell'host: ")
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input().strip()
        if message:
            client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
