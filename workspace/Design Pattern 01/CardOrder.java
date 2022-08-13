import java.util.Collections;

/**
 * OOP Assignment One
 * CardOrder class keeps details of one card order
 * and provides methods to print a card 
 * and determine the price
 *
 */
public class CardOrder {
	private Name name;  	//the name printed on the card
	private char border;    //the card border
	private int numCards;   //the number of cards to be printed
	
	private static final int CARD_LEN = 32;  //the length of the card in characters
	
	//initialises name from value in parameter
	//and sets other instance variables to suitable default values
	//you can create a Name from a single string after L5
      //If you want to start before then, just write name = new Name("A", "B", "C") in the constructor!
	public CardOrder(String fullName) {
		String[] tmp = fullName.split(" ");
		if (tmp.length == 2) {
			name = new Name(tmp[0], tmp[1]);
		}
		else {
			name = new Name(tmp[0], tmp[1], tmp[2]);
		}
		border = '*';
		numCards = 0;
	}
	
	///////////////////////////////////////////
	//accessor/mutator methods
	
	//returns the character used in the border
	public char getBorder() {
		return border;
	}
	
	//sets the character used in the border 
	//to that provided in the parameter
	public void setBorder(char ch) {
		border = ch;
	}
	
	//returns the name 
	public Name getName() {
		return name;
	}
	
	//sets the name used in the card
	//to that provided in the parameter
	public void setName(Name ne) {
		name = ne;
	}
	
	//returns the number of cards to be printed
	public int getNumCards() {
		return numCards;
	}
	
	//sets the number of cards to be printed 
	//to that provided in the parameter
	public void setNumCards(int n) {
		numCards = n;
	}
	///////////////////////////////////////////
	
	//returns a sample card, including a newline at the end of each line
	public String getSampleCard() {
		return getTopLine() + getBlankLine() + this.getLineWithName()
		       + getBlankLine() + getTopLine();
	}
	
	//returns a String containing the top or bottom line
	//of a card, including a newline character at the end
	private String getTopLine() {
		//use this value until more code written
		String topLine = name.getInits();
		String edge = Character.toString(border);
		String edges = String.join("", Collections.nCopies(CARD_LEN - (topLine.length() * 2), edge));
		topLine += edges + name.getInits() + "\n";
		return topLine;
	}
	
	//returns a String containing the blank line
	//of a card, with a border char at each end
	//and including the newline character	
	private String getBlankLine() {	
		//use this value until more code written
		String blankLine = Character.toString(border);
		String blank = String.join("", Collections.nCopies(30, " "));
		blankLine += blank + blankLine + "\n";
		return blankLine;
	}
	
	//returns a String containing the name line
	//of a card, including name, padding and border
	//and including the newline character	
	private String getLineWithName() {
		//use this value until more code written
		String nameLine = Character.toString(border);
		String cardName = name.getCardName();
		
		int blank = CARD_LEN - cardName.length() - 2;
		if (blank % 2 == 1) {
			nameLine += String.join("", Collections.nCopies((blank / 2) + 1, " "));
		}
		else {
			nameLine += String.join("", Collections.nCopies((blank / 2), " "));
		}
		
		nameLine += cardName + String.join("", Collections.nCopies((blank / 2), " ")) + nameLine + "\n";
		
		return nameLine;
	}
	
	//returns the price of one card
	//in pounds (i,e either 0.20 or 0.25)
	//based on the number of characters in the name to be printed
	//0.20 if <=12 otherwise 0.25
	public int getCardPrice() {
		//use this value until more code written
		int price = 40;
		if (name.getCardName().length() > 12) {
			price = 50;
		}
		return price * numCards;
	}

	//returns the final cost of the order
	//which is the number of cards multiplied by the card price
	//and reduced by 10% if >= 100 cards
    public int getFinalCost() {
		//use this value until more code written
    	int finalCost = getCardPrice();
    	if (numCards >= 200) {
    		finalCost *= 0.9;
    	}
		return finalCost;   	
    }
    
    //returns true if number of cards < 100, false otherwise
    //public boolean hasDiscount() {

    //}
}
