from transformers import pipeline

# Load GPT-2 model
generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    return generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
