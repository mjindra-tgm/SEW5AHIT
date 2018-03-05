package Jindra;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class ConcreteServer extends Thread implements SocketIf {
	private Socket client;
	private ServerSocket server;
	private int port;
	private BufferedReader in;
	private PrintWriter out;
	
	/**
	 * Der konkrete Server
	 * @author Michael Jindra
	 * @version 25-01-2018
	 */
	public ConcreteServer(int port) throws IOException {
		super();
		server = new ServerSocket(port);
		this.port = port;
		client = server.accept();
		

	}
	

	/**
	 * Standard Decorator Methode write
	 * @param message zu sendende Nachricht
	 * @since 25-01-2018
	 */
	public void write(String message) {
		try {
			out = new PrintWriter(client.getOutputStream(), true);
		} catch (IOException e) {
			e.printStackTrace();
		}
		out.println(message);
		
	}
	

	/**
	 * Standard Decorator Methode read
	 * @return message vom Socket
	 * @since 25-01-2018
	 */
	public String read() {
		try {
			in = new BufferedReader(new InputStreamReader(client.getInputStream()));
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		String message=null;
		try {
			message=in.readLine();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return message;
	}

	/**
	 * Main für Server
	 * @since 25-01-2018
	 */
	public static void main(String[] args) {
		int port = 8090; 
		SocketIf server = null;	
		try {
			server = new Caesar(new ConcreteServer(port),2);
		} catch (IOException e) {
			e.printStackTrace();
		}
		server.write("test");
		server.read();
	}

}
