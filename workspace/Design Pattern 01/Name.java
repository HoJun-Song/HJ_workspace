//Basics 3
public class Name {
	
	private String firstName;
	private String middleName;
	private String lastName;
	
	public Name(String fName, String mName, String lName) {
		firstName = fName;
		middleName = mName;
		lastName = lName;
	}
	public Name(String fName, String lName) {
		firstName = fName;
		lastName = lName;
	}
	
	public String getFirstName() {return firstName; }
	public String getMiddleName() { return middleName; }
	public String getLastName() {return lastName; }
	  
	public void setFirstName(String fn) {
		firstName = fn;
	}
	public void setMiddleName(String mn) {
		middleName = mn;
	}
	public void setLastName(String ln) {
		lastName = ln;
	}
	  
	public String getFirstAndLastName() {
		return firstName + " " + lastName;
	}
	  
	public String getLastCommaFirst() {
		return lastName + ", "+ firstName;
	}
	
	public String getInits() {
		String inits;
		if (middleName == null) {
			inits = firstName.substring(0,1) + lastName.substring(0,1);
		}
		else {
			inits = firstName.substring(0,1) + middleName.substring(0,1) + lastName.substring(0,1);
		}
		return inits;
	}
	
	public String getCardName() {
		String cardName = firstName + " ";
		if (middleName != null) {
			cardName += middleName.substring(0,1) + " ";
		}
		cardName += lastName;
		return cardName;
	}
}

