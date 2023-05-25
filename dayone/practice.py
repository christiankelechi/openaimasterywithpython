import random

# Define templates
templates = {
    "discount": "Hello {name},\nWe're offering a special discount on our products!...",
    "new product": "Hi {name},\nWe have a new product that we think you'll love...",
    "thank you": "Dear {name},\nThank you for your support...",
    "newsletter": "Greetings {name},\nHere's our latest news...",
    "feedback": "Hi {name},\nCould you take a moment to give us your feedback...",
    "event": "Hello {name},\nYou're invited to our upcoming event...",
    "reminder": "Dear {name},\nThis is a reminder about your upcoming appointment...",
    "update": "Hi {name},\nWe have an update we'd like to share with you...",
    "invitation": "Hello {name},\nWe'd like to invite you to join us...",
    "promotion": "Greetings {name},\nDon't miss out on our special promotion..."
}

def generate_email(keyword, name):
    template = templates.get(keyword)
    if template:
        return template.format(name=name)
    else:
        return None

def generate_emails(keywords, names):
    emails = []
    for name in names:
        keyword = random.choice(keywords)
        email = generate_email(keyword, name)
        if email:
            emails.append(email)
    return emails

keywords = ["discount", "new product", "thank you", "newsletter", "feedback", "event", "reminder", "update", "invitation", "promotion"]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

emails = generate_emails(keywords, names)
for email in emails:
    print(email)
    print("\n----------------------\n")
