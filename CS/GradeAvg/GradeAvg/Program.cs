using System;

class Program
{
    static void Main(string[] args)
    {
        int numberOfGrades;
        double sumOfGrades = 0;

        Console.Write("Enter the number of grades: ");
        if (int.TryParse(Console.ReadLine(), out numberOfGrades) && numberOfGrades > 0)
        {
            for (int i = 1; i <= numberOfGrades; i++)
            {
                Console.Write($"Enter grade {i}: ");
                if (double.TryParse(Console.ReadLine(), out double grade))
                {
                    sumOfGrades += grade;
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter a valid grade.");
                    i--;
                }
            }

            double average = sumOfGrades / numberOfGrades;

            Console.WriteLine($"Average grade: {average:F2}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid number of grades.");
        }
    }
}
