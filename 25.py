from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

output = generator(
    "Explain Natural Language Processing:",
    max_length=80,
    num_return_sequences=1
)

print(output[0]["generated_text"])
# I have used tranformers library instead of OpenAi API