# Chat Server-Client with Python

This project implements a simple chat system based on TCP sockets using Python. The server manages multiple clients simultaneously and allows users to send messages with automatically assigned colors using the **Colorama** library.

## 🛠 Features
- Supports multiple connected clients.
- Each user has a unique color for their nickname.
- Messages are broadcast to all connected clients.
- The host can view connected users and send messages to the chat.

## 📌 Requirements
- Python 3.x
- `colorama` library (for colored nicknames)

## 🚀 Installation
1. Clone or download this repository.
2. Open a terminal and install the required library:
   ```bash
   pip install colorama
   ```

## 🔧 Usage

### 1️⃣ Start the Server
To run the server, open a terminal in the project folder and execute:
```bash
python server.py
```
The host will start a server on port **5555** and display the IP address it is listening on.

### 2️⃣ Start a Client
On another device or the same machine, run:
```bash
python client.py
```
The client will ask for the server's IP. Enter it to connect to the chat.

## 🔹 Available Commands
| Command  | Description |
|----------|-------------|
| `client` | Displays the list of connected users (host only). |

## 🖥 Chat Example
```
🟡 Host: Welcome to the chat!
🔵 Client 1 joined the chat!
🟢 Client 2 joined the chat!
🔵 Client 1: Hello!
🟢 Client 2: Hi!
🟡 Host: Let's get started.
```

## 📝 Notes
- The server must be started before clients can connect.
- Clients do not see their own messages duplicated.
- The server can send messages to the chat as "Host".

## 📜 License
This project is open-source and can be freely modified.

## 🤝 Contributing
Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.

## ⭐ Star the Project
If you find this project useful or interesting, feel free to give it a ⭐ (star) on GitHub! Your support helps to keep the project alive and encourages future improvements.

[Star the repository here](#)

---

Made with ❤️ by Gecky

