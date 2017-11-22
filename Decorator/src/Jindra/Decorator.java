package Jindra;

public abstract class Decorator implements SocketIf{
	protected SocketIf inner;
	
	public Decorator(SocketIf inner) {
		super();
		this.inner = inner;
	}
	
	public void write(String message) {
	}
	
	public void read() {		
	}
	
}
