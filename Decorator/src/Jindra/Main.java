package Jindra;

import java.io.IOException;
import java.net.UnknownHostException;

public class Main {

	public static void main(String[] args) {
		testRSA();
	}
	
	public static void testCaesar(){
		String text = "random";
		SocketIf ct = new Caesar(new ConcreteTest(),3);
		System.out.println(text);
		ct.write(text);
		System.out.println(ct.read());
	}
	
	public static void testRSA(){
		RSA si1 = new RSA(new ConcreteTest());
		si1.setHisPublicKey(si1.getMyPublicKey());
		
		si1.write("Hola");
		System.out.println(si1.read());
	}
	
	public static void testSocket(){
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
