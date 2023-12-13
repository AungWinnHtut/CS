public class Student {
    
    private String name;
    private int age;

    
    public  Student()
    {

    }

    public void setName(String username)
    {
        name = username;
    }
    public String getName()
    {
        return name;
    }
    public void setAge(int userage)
    {
        age=userage;
    }
    public int getAge()
    {
        return age;
    }


    public static void main(String[] args)
    {
        Student ayeaye = new Student();
        //ayeaye.name = "ayeaye";
        ayeaye.setName("aye aye");
      
        //ayeaye.age = 20;
        ayeaye.setAge(20);

        System.out.println("Name: " + ayeaye.getName());
        System.out.println("Age: " + ayeaye.getAge()); 

    }

}
