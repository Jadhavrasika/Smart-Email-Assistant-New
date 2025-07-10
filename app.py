from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_reply(email_text, predicted_category):
    if predicted_category == "IT":
        prompt = f"As an IT support agent, write a polite reply to:\n{email_text}"
    elif predicted_category == "HR":
        prompt = f"As an HR representative, write a professional reply to:\n{email_text}"
    else:
        prompt = f"Write a polite, professional reply to:\n{email_text}"

    output = generator(prompt, max_length=256)[0]["generated_text"]
    return output
