import openai
import random

openai.api_key = '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'

def rephrase_question(question, num_rephrases):
    rephrases = set()
    while len(rephrases) < num_rephrases:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{question}\n\nRewrite the question:",
            temperature=0.7,
            max_tokens=30,
        )

        rephrase = response.choices[0].text.strip()

        # check if the generated rephrase is distinct
        if rephrase not in rephrases and rephrase:
            rephrases.add(rephrase)
    
    return rephrases

def main():
    question = input("Please enter your question: ")
    num_rephrases = 10

    rephrases = rephrase_question(question, num_rephrases)

    print(f"\nHere are {num_rephrases} different ways to ask your question:\n")
    for i, rephrase in enumerate(rephrases, start=1):
        print(f"{i}. {rephrase}")

if __name__ == "__main__":
    main()
