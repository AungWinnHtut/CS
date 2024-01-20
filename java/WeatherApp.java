import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;

public class WeatherApp {
    private static final String API_KEY = "dd7949b5d8974f05b2c121203242001";

    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            System.out.print("Enter city name: ");
            String cityName = reader.readLine();

            String weatherData = getWeatherData(cityName);
            if (weatherData != null) {
                System.out.println("\nWeather Information for " + cityName + ":");
                System.out.println(weatherData);
            } else {
                System.out.println("Unable to fetch weather data.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static String getWeatherData(String cityName) {
        try {
            String apiUrl = "https://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + cityName;

            URI uri = new URI(apiUrl);
            URL url = uri.toURL();

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                StringBuilder response = new StringBuilder();
                String line;

                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }

                reader.close();
                return response.toString();
            } else {
                System.out.println("HTTP error code: " + responseCode);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return null;
    }
}
