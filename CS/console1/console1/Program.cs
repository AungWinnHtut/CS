using System;

class StudentMarks
{
    public enum Status { OK=2,Cancel };
    private enum Exam { Fail,Pass,D};
    static int Main()
    {
 
        float Area = 0.0F;
        float Radius = 0.0F;
        string input = "";
        //Console.WriteLine(Status.Cancel);
        greet();
        Console.Write("Please Enter Radius in cm: ");
        input =Console.ReadLine() ?? "";
        if(float.TryParse(input, out Radius)) //true or false
        {
            Area = 3.14F * Radius * Radius;
            Console.WriteLine($"Area = {Area:F2}");
            string sArea = Area.ToString("F4");
            Console.WriteLine("Area = " + sArea);
        }
        else
        {
            Console.WriteLine("Error! Enter only float value!");
            Console.ReadLine();
            return (1);
        }

        int age = 0;
        Console.Write("Please Enter age : ");
        input = Console.ReadLine() ?? "";
        if (int.TryParse(input, out age)) //true or false
        {            
            Console.WriteLine($"age = {age}");
        }
        else
        {
            Console.WriteLine("Error! Enter only int value!");
            Console.ReadLine();
            return (1);
        }


        Console.ReadLine();
        return 0;
    }
    static float readFloatInput(string prompt)
    {
        float value = 0.0F;
        Console.Write(prompt);
        string input = "";
         input   = Console.ReadLine() ?? "";
        if(float.TryParse((string)input, out  value))
        {
            return value;
        }
        else
        {
            return -1;
        }       

    }

    static void greet()
    {
        Console.WriteLine("Hello");
        
    }

    static void greet(string name)
    {
        Console.WriteLine("Hello " + name);
    }
    static void greet(string name, string status)
    {
        Console.WriteLine("Hello " + name + status);
    }




}
