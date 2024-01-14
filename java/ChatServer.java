import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

class ChatServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(9000);
            System.out.println("Server waiting for connection on port 9000...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Connection established with client.");

            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

            BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));

            String clientMessage;
            String serverMessage;

            while (true) {
                System.out.print("Server: ");
                serverMessage = consoleInput.readLine(); //read from keyboard

                out.println(serverMessage); //write these message to client

                //if server say 'bye', then the con will be closed
                if (serverMessage.equalsIgnoreCase("bye")) {
                    break;
                }
                //not bye?
                //read client meessage and print in server console
                clientMessage = in.readLine();
                System.out.println("Client: " + clientMessage);

                //if client say 'bye', then the con will be closed
                if (clientMessage.equalsIgnoreCase("bye")) {
                    break;
                }
            }

            serverSocket.close();
            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


