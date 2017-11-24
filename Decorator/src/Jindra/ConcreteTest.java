package Jindra;

public class ConcreteTest implements SocketIf{
	String message;
	

	public void write(String message) {
		System.out.println(message);
		this.message = message;
	}
	
	public String read() {
		return this.message;		
	}
	
}
