import java.io.FileInputStream;
import java.io.IOException;

public class FileInput {
    public static void main(String[] args) {
        try (FileInputStream fis = new FileInputStream("index.php")) {
            int byteData;
            while ((byteData = fis.read()) != -1) {
                System.out.print((char) byteData);
            }
        } catch (IOException e) {
            // e.printStackTrace();
            System.out.println("File not found!, Please check the file name and extension!");
        }
    }
}
