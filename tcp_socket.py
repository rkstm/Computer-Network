import socket
import threading

# Function to handle file transfer
def handle_file_transfer(client_socket):
    filename = client_socket.recv(1024).decode()  # Receive the filename
    client_socket.send("READY".encode())  # Acknowledge receipt

    with open(filename, 'wb') as f:
        print(f"Receiving file: {filename}")
        while True:
            data = client_socket.recv(1024)
            if data == b"DONE":
                print("File received successfully.")
                break
            f.write(data)

# Function to perform arithmetic calculations
def handle_arithmetic(client_socket):
    while True:
        expression = client_socket.recv(1024).decode()
        if expression.lower() == 'exit':
            break
        try:
            result = eval(expression)
            client_socket.send(f"Result: {result}".encode())
        except Exception as e:
            client_socket.send(f"Error: {e}".encode())

# Server function
def server():
    host = '127.0.0.1'
    port = 5005

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Send hello message to the client
    client_socket.send("Hello, client!".encode())

    while True:
        choice = client_socket.recv(1024).decode()

        if choice == '1':  # Say hello
            client_socket.send("Hello to you too!".encode())

        elif choice == '2':  # File transfer
            handle_file_transfer(client_socket)

        elif choice == '3':  # Arithmetic calculation
            handle_arithmetic(client_socket)

        elif choice.lower() == 'exit':  # Exit the connection
            print("Closing connection...")
            client_socket.close()
            break

# Client function
def client():
    host = '127.0.0.1'
    port = 5005

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive Hello from server
    hello_message = client_socket.recv(1024).decode()
    print(hello_message)

    while True:
        print("\nChoose an option:")
        print("1. Say Hello to the server")
        print("2. Transfer a file to the server")
        print("3. Perform arithmetic calculations")
        print("Type 'exit' to quit the program.")
        
        choice = input("Enter your choice: ")
        client_socket.send(choice.encode())

        if choice == '1':  # Say Hello
            server_message = client_socket.recv(1024).decode()
            print(server_message)

        elif choice == '2':  # File transfer
            filename = input("Enter the filename to send: ")
            client_socket.send(filename.encode())  # Send the filename
            server_ack = client_socket.recv(1024).decode()
            if server_ack == "READY":
                with open(filename, 'rb') as f:
                    while True:
                        data = f.read(1024)
                        if not data:
                            client_socket.send(b"DONE")
                            print(f"File '{filename}' sent successfully.")
                            break
                        client_socket.send(data)

        elif choice == '3':  # Arithmetic calculation
            while True:
                expression = input("Enter arithmetic expression (e.g., 2 + 2) or 'exit' to stop: ")
                client_socket.send(expression.encode())
                if expression.lower() == 'exit':
                    break
                result = client_socket.recv(1024).decode()
                print(result)

        elif choice.lower() == 'exit':  # Exit the program
            client_socket.send("exit".encode())
            print("Exiting...")
            client_socket.close()
            break

# Main function to start the server or client based on user's choice
def main():
    mode = input("Enter 'server' to run as server or 'client' to run as client: ").strip().lower()
    if mode == 'server':
        server_thread = threading.Thread(target=server)
        server_thread.start()
    elif mode == 'client':
        client_thread = threading.Thread(target=client)
        client_thread.start()
    else:
        print("Invalid choice, please enter 'server' or 'client'.")

if __name__ == "__main__":
    main()
