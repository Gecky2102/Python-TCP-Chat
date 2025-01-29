import socket
import threading
from colorama import Fore, Style, init

# Inizializza Colorama per la compatibilità cross-platform
init(autoreset=True)

# Colori disponibili per i nickname
COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
    Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
]

# Dizionario per memorizzare i client connessi: {nickname: (connection, address)}
clients = {}

# Funzione per gestire i client
def handle_client(conn, addr):
    try:
        # Richiedi il nickname al client
        conn.send("Inserisci il tuo nickname: ".encode('utf-8'))
        nickname = conn.recv(1024).decode('utf-8').strip()

        # Controlla se il nickname è già in uso
        while nickname in clients:
            conn.send("Nickname già in uso. Scegline un altro: ".encode('utf-8'))
            nickname = conn.recv(1024).decode('utf-8').strip()

        # Assegna un colore al nickname
        color = COLORS[len(clients) % len(COLORS)]
        clients[nickname] = (conn, addr, color)

        # Notifica a tutti i client che un nuovo utente si è unito
        broadcast(f"{color}{nickname}{Style.RESET_ALL} si è unito alla chat!", sender="Server")

        while True:
            message = conn.recv(1024).decode('utf-8').strip()
            if not message:
                continue

            if message.startswith("info "):
                target_nickname = message[5:].strip()
                if target_nickname in clients:
                    target_conn, target_addr, _ = clients[target_nickname]
                    conn.send(f"L'indirizzo IP di {target_nickname} è {target_addr[0]}".encode('utf-8'))
                else:
                    conn.send(f"Utente {target_nickname} non trovato.".encode('utf-8'))
            else:
                # Invia il messaggio a tutti i client tranne chi lo ha inviato
                broadcast(f"{color}{nickname}{Style.RESET_ALL}: {message}", sender=nickname)
    except:
        if nickname in clients:
            del clients[nickname]
            broadcast(f"{color}{nickname}{Style.RESET_ALL} ha lasciato la chat.", sender="Server")
        conn.close()

# Funzione per inviare messaggi a tutti i client
def broadcast(message, sender=None):
    if sender != "Server":  
        print(message)

    for nickname, (conn, addr, color) in clients.items():
        try:
            conn.send(message.encode('utf-8'))
        except:
            pass

# Funzione per mostrare i client connessi
def show_clients():
    if not clients:
        print("Nessun client connesso.")
    else:
        print("Client connessi:")
        for nickname, (_, addr, color) in clients.items():
            print(f"{color}- {nickname} ({addr[0]}){Style.RESET_ALL}")

# Funzione principale per avviare il server
def start_host():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()

    print(f"Host avviato su {Fore.CYAN}{ip}:{port}{Style.RESET_ALL}")

    def accept_clients():
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

    def host_commands():
        while True:
            command = input().strip()
            if command == "client":
                show_clients()
            elif command:
                broadcast(f"{Fore.WHITE}{Style.BRIGHT}Host:{Style.RESET_ALL} {command}", sender="Server")

    threading.Thread(target=accept_clients, daemon=True).start()
    threading.Thread(target=host_commands, daemon=True).start()

    while True:
        pass

if __name__ == "__main__":
    start_host()
