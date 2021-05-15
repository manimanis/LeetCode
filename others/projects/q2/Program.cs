using System;

namespace q2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Type a string ?");
            string input = Console.ReadLine();

            // there is at most input.Length / 2 words in the input
            string[] words = new string[input.Length];
            int count = 0;
            int p = -1;

            do
            {
                // Search the space index
                p = input.IndexOfAny(new char[] {' ', ',', '.', ':'});
                // If there is no spaces we are at the last word
                if (p == -1)
                {
                    p = input.Length;
                }
                // Get the word
                string word = input.Substring(0, p);
                if (word.Length > 0) {
                    words[count++] = word;
                }
                // Remove it from the input string
                input = (p == input.Length) ? "" : input.Substring(p + 1);

                // Loop until the string is empty
            } while (input.Length > 0);

            Console.WriteLine("Found {0} words", count);
            for (int i = 0; i < count; i++)
            {
                Console.WriteLine(words[i]);
            }
            // The book:on the table, and the pen.
        }
    }
}
