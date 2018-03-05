package Jindra;

/**
 * Die Caesar Verschlüsselung
 * @author Michael Jindra
 * @version 25-01-2018
 */
public class Caesar extends Decorator{

	private int offset;

	/**
	 * Konstruktor
	 * @param inner
	 * @param offset Caesar Verschiebungsparameter
	 */
	public Caesar(SocketIf inner,int offset) {
		super(inner);
		this.offset = offset;
	}
	
	/**
	 * Standard Write Methode mit Caesar Verschlüsselung
	 * @since 25-01-2017
	 * @param message Nachricht
	 */
	public void write(String message) {
		String crypted = "";
		for(int i=0;i<message.length();i++){
			crypted = crypted + (char)((int)message.charAt(i)+offset);
		}
		inner.write(crypted);
	}
	
	/**
	 * Standard Read Methode mit Caesar Entschlüsselung
	 * @since 25-01-2017
	 * @return Nachricht
	 */
	public String read() {
		String message=inner.read();
		String decrypted = "";
		for(int i=0;i<message.length();i++){
			decrypted = decrypted + (char)((int)message.charAt(i)-offset);
		}		
		return decrypted;
	}

}
