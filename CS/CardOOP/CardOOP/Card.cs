namespace CardOOP
{
    class Card
    {
        private string face;
        private string suit;

        public Card(string face, string suit)
        {
            this.face = face;
            this.suit = suit;
        }

        public string getFace()
        {
            return face;
        }
        public string getSuit()
        {
            return suit;
        }
        public override string ToString() => $"{face} of {suit}";    
        
    }
}