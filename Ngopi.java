import java.util.*;
import javax.swing.JOptionPane;

public class Ngopi {

	public static void main(String[] args) {
		
		// Prima
		
//		for (int i=1;i<=20;i++) {
//			int prima = 0;
//			for (int j=1;j<=i;j++) {
//				if (i%j==0) {
//					prima++;
//				}
//				else {
//					;
//				}
//			}
//			if (prima==2) {
//				System.out.println(i+" adalah bilangan prima.");
//			}
//			else {
//				System.out.println(i+" bukan bilangan prima.");
//			}
//		}
		
		
		// ArrayList
//		Scanner scanner = new Scanner(System.in);
//		ArrayList<String> games = new ArrayList<String>();
//	
//		while (true) {	
//	
//			System.out.println("What games would you like to add? (Input blank to quit): ");
//			String addtolist = scanner.nextLine();
//		
//			if (addtolist.isBlank()) {
//				break;
//			}
//			else {
//				games.add(addtolist);
//			}
//		
//			System.out.println("Your current games in list :");
//			for (int i=0;i<games.size();i++) {
//				System.out.println(games.get(i));
//			}
		
			// FOREACH
//			for (String i : games) {
//				System.out.println(i);
//			}
//	
//	}
		
		
	// METHODS
//		String[] accounts = {"kenntcky","kentapassword123"};
//		
//		String usn = JOptionPane.showInputDialog("Please input your username.");
//		if (usn.equals(accounts[0])) {
//			int lvl = 21;
//			String pwinput = JOptionPane.showInputDialog("Please input your password.");
//			if (pwinput.equals(accounts[1])) {
//				login(usn, lvl);
//			}
//		}
		
		// OOP
		Map<String, String> accounts = new HashMap<>();
		
		while (true) {
			String option = JOptionPane.showInputDialog("Do you have an account? (Y/N/X to exit)");
			if (option.equalsIgnoreCase("y")) {
				String usninput = JOptionPane.showInputDialog("Input your username.");
				for (Map.Entry<String, String> acc : accounts.entrySet()) {
					if (usninput.equals(acc.getKey())) {
						String pwinput = JOptionPane.showInputDialog("Insert your password.");
						if (pwinput.equals(acc.getValue())) {
							JOptionPane.showMessageDialog(null, "Welcome, "+acc.getKey()+"!");
							break;
						}
						else {
							JOptionPane.showMessageDialog(null, "Invalid password!");
						}
					}
					else {
						JOptionPane.showMessageDialog(null, "Invalid username!");
					}
				}
			}
			else if (option.equalsIgnoreCase("n")) {
				String usninput = JOptionPane.showInputDialog("Insert your username.");
				if (accounts.containsKey(usninput)) {
					JOptionPane.showMessageDialog(null, "Username already exists!");
				}
				else {
					String pwinput = JOptionPane.showInputDialog("Insert your password.");
					String pwconfirm = JOptionPane.showInputDialog("Confirm your password.");
					if (pwinput.equals(pwconfirm)) {
						accounts.put(usninput, pwinput);
						JOptionPane.showMessageDialog(null, "Account has been successfully created!");
					}
					else {
						JOptionPane.showMessageDialog(null, "Password does not match.");
					}
				}
			}
			else if (option.equalsIgnoreCase("x")) {
				break;
			}
		}
	}

	// METHODS
	
//	static void login(String usn, int lvl) {
//		
//		JOptionPane.showMessageDialog(null, "Welcome back "+usn+"!\nLevel: "+lvl);
//		
//	}
	
}
