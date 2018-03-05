package Jindra;

import java.io.FileWriter;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketAddress;
import java.util.HashMap;

/**
 * Der Main Server der die Connections annimmt, an Threads weitergibt und die Credits in einer Collection verwaltet.
 * @author Michael Jindra
 * @version 16-02-2018
 */
public class Server {
	static HashMap<String, Integer> credits = new HashMap<String, Integer>();
	
	/**
	 * Connections werden angenommen und an Threads weitergegeben.
	 * @param args
	 * @since 16-02-2018
	 */
	public static void main(String[] args) {
		ServerSocket s = null;
		try {
			s = new ServerSocket(12345);
		} catch (IOException e) {
			e.printStackTrace();
		}
		while(true) {
			try {
				Socket c = s.accept();
				synchronized (c) {
					if(!credits.containsKey(c.getInetAddress().toString())) {
						credits.put(c.toString(),10);

					}
				}
				ServerThread st = new ServerThread(c);
				st.start();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	/**
	 * Reduziert die Anzahl der Credits um 1(Aktion wird "bezahlt")
	 * @param ip Die IP des Clients, dessen Credits reduziert werden
	 * @since 16-02-2018
	 */
	public static void subcredits(String ip) {
		synchronized (credits) {
			credits.replace(ip, credits.get(ip)-1);
		}
	}
	
	/**
	 * Erhöht die Anzahl der Credits(Credits werden gekauft)
	 * @param ip Die IP des Clients, dessen Credits erhöht werden.
	 * @param anzahl Anzahl der Credits die "gekauft" wurden
	 * @since 16-02-2018
	 */
	public static void addcredits(String ip, int anzahl) {
		synchronized (credits) {
			credits.replace(ip, credits.get(ip)+anzahl);
		}
	}
	
	/**
	 * Gibt die Anzahl an Credits zurück
	 * @param ip Die IP des Clients, dessen Credits zurückgegeben werden
	 * @return Anzahl der verfügbaren Credits
	 * @since 16-02-2018
	 */
	public static int getcredits(String ip) {
		synchronized (credits) {
			return credits.get(ip);
		}
	}
	
}
