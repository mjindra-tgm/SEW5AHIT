package Jindra;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * Einfacher Frage-Antwort Client
 * @author Walter Raffeiner-Magor, Michael Jindra
 * @version 16-02-2018
 */
public class CalculatorClient {
	private String ip;
	private int port;

	/**
	 * Konstruktor
	 * @param ip, IP des Servers
	 * @param port, Port des Servers
	 * @since 16-02-2018
	 */
	public CalculatorClient(String ip, int port) {
		this.ip = ip;
		this.port = port;
	}

	/**
	 * Baut Verbindung zum Server auf und wartet auf Eingaben des Benutzers, um sie an den Server weiterzuleiten.
	 * @since 16-02-2018
	 */
	public void connect() {
		try (Socket socket = new Socket(ip, port);
				PrintWriter out = new PrintWriter(socket.getOutputStream(),
						true);
				BufferedReader in = new BufferedReader(new InputStreamReader(
						socket.getInputStream()));
				BufferedReader userInputReader = new BufferedReader(
						new InputStreamReader(System.in));) {
			String msg;
			System.out.println(in.readLine());
			while ((msg = userInputReader.readLine()) != null) {
				out.println(msg);
				do{
					String answer = in.readLine();
					System.out.println(answer);
					if (answer == null || answer.equals("Bye!"))
						return;
				}while(in.ready());
			}
		} catch (UnknownHostException e) {
			System.err.println("Host not found!");
			System.exit(1);
		} catch (IOException e) {
			System.err.println("Server is unreachable");
			System.exit(1);
		} catch (Exception e) {
			System.err.println("Error!");
			System.exit(1);
		}
	}

	/**
	 * Main
	 * @param args
	 * @since 16-02-2018
	 */
	public static void main(String[] args) {
		CalculatorClient client = new CalculatorClient("127.0.0.1", 12345);
		client.connect();
	}

}
