import java.util.ArrayList;
import java.util.Scanner;

public class ExpenseTracker {
    static ArrayList<Expense> expenses = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        printMenu();
        while (true) {
            System.out.print("\nEnter your choice (1/2/3/4): ");
            int choice = scanner.nextInt();
            scanner.nextLine();
            if (choice == 1) {
                addExpense();
            } else if (choice == 2) {
                viewExpenses();
            } else if (choice == 3) {
                calculateExpenses();
            } else if (choice == 4) {
                exitApp();
                break;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
            printMenu();
        }
    }

    public static void printMenu() {
        System.out.println("""
		\n       Welcome to Semicolon Expense Tracker App
        ------------------------------------------
				1. Add an expense
				2. View all expenses
				3. Calculate total expenses
				4. Exit
		""");
        
    }

    public static void addExpense() {
        System.out.print("Enter the date (YYYY-MM-DD): ");
        String date = scanner.nextLine();
        System.out.print("Enter the description: ");
        String description = scanner.nextLine();
        System.out.print("Enter the amount: ");
        float amount = scanner.nextFloat();
        scanner.nextLine();
        expenses.add(new Expense(date, description, amount));
        System.out.println("Expense added!");
    } 

    public static void viewExpenses() {
        if (expenses.isEmpty()) {
            System.out.println("No expenses recorded yet.");
        } else {
            for (Expense expense : expenses) {
                System.out.println("Date: " + expense.date + ", Description: " + expense.description + ", Amount: " + expense.amount);
            }
        }
    }

    public static void calculateExpenses() {
        double total = 0;
        for (Expense expense : expenses) {
            total += expense.amount;
        }
        System.out.println("Total Expenses: " + total);
    }

    public static void exitApp() {
        System.out.println("Exiting the app. Goodbye!");
    }
}

class Expense {
	String date;
	String description;
	float amount;
	
	Expense(String date, String description, float amount) {
		this.date = date;
		this.description = description;
		this.amount = amount;
	}

} 
