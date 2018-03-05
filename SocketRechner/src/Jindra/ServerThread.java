package Jindra;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * Eine Server Thread Klasse die für die Kommunikation mit nur jeweils einem Client
 * @author Michael Jindra
 * @version 16-02-2018
 */
public class ServerThread extends Thread{
	Socket client = null;
	BufferedReader in = null;
	PrintWriter out = null;
	String clientSocketString = null;
	
	/**
	 * Konstruktor
	 * @param client Socket vom Main Server übergeben
	 * @since 16-02-2018
	 */
	public ServerThread(Socket client) {
		this.client = client;
		this.clientSocketString = client.toString();
		
		try {
			in = new BufferedReader(new InputStreamReader(client.getInputStream()));
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		
		try {
			out = new PrintWriter(client.getOutputStream(), true);
		} catch (IOException e) {
			e.printStackTrace();
		}
		out.println("Hello "+clientSocketString+" send me your calculations!");
	}

	/**
	 * Die run antwortet auf die Commands des Clients
	 * @since 16-02-2018
	 */
	@Override
	public void run() {
		super.run();
		String message=null;
		while(true) {
			try {
				message=in.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			synchronized(this) {
				try {
					FileWriter fwriter = new FileWriter("actions.log",true);
					BufferedWriter writer = new BufferedWriter(fwriter);
					writer.write(client.toString()+": "+message+", Credits: "+Server.getcredits(clientSocketString));
					writer.newLine();
					writer.close();
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
			
			String[] args = message.split(" ");
			switch(args[0]) {
			case "!exit":
				out.println("Bye!");
				try {
					client.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
				return;
				
			case "!add":
				if(args.length!=3) {
					out.println("Incorrect amount of parameters. Type !help for help");
				}else {
					if(Server.getcredits(clientSocketString)==0) {
						out.println("Sorry, you don't have enough Credits. Buy some with \"!buy <how many> \"");
					}else {
						Server.subcredits(clientSocketString);
						out.println(Integer.parseInt(args[1])+Integer.parseInt(args[2])+" Credits: "+Server.getcredits(clientSocketString));
					}
				}
				break;
				
			case "!sub":
				if(args.length!=3) {
					out.println("Incorrect amount of parameters. Type !help for help");
				}else {
					if(Server.getcredits(clientSocketString)==0) {
						out.println("Sorry, you don't have enough Credits. Buy some with \"!buy <nr> \"");
					}else {
						Server.subcredits(clientSocketString);
						out.println(Integer.parseInt(args[1])-Integer.parseInt(args[2])+" Credits: "+Server.getcredits(clientSocketString));
					}
				}
				break;
				
			case "!buy":
				if(args.length!=2) {
					out.println("Incorrect amount of parameters. Type !help for help");
				}else {
					if(Integer.parseInt(args[1])<1){
						out.println("You are not allowed to buy less than 1 credit.");
					}else {
						Server.addcredits(clientSocketString, Integer.parseInt(args[1]));
						out.println("Credits: "+Server.getcredits(clientSocketString));
					}
				}
				break;
				
			case "!help":
				out.println("!add <nr1> <nr2>\n!sub <nr1> <nr2>\n!exit\n!buy <nr>");
				break;
				
			default:
				out.println("No valid command. Try to type !help");
				break;
			}
			
		}
	}
}
