import random

def random_love_confession():
    """Creates a personalized, love confession with a random message."""

    # Input
    name = input("What is your name? ")
    love_interest = input("Who's your crush? ")

    # Variables
    love_messages = [
        "   I've been thinking about you a lot lately, and I realized that I've fallen deeply in love with you. Your joy and positive you are truly inspiring, and I'm drawn to your kind and compassionate nature. I've never felt this way about anyone before, and I can't imagine my life without you.",
        "   Every day I spend with you is a gift, and I cherish every moment. I love the way you make me feel, and I'm so grateful for your love and support. You're my best friend, my confidante, and the love of my life.",
        "   I've been trying to find the right words to express how I feel about you, but nothing seems quite enough. You're the most amazing person I've ever met, and I'm so lucky to have you in my life. I promise to always be there for you, no matter what. I love you more than words can say.",
        "   From the moment I met you, I knew there was something special about you. You've brought so much joy and happiness into my life, and I'm so grateful for your love. I can't wait to see what the future holds for us, and I'm excited to spend the rest of my life with you.",
        "   I've been falling in love with you little by little, day by day. Every time I see you, I'm reminded of how lucky I am to have you in my life. You're my everything, and I love you more than you'll ever know."
    ]

    # Random message
    random_message = random.choice(love_messages)
        
        
    # Personalized message
    love_message =  f"Dear {love_interest},\n\n{random_message}\n    I have feelings for you, {love_interest}. Your eyes and smile are truly admirable. I hope you can give me a chance to show you how much I care.\n\nSincerely,\n{name}"

    # Conditional statement
    if input("Do you want to add a special message? (yes/no) ").lower() == "yes":
        special_message = input("Enter your special message: ")
        love_message += f"\n\n{special_message}"

    # Output
    print(love_message)

    # Loop (optional)
    while input("Do you want to write another confession? (yes/no) ").lower() == "yes":
        random_love_confession()

# Run the function
random_love_confession()
