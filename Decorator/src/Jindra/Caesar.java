package Jindra;

public class Caesar extends Decorator{

	private int offset;

	public Caesar(SocketIf inner,int offset) {
		super(inner);
		this.offset = offset;
	}
	
	public void write(String message) {
		String crypted = "";
		for(int i=0;i<message.length();i++){
			crypted = crypted + (char)((int)message.charAt(i)+offset);
		}
		inner.write(crypted);
	}
	
	public String read() {
		String message=inner.read();
		String decrypted = "";
		for(int i=0;i<message.length();i++){
			decrypted = decrypted + (char)((int)message.charAt(i)-offset);
		}		
		return decrypted;
	}

}
