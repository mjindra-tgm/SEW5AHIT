package Jindra;

/**
 * Socket Interface Grundlage des Decorator Patterns
 * @author Michael Jindra
 * @version 25-01-2018
 */
public interface SocketIf {
	public void write(String message);
	public String read();
}
