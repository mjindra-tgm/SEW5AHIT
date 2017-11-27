package Jindra;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class ConcreteClient implements SocketIf{
	Socket client;
	
	public ConcreteClient(String hostName, int portNumber) {
		super();
		try {
			client = new Socket(hostName,portNumber);
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	
	@Override
	public void write(String message) {
		PrintWriter pw = null;
		
		try {
			pw = new PrintWriter(client.getOutputStream(), true);
		} catch (IOException e) {
			e.printStackTrace();
		}
		pw.write(message);
	}
	

	@Override
	public String read() {
		BufferedReader in=null;
		String message="Something went wrong. See the StackTrace";
		
		try {
			in = new BufferedReader(new InputStreamReader(client.getInputStream()));
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		try {
			message=in.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return message;
	}

}
