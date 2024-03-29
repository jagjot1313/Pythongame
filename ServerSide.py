import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)
print('Server is listening for connections...')

# Accept the first player's connection
player1_socket, player1_address = server_socket.accept()
print('Player 1 connected:', player1_address)

# Notify Player 1 to wait for Player 2
player1_socket.sendall("Waiting for another player to connect...".encode('utf-8'))

# Accept the second player's connection
player2_socket, player2_address = server_socket.accept()
print('Player 2 connected:', player2_address)

# Notify both players that the game is starting
player1_socket.sendall("Both players connected. The game is starting!".encode('utf-8'))
player2_socket.sendall("Both players connected. The game is starting!".encode('utf-8'))

# Receive choices from both players
player1_choice = player1_socket.recv(1024).decode('utf-8')
player2_choice = player2_socket.recv(1024).decode('utf-8')

# Display the choices
print('Player 1 chose:', player1_choice)
print('Player 2 chose:', player2_choice)

# Determine the winner
if player1_choice == player2_choice:
    result = "It's a tie!"
elif (
    (player1_choice == 'rock' and player2_choice == 'scissors') or
    (player1_choice == 'paper' and player2_choice == 'rock') or
    (player1_choice == 'scissors' and player2_choice == 'paper')
):
    result = "Player 1 wins!"
else:
    result = "Player 2 wins!"

# Send the result to both players
player1_socket.sendall(result.encode('utf-8'))
player2_socket.sendall(result.encode('utf-8'))

# Close the connections
player1_socket.close()
player2_socket.close()
server_socket.close()
