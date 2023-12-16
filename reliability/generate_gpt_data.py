import os
import argparse
from openai import OpenAI
from datetime import datetime
from datasets import load_dataset
from dotenv import load_dotenv # pip install python-dotenv
import time
import pickle
from tqdm import tqdm
from pathlib import Path

# Load the .env file
load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
model = "gpt-3.5-turbo"

with open('./context_list.pkl', 'rb') as f:
    context_list = pickle.load(f)

print("Number of contexts: ", len(context_list))

prompt_template = "This is a Wikipedia passage about {concept}: "
dest_base = f"./output/{model}"

Path(dest_base).mkdir(parents=True, exist_ok=True)

concept_to_model = {}
for concept in tqdm(context_list):
    try:
        prompt = prompt_template.format(concept = concept)
        response = client.chat.completions.create(
            model = model,
            messages = [
                {"role": "system", "content": "You are a helpful assistant. Given a user query, you have to generate the corresponding Wikipedia passage about the concept mentioned in the query."},
                {"role": "user", "content": prompt},
            ],
            temperature = 0.0,
        )
        gen_text = response.choices[0].message.content
        if concept in concept_to_model:
            concept_to_model[concept].append(gen_text)
        else:
            concept_to_model[concept] = [gen_text]

    except:
        print("Error for concept: ", concept)
        continue

for concept in concept_to_model:
    concept_to_model[concept] = concept_to_model[concept][0]

with open(f'{dest_base}/concept_to_model.pkl', 'wb') as f:
    pickle.dump(concept_to_model, f)

concept_to_model_samples = {}
for concept in tqdm(context_list):
    try:
        prompt = prompt_template.format(concept = concept)
        for i in range(6):
            response = client.chat.completions.create(
                model = model,
                messages = [
                    {"role": "system", "content": "You are a helpful assistant. Given a user query, you have to generate the corresponding Wikipedia passage about the concept mentioned in the query."},
                    {"role": "user", "content": prompt},
                ],
                temperature = 1.0,
            )
            gen_text = response.choices[0].message.content
            if concept in concept_to_model_samples:
                concept_to_model_samples[concept].append(gen_text)
            else:
                concept_to_model_samples[concept] = [gen_text]

    except:
        print("Error for concept: ", concept)
        continue

with open(f'{dest_base}/concept_to_model_samples.pkl', 'wb') as f:
    pickle.dump(concept_to_model_samples, f)