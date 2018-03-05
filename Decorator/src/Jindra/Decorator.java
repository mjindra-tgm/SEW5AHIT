package Jindra;

/**
 * Die Superklasse aller Dekoratoren
 * @author Michael Jindra
 * @version 25-01-2018
 */
public abstract class Decorator implements SocketIf{
	protected SocketIf inner;
	
	/**
	 * Konstruktor
	 * @param inner
	 */
	public Decorator(SocketIf inner) {
		super();
		this.inner = inner;
	}
	
	public void write(String message) {
	}
	
	public String read() {
		return null;		
	}
	
}
