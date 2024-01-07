public class Arg {

    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            switch(args[i]){
                case "-h": System.out.println("Hidden"); break;
                case "-r": System.out.println("Recursive"); break;
                case "-s": System.out.println("SystemFile"); break;
                case "/s": System.out.println("Sub folder"); break;
                case "/d": System.out.println("Directory"); break;
            }
        }
    }
}
