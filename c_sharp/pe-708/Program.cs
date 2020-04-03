using System;

namespace pe_708 {
    class Program {
        static void Main(string[] args) {
            if (args.Length > 0) {
                Console.WriteLine($"Hello, {args[0]}!");
            } else {
                Console.WriteLine("Hello, World!");    
            }
            
            Console.WriteLine("Fibonacci numbers 1 - 15:");
            for (int i = 0; i < 15; i++) {
                Console.WriteLine($"{i + 1}: {FibonacciNumbers(i)}");
            }
        }

        static int FibonacciNumbers(int n) {
            int a = 0;
            int b = 1;
            int tmp;
            for (int i = 0; i < n; i++) {
                tmp = a;
                a = b;
                b += tmp;
            }
            return a;
        }
    }
}
