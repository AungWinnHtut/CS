import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class AreaOutput {
    public static void main(String[] args) {
        float r = 23.44f;
        float a = 3.1415f * r * r;
        String filePath = "area.txt";

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true))) {
            writer.write(Float.toString(a));
            writer.newLine(); // Add a new line after the float value
            System.out.println("Float data with new line has been appended to the file.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
