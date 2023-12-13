import java.util.Scanner;

public class Area2 {

    public static float areaOfRectangle(float L, float W) {
        return L * W;
        // System.out.println("The Rectangular Area is " + A);
    }

    public static float areaOfCircle(float R) {
        float A;
        A = 3.14F * R * R;
        // System.out.println("The Area of Circle is " + A);
        return A;
    }

    public static float volumeOfCircle() {
        // reading input
        float Volume;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please Enter Radius: ");
        float R = scanner.nextFloat();
        System.out.println("Please Enter Height: ");
        float Height = scanner.nextFloat();
        scanner.close();

        // calculating
        float Area = areaOfCircle(R);
        Volume = Area * Height;
        // System.out.println("Volume of Circle " + Volume);
        return Volume;
    }

    public static float volumeOfRectangle() {
        float Volume;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please Enter Length: ");
        float L = scanner.nextFloat();
        System.out.println("Please Enter Width: ");
        float W = scanner.nextFloat();
        System.out.println("Please Enter Height: ");
        float Height = scanner.nextFloat();
        scanner.close();

        // calculating
        float Area = areaOfRectangle(L, W);
        Volume = Area * Height;
        // System.out.println("Volume of Circle " + Volume);
        return Volume;
    }

    public static void main(String args[]) {
        float V1 = volumeOfCircle();
        float V2 = volumeOfRectangle();
        System.out.println("Volume of Circle " + V1);
        System.out.println("Volume of Rectangle " + V2);
    }
}
