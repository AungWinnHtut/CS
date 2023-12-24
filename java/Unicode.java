
public class Unicode {
    public void greet() {
        char uniChar = '\u1000';
        System.out.println(uniChar);
    }

    public static void main(String[] args) {
        System.setProperty("console.encoding", "UTF-8");
        Unicode ucode = new Unicode();
        ucode.greet();
    }
}
