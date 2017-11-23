package Jindra;

import java.io.IOException;
import java.net.UnknownHostException;

public class Main {

	public static void main(String[] args) {
		int port = 12345;
		ConcreteClient client1 = null;
		ConcreteServer server = null;
		try {
			server = new ConcreteServer(port);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		client1 = new ConcreteClient("localhost", port);
		
		client1.write("Hello");
		System.out.println(server.read());
	}

}
