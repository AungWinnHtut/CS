import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class CalculateVol {
    public static void main(String[] args) {
        String filePath = "area.txt";
        String areaString = "";
        float height = 3.4f;

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            // Read the area value from the file
            // Read and process each line in the file
            while ((areaString = reader.readLine()) != null) {
                try {
                    // Parse the area value to a float
                    float area = Float.parseFloat(areaString);

                    // Calculate the volume (replace with your actual formula)
                    float volume = area * height;

                    // Print the result for each line
                    System.out.println("Area: " + area + "\tVolume: " + volume);
                } catch (NumberFormatException e) {
                    System.out.println("Error parsing the area value: " + areaString);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (NumberFormatException e) {
            System.out.println("Error parsing the area value from the file. Please make sure it's a valid float.");
        }
    }
}
