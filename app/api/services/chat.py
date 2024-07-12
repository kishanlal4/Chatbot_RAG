import os
from openai import OpenAI
from app.api.services.pdf_extraction import split_text_into_chunks


# Function to use OpenAI API to process the text
def answer_text_with_openai(chunk, question, openai_api_key):
    client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key,
    )

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Analyze the following text and provide the summarized information on:\n\n{question}\n\n{chunk}",
        }
    ],
    model="gpt-3.5-turbo-0125",
    )
    return chat_completion.choices[0].message.content



def find_best_answer(chunks, question, openai_api_key):
    best_answer = ""
    best_score = 0

    for chunk in chunks:
        answer = answer_text_with_openai(chunk, question, openai_api_key)
        # Simple scoring: count keyword matches in the answer
        score = sum(word in answer for word in question.split())

        if score > best_score:
            best_score = score
            best_answer = answer

    return best_answer


# Main function
def main_ask(message, pdf_path, openai_api_key):
    print(pdf_path)
    question = message
    chunks = split_text_into_chunks(pdf_path)
    best_answer = find_best_answer(chunks, question, openai_api_key)
    return best_answer






