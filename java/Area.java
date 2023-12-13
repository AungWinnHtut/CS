import java.util.Scanner;

public class Area {
    
    public static void areaOfCircle(float radius) //float radius = 22.44
    {
        //float radius = 44.5F;
        float Area = 3.14F * radius * radius;
        System.out.println("Ther Area is " + Area);
    }
    
    public static void main(String[] args)
    {
        areaOfCircle(23.44);
        Scanner scan = new Scanner(System.in);
        System.out.println("This is Test Program");
        System.out.print("Please enter username: ");
        String username = scan.nextLine();
        System.out.println("Your username is " + username);
    }
}
