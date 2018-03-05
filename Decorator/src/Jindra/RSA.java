package Jindra;

import java.security.InvalidKeyException;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;

public class RSA extends Decorator{

   private PrivateKey myPrivateKey;
   private PublicKey myPublicKey;
   private PublicKey hisPublicKey;

   /**
    * Return den generierten public key
    * @since 25-01-2018
    * @return PublicKey
    */
   public PublicKey getMyPublicKey() {
	   return myPublicKey;
   }


   /**
    * Übernimmt den PublicKey, den der Client/Server vorher bekommen haben muss.
    * @since 25-01-2018
    * @param hisPublicKey
    */
	public void setHisPublicKey(PublicKey hisPublicKey) {
	this.hisPublicKey = hisPublicKey;
}



	
	RSA(SocketIf inner, PublicKey hisPublicKey) {
	   super(inner);
	   this.hisPublicKey=hisPublicKey;
	   KeyPairGenerator kpg=null;
		try {
			kpg = KeyPairGenerator.getInstance("RSA");
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
		
		   kpg.initialize(2048);
		   KeyPair kp = kpg.genKeyPair();
		   myPublicKey = kp.getPublic();
		   myPrivateKey = kp.getPrivate();
	}
	
	RSA(SocketIf inner) {
		   super(inner);
		   KeyPairGenerator kpg=null;
			try {
				kpg = KeyPairGenerator.getInstance("RSA");
			} catch (NoSuchAlgorithmException e) {
				e.printStackTrace();
			}
			
			   kpg.initialize(2048);
			   KeyPair kp = kpg.genKeyPair();
			   myPublicKey = kp.getPublic();
			   myPrivateKey = kp.getPrivate();
		}


	/**
	 * Standard Decorator Methode read
	 * @since 25-01-2018
	 */
	public String read() {
	    Cipher cipher = null;
	    String msg = null;
		try {
			cipher = Cipher.getInstance("RSA");
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		} catch (NoSuchPaddingException e) {
			e.printStackTrace();
		}  
	       try {
			cipher.init(Cipher.DECRYPT_MODE, myPrivateKey);
		} catch (InvalidKeyException e) {
			e.printStackTrace();
		}
	       try {
			msg = new String(cipher.doFinal(inner.read().getBytes()));
		} catch (IllegalBlockSizeException e) {
			e.printStackTrace();
		} catch (BadPaddingException e) {
			e.printStackTrace();
		}
       return msg;
   }

	/**
	 * Standard Decorator Methode write
	 * @since 25-01-2018
	 */
   public void write(String msg) {
       
	    Cipher cipher = null;
		try {
			cipher = Cipher.getInstance("RSA");
		} catch (NoSuchAlgorithmException e1) {
			e1.printStackTrace();
		} catch (NoSuchPaddingException e1) {
			e1.printStackTrace();
		}  
	    try {
			cipher.init(Cipher.ENCRYPT_MODE, hisPublicKey);
		} catch (InvalidKeyException e) {
			e.printStackTrace();
		}
	    
	    byte[] bytes = null;
	    
		try {
			bytes = cipher.doFinal(msg.getBytes());
		} catch (IllegalBlockSizeException e) {

			e.printStackTrace();
		} catch (BadPaddingException e) {
			e.printStackTrace();
		}
	    inner.write(new String(bytes));
   }


}
