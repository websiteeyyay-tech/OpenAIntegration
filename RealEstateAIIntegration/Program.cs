using OpenAI;
using OpenAI.Chat;
using System;
using System.Threading.Tasks;
using System.Collections.Generic;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("🏠 Real Estate AI Assistant");
        Console.WriteLine("Type 'exit' to quit.\n");

        // Load OpenAI API Key from environment variable
        var apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
        if (string.IsNullOrEmpty(apiKey))
        {
            Console.WriteLine("❌ Missing OpenAI API key. Please set it with:");
            Console.WriteLine("export OPENAI_API_KEY=your_api_key_here\n");
            return;
        }

        var client = new OpenAIClient(apiKey);

        // Create message history (for "memory")
        var messages = new List<Message>
        {
            new Message(Role.System, "You are a helpful AI assistant specializing in real estate. You can provide property details, price estimates, investment tips, and help users schedule appointments.")
        };

        // Example property listings
        var properties = new List<(string Name, string Location, int Price, int Bedrooms)>
        {
            ("Skyline Residences", "Makati", 7500000, 2),
            ("Palm Heights", "Taguig", 5200000, 1),
            ("Maple Grove Villas", "Quezon City", 4200000, 3),
            ("Seaview Towers", "Pasay", 8600000, 2)
        };

        while (true)
        {
            Console.Write("You: ");
            var userInput = Console.ReadLine();
            if (userInput?.ToLower() == "exit") break;

            // Handle simple keyword-based property search
            if (userInput!.ToLower().Contains("find") ||
                userInput.ToLower().Contains("condo") ||
                userInput.ToLower().Contains("house"))
            {
                Console.WriteLine("\n🔍 Searching properties for you...\n");
                foreach (var property in properties)
                {
                    Console.WriteLine($"🏘️ {property.Name} - {property.Location}");
                    Console.WriteLine($"   ₱{property.Price:N0} • {property.Bedrooms} Bedrooms\n");
                }
                continue;
            }

            // Add user message to chat history
            messages.Add(new Message(Role.User, userInput));

            // Create chat request with context (AI remembers previous messages)
            var chat = new ChatRequest(
                model: "gpt-5",
                messages: messages.ToArray()
            );

            var response = await client.ChatEndpoint.GetCompletionAsync(chat);

            var aiReply = response.FirstChoice.Message.Content[0].Text;
            Console.WriteLine($"\nAI: {aiReply}\n");

            // Add AI response to message history
            messages.Add(new Message(Role.Assistant, aiReply));
        }

        Console.WriteLine("👋 Goodbye!");
    }
}
