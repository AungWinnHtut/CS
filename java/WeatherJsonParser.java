import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
//javac -cp "jackson-core-2.13.0.jar:jackson-databind-2.13.0.jar" WeatherJsonParser.java


public class WeatherJsonParser {
    public static void main(String[] args) {
        String json = "{\n" +
                "    \"location\":{\n" +
                "        \"name\":\"London\",\n" +
                "        \"region\":\"City of London, Greater London\",\n" +
                "        \"country\":\"United Kingdom\",\n" +
                "        \"lat\":51.52,\"lon\":-0.11,\n" +
                "        \"tz_id\":\"Europe/London\",\n" +
                "        \"localtime_epoch\":1706355895,\n" +
                "        \"localtime\":\"2024-01-27 11:44\"\n" +
                "        },\n" +
                "\n" +
                "    \"current\":{\n" +
                "        \"last_updated_epoch\":1706355000,\n" +
                "        \"last_updated\":\"2024-01-27 11:30\",\n" +
                "        \"temp_c\":6.0,\n" +
                "        \"temp_f\":42.8,\n" +
                "        \"is_day\":1,\n" +
                "        \"condition\":{\n" +
                "            \"text\":\"Partly cloudy\",\n" +
                "            \"icon\":\"//cdn.weatherapi.com/weather/64x64/day/116.png\",\n" +
                "            \"code\":1003\n" +
                "        },\n" +
                "        \"wind_mph\":6.9,\n" +
                "        \"wind_kph\":11.2,\n" +
                "        \"wind_degree\":190,\n" +
                "        \"wind_dir\":\"S\",\n" +
                "        \"pressure_mb\":1034.0,\n" +
                "        \"pressure_in\":30.53,\n" +
                "        \"precip_mm\":0.0,\n" +
                "        \"precip_in\":0.0,\n" +
                "        \"humidity\":81,\n" +
                "        \"cloud\":25,\n" +
                "        \"feelslike_c\":4.2,\n" +
                "        \"feelslike_f\":39.6,\n" +
                "        \"vis_km\":10.0,\n" +
                "        \"vis_miles\":6.0,\n" +
                "        \"uv\":2.0,\n" +
                "        \"gust_mph\":7.3,\n" +
                "        \"gust_kph\":11.7\n" +
                "    }\n" +
                "}";

        try {
            ObjectMapper objectMapper = new ObjectMapper();
            JsonNode root = objectMapper.readTree(json);

            // Extract temperature in degrees Celsius
            double tempCelsius = root.path("current").path("temp_c").asDouble();
            System.out.println("Temperature in Celsius: " + tempCelsius);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

