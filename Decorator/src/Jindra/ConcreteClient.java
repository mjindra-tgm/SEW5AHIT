package Jindra;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
/**
 * Der konkrete Client
 * @author Michael Jindra
 * @version 25-01-2018
 */
public class ConcreteClient implements SocketIf{
	Socket client;
	private PrintWriter pw = null;
	private BufferedReader in=null;
	
	/**
	 * Der Konstruktor
	 * @param hostName IP/DNS des Servers
	 * @param portNumber selbsterklärend
	 * @since 25-01-2018
	 */
	public ConcreteClient(String hostName, int portNumber) {
		super();
		
		try {
			client = new Socket(hostName,portNumber);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		try {
			pw = new PrintWriter(client.getOutputStream(), true);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		try {
			in = new BufferedReader(new InputStreamReader(client.getInputStream()));
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	
	/**
	 * Standard Decorator Methode write
	 * @param message zu sendende Nachricht
	 * @since 25-01-2018
	 */
	@Override
	public void write(String message) {
		pw.write(message);
	}
	

	/**
	 * Standard Decorator Methode read
	 * @since 25-01-2018
	 */
	@Override
	public String read() {
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
	 * Main
	 * @since 25-01-2018
	 */
	public static void main(String[] args) {
		int port = 8090;
		SocketIf client1 = null;
		ConcreteClient client = new ConcreteClient("localhost", port);
		client1 = new Caesar(client,2);
		System.out.println(client1.read());
	}

}
