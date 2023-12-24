import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutput {
    public static void main(String[] args) {
        try (FileOutputStream fos = new FileOutputStream("output.txt")) {
            String data = "Hello, I am Dr. Aung Win Htut";
            byte[] byteData = data.getBytes();
            fos.write(byteData);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
