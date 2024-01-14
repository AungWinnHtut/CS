import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class ExpenseTracker {
    private Map<String, Double> expenses;

    //constructor
    public ExpenseTracker() {
        expenses = new HashMap<>();
    }

    public void addExpense(String category, double amount) {
        //if old value exists, add to this value, if not add 0.0
        expenses.put(category, expenses.getOrDefault(category, 0.0) + amount);
        //expenses.put(category,  amount);
        System.out.println("Expense added: $" + amount + " in category '" + category + "'");
    }

    public void viewTotalExpenses() {
        //extract all values, change stream to process, convert to all Double, Add ALL
        double totalExpenses = expenses.values().stream().mapToDouble(Double::doubleValue).sum();

        if (totalExpenses == 0.0) {
            System.out.println("No expenses recorded.");
        } else {
            System.out.println("Total Expenses: $" + totalExpenses);
            System.out.println("Expense Breakdown:");

            for (Map.Entry<String, Double> entry : expenses.entrySet()) {
                System.out.println("- " + entry.getKey() + ": $" + entry.getValue());
            }
        }
    }
}

public class ExpenseTrackerApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ExpenseTracker expenseTracker = new ExpenseTracker();

        while (true) {
            System.out.println("\nExpense Tracker Application");
            System.out.println("1. Add Expense");
            System.out.println("2. View Total Expenses");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter expense category: ");
                    String category = scanner.nextLine();
                    System.out.print("Enter expense amount: $");
                    double amount = scanner.nextDouble();
                    expenseTracker.addExpense(category, amount);
                    break;
                case 2:
                    expenseTracker.viewTotalExpenses();
                    break;
                case 3:
                    System.out.println("Exiting Expense Tracker Application. Goodbye!");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }
}

