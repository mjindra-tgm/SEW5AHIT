package Jindra;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class ConcreteServer implements SocketIf{
	private Socket client;
	private ServerSocket server;
	private int port;
	private BufferedReader in;
	private PrintWriter out;
	
	

	@Override
	public void write(String message) {
		try {
			out = new PrintWriter(client.getOutputStream(), true);
		} catch (IOException e) {
			e.printStackTrace();
		}
		out.println(message);
	}
	

	@Override
	public String read() {
		try {
			in = new BufferedReader(new InputStreamReader(client.getInputStream()));
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		String message = null;
		try {
			message = in.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return message;
	}


	public ConcreteServer(int port) throws IOException {
		super();
		server = new ServerSocket(port);
		this.port = port;
		while(true) {
			client = server.accept();
		}

	}
}
