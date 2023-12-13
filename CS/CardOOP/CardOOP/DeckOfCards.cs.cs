using System;
using System.Collections.Specialized;
using System.Net.Security;
using System.Reflection.Metadata.Ecma335;
using System.Security.Cryptography.X509Certificates;

namespace CardOOP
{
    class DeckOfCards
    {
        private const int noOfCards = 52;
        private Card[] deck = new Card[noOfCards];
        private Card[] Players1 = new Card[5];
        private Card[] Players2 = new Card[5];
        private Card[] Players3 = new Card[5];
        private Card[] Players4 = new Card[5];
        private Card[] Players5 = new Card[5];

        private int player1Value = 0;
        private int player2Value = 0;
        private int player3Value = 0;
        private int player4Value = 0;
        private int player5Value = 0;


        private string[] faces = { "Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King" };
        private string[] suits = { "Heart", "Spade", "Diamond", "Club" };
        public DeckOfCards() {
            //int d = 0;
            for (int s = 0; s < 4; s++) {
                for (int i = 0; i < 13; i++)
                {
                    deck[ (s*13)+i ] = new Card(faces[i], suits[s] );
                    //deck[d++] = new Card(faces[i], suits[s]);
                    
                } 
            }        
        }

        public void PrintCards()
        {
            for (int s = 0; s < noOfCards; s++) {
                Console.Write($"{deck[s].ToString(),-19}");
                if ((s + 1) % 4 == 0)
                {
                    Console.WriteLine();
                }
            }
            
        }

        public void Shuffle()
        {
            Random rand = new Random();
            for(int i=0;i<deck.Length; i++)
            {
                int randCard1 = rand.Next(0, 51);
                int randCard2 = rand.Next(0, 51);
                Card tempCard = deck[randCard1];
                deck[randCard1] = deck[randCard2];
                deck[randCard2] = tempCard;
            }        
        }

        public void placingCard(int player)
        {
            int i = 0;
            int p = 0;      
           
            while(p<5)
            {
                Players1[p] = deck[i++];
                Players2[p] = deck[i++];
                Players3[p] = deck[i++];
                Players4[p] = deck[i++];
                Players5[p++] = deck[i++];               
            }
        }

        public void showingCards()
        {
            Console.WriteLine("\nPlayer1 Cards");
            Console.WriteLine("********************");
            for(int i =0; i<5; i++)
            {
                Console.WriteLine(Players1[i].ToString());
            }
            Console.WriteLine("\nPlayer2 Cards");
            Console.WriteLine("********************");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(Players2[i].ToString());
            }
            Console.WriteLine("\nPlayer3 Cards");
            Console.WriteLine("********************");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(Players3[i].ToString());
            }
            Console.WriteLine("\nPlayer4 Cards");
            Console.WriteLine("********************");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(Players4[i].ToString());
            }
            Console.WriteLine("\nPlayer5 Cards");
            Console.WriteLine("********************");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(Players5[i].ToString());
            }
        }

        public void calResult()
        {

            for (int i = 0; i < 5; i++)
            {
                player1Value += cardToValue(Players1[i]);
            }
            player1Value %= 10;

            for (int i = 0; i < 5; i++)
            {
                player2Value += cardToValue(Players2[i]);
            }
            player2Value %= 10;

            for (int i = 0; i < 5; i++)
            {
                player3Value += cardToValue(Players3[i]);
            }
            player3Value %= 10;

            for (int i = 0; i < 5; i++)
            {
                player4Value += cardToValue(Players4[i]);
            }
            player4Value %= 10;

            for (int i = 0; i < 5; i++)
            {
                player5Value += cardToValue(Players5[i]);
            }
            player5Value %= 10;

        }


        private int cardToValue(Card card)
        {
            int value = 0;
            switch (card.getFace())
            {
                case "Ace": value = 1; break; //Deuce
                case "Deuce": value = 2; break;
                case "Three": value = 3; break;
                case "Four": value = 4; break;
                case "Five": value = 5; break;
                case "Six": value = 6; break;
                case "Seven": value = 7; break;
                case "Eight": value = 8; break;
                case "Nine": value = 9; break;
                case "Ten": value = 10; break;
                case "Jack": value = 10; break;
                case "Queen": value = 10; break;
                case "King": value = 10; break;


            }
            return value;
        }

        public void showResult()
        {
            Console.WriteLine($"Player 1 Marks = {player1Value}");
            Console.WriteLine($"Player 2 Marks = {player2Value}");
            Console.WriteLine($"Player 3 Marks = {player3Value}");
            Console.WriteLine($"Player 4 Marks = {player4Value}");
            Console.WriteLine($"Player 5 Marks = {player5Value}");
            Console.WriteLine("The Winner is " + getWinner());
        }
        public string getWinner()
        {
            int greatest = player1Value;
            string winner = "Player 1";
            if ( player2Value > greatest)
            {
                greatest = player2Value;
                winner = "Player 2";
            }
            if (player3Value > greatest)
            {
                greatest = player3Value;
                winner = "Player 3";
            }
            if (player4Value > greatest)
            {
                greatest = player4Value;
                winner = "Player 4";
            }
            if (player5Value > greatest)
            {
                greatest = player5Value;
                winner = "Player 5";
            }

            if ((greatest == player2Value)  && (winner != "Player 2"))
            {
                winner += " Player 2";
            }
            if ((greatest == player3Value) && (winner != "Player 3"))
            {
                winner += " Player 3";
            }
            if ((greatest == player4Value) && (winner != "Player 4"))
            {
                winner += " Player 4";
            }
            if ((greatest == player5Value) && (winner != "Player 5"))
            {
                winner += " Player 5";
            }        

            return winner;
        }
    }
}
