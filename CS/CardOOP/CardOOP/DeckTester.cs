using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CardOOP
{
    internal class DeckTester
    {
        public static void Main()
        {
            DeckOfCards deck = new DeckOfCards();
            deck.PrintCards();
            Console.ReadLine();
            Console.WriteLine("******************************");
            deck.Shuffle();
            deck.PrintCards();
            Console.ReadLine();
            deck.placingCard(5);
            deck.showingCards();
            Console.ReadLine();
            deck.calResult();
            deck.showResult();
            Console.ReadLine();


        }
    }
}
