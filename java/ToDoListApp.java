import java.util.ArrayList;
import java.util.Scanner;

class ToDoList {
    private ArrayList<String> tasks;

    //constructor  create empty list  
    public ToDoList() {
        tasks = new ArrayList<>();
    }

    //ArrayList.add(data) fun is used to add last element (append)
    public void addTask(String task) {
        tasks.add(task);
        System.out.println("Task added: " + task);
    }

    public void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks in the list.");
        } else {
            System.out.println("Tasks:");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i)); //ArrayList.get(index) သုံးပြီး အထဲက data တွေကို ယူ
            }
        }
    }

    public void markTaskAsCompleted(int taskIndex) {
        if (isValidIndex(taskIndex)) {
            System.out.println("Marking task as completed: " + tasks.get(taskIndex - 1)); //actual index start from '0'
            tasks.remove(taskIndex - 1); //ArrayList.remove()
        } else {
            System.out.println("Invalid task index.");
        }
    }

    private boolean isValidIndex(int index) {
        return index > 0 && index <= tasks.size();
    }
}

public class ToDoListApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ToDoList toDoList = new ToDoList();

        while (true) {
            System.out.println("\nToDo List Application");
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Mark Task as Completed");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");
                    String taskDescription = scanner.nextLine(); //to read string data
                    toDoList.addTask(taskDescription);
                    break;
                case 2:
                    toDoList.viewTasks();
                    break;
                case 3:
                    System.out.print("Enter the task index to mark as completed: ");
                    int taskIndex = scanner.nextInt(); //inded must be integer
                    toDoList.markTaskAsCompleted(taskIndex);
                    break;
                case 4:
                    System.out.println("Exiting ToDo List Application. Goodbye!");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }
}

