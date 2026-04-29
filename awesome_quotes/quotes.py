import random

QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. – Aristotle",
    "Whoever is happy will make others happy too. – Anne Frank",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "The journey of a thousand miles begins with one step. – Lao Tzu",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. – Benjamin Franklin",
]

def get_random_quote():
    """Return a random inspiring quote."""
    return random.choice(QUOTES)

if __name__ == "__main__":
    print(get_random_quote())
