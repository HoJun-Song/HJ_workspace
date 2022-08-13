/*
 * OOP Assignment 1
 * Contains methods for interaction with user
 */
import java.util.Scanner;
public class CardInteraction {
	private Scanner scanner;
	private CardOrder card;
	
	public CardInteraction() {
		scanner = new Scanner(System.in);
	}
	
	//runs the program as follows:
	//Gets details of card name from user
	//Displays card
	//Repeatedly, until user responds ok
	//	Asks the user if they would like to change the border
	//	If so, change the border and print the new card
	//Print the price of the order
	//print whether a discount is applicable or not
	public void run() {
		//Alter this gradually to add more details
		System.out.print("Enter Name: ");
		String name = getNameFromUser();
		while (!name.contains(" ")) {
			System.out.println("Please include a blank in your name.");
			System.out.print("Enter Name: ");
			name = getNameFromUser();
		}
		card = new CardOrder(name);
		while (card.getName().getCardName().length() > 28) {
			System.out.println("Please write your name in 28 characters or less.");
			System.out.print("Enter Name: ");
			name = getNameFromUser();
			while (!name.contains(" ")) {
				System.out.println("Please include a blank in your name.");
				System.out.print("Enter Name: ");
				name = getNameFromUser();
			}
			card = new CardOrder(name);
		}
		System.out.print("\nHere is a sample card:\n\n");
		System.out.print(card.getSampleCard());
		
		System.out.print("\nEnter \"OK\" if this card is ok, otherwise enter an alternative border character: ");
		String borders = scanner.next();
		while (!borders.equals("OK")) {
			char border = borders.charAt(0);
			card.setBorder(border);
			System.out.print("Here is a sample card:\n\n");
			System.out.print(card.getSampleCard());
			System.out.print("\nEnter \"OK\" if this card is ok, otherwise enter an alternative border character: ");
			borders = scanner.next();
		}
		
		System.out.print("\nHow many cards would you like? ");
		int numCards = getNumberFromUser();
		while (numCards < 1 || numCards > 1000) {
			System.out.println("Please enter a number between 1 and 1000.");
			System.out.print("\nHow many cards would you like? ");
			numCards = getNumberFromUser();
		}
		card.setNumCards(numCards);
		
		System.out.println("\nThe price of " + card.getNumCards() + " cards is " + card.getFinalCost() + " won.");
		if (card.getNumCards() >= 200) {
			System.out.println("10% discount applied");
		}
		else {
			System.out.println("No discount given");
		}
	}

	//repeatedly requests and reads name from user
	//until valid (i.e. <=28 chars and contains at least one space
	//finally returns the valid text
	private String getNameFromUser() {
		//use this value until more code written
		String fullName = scanner.nextLine();
		return fullName;
	}
	
	//repeatedly requests and reads number from user
	//until valid number entered i.e. between 1 and 1000
	//finally returns the valid number	
	private int getNumberFromUser() {
		//use this number until more code written
		int numCards = scanner.nextInt();
		return numCards;
	}
	

}


