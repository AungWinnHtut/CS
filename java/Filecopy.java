import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Filecopy {

    public static void main(String args[]) throws IOException {
        FileInputStream in = null;
        FileOutputStream out = null;

        in = new FileInputStream("input.txt");
        out = new FileOutputStream("output.txt");

        int c;
        while ((c = in.read()) != -1) {  //EOF - end of file
            out.write(c);
        }
        in.close();
        out.close();

    }
}