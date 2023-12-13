class Super {

    public void greet() {

        System.out.println("Hello Super");
    }

}

public class Sub extends Super {
    public void greet() {
        super.greet();
    }

    public static void main(String[] args) {
        Super parent = new Super();
        Sub child = new Sub();
        parent.greet();
        child.greet();
    }
}
