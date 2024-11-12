import socket
import os

def udp_server():
    host = '127.0.0.1'
    port = 5005
    buffer_size = 1024
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server started at {host}:{port}")
    
    while True:
        data, client_address = server_socket.recvfrom(buffer_size)
        file_type = data.decode()
        
        if file_type.lower() == "exit":
            print("Client has exited. Stopping Server.")
            break
        
        print(f"Receiving a {file_type} file from {client_address}...")
        
        filename = f"received_{file_type}"
        
        with open(filename, 'wb') as file:
            while True:
                data, client_address = server_socket.recvfrom(buffer_size)
                if data == b"DONE":
                    break
                file.write(data)
        print(f"{file_type} file received successfully.")
    
    server_socket.close()

def udp_client():
    host = '127.0.0.1'
    port = 5005
    buffer_size = 1024
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        file_path = input("\nEnter the file path to send (or type 'exit' to quit): ")
        
        if file_path.lower() == 'exit':
            client_socket.sendto("exit".encode(), (host, port))
            print("Exiting...")
            break
        
        file_type = input("Enter file type (script/text/audio/video): ")
        
        if not os.path.exists(file_path):
            print(f"File {file_path} not found!")
            continue
        
        client_socket.sendto(file_type.encode(), (host, port))
        with open(file_path, 'rb') as file:
            print(f"Sending {file_type} file.")
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                client_socket.sendto(data, (host, port))
                
        client_socket.sendto(b"DONE", (host, port))
        print(f"{file_type} file sent successfully.")
    
    client_socket.close()

def main():
    mode = input("Enter 'server' to run as server or 'client' to run as client: ")
    
    if mode.lower() == 'server':
        udp_server()
    elif mode.lower() == 'client':
        udp_client()
    else:
        print("Invalid choice! Please enter 'server' or 'client'.")

if __name__ == "__main__":
    main()