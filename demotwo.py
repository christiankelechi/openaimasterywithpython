from transformers import GPT2Tokenizer,GPT2LMHeadModel

tokenizer=GPT2Tokenizer.from_pretrained('gpt2')
model=GPT2LMHeadModel.from_pretrained('gpt2')

model.eval()

prompt=input("You: ")

input_ids=tokenizer.encode(prompt,return_tensors='pt')

output=model.generate(input_ids,max_length=50,do_sampe=True)

generated_text=tokenizer.decode(output[0],skip_special_tokens=True)

print("AI: "+generated_text)