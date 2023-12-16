import os
import argparse
from openai import OpenAI
from datetime import datetime
from datasets import load_dataset
from dotenv import load_dotenv # pip install python-dotenv
import time
from pathlib import Path

from tqdm import tqdm

# Load the .env file
load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

model = "gpt-3.5-turbo" # LLM used in selfcheckgpt_prompt

dataset = load_dataset("rohit901/nlp_proj_llm_hallucination")['gpt3_5'] # Model to be evaluated for.

prompt_template = "Context: {}\n\nSentence: {}\n\nIs the sentence supported by the context above? Answer Yes or No: "

out_dir = "./output/hallucination_evaluation/selfcheckgpt_prompt/gpt3_5"

Path(out_dir).mkdir(parents=True, exist_ok=True)

for idx in range(len(tqdm(dataset))): # loop over each passage.
    sentences = dataset[idx]['sentences']
    text_samples = dataset[idx]['text_samples']
    for sent_i, sentence in enumerate(sentences): # loop over all "Response Sentences" in current passage.
        for sample_i, sample in enumerate(text_samples): # loop over all stochastic LLM samples.
            outpath = "{}/passage_{}_sentence_{}_sample_{}.txt".format(out_dir, idx, sent_i, sample_i)
            exist = os.path.isfile(outpath)
            if exist:
                print("idx {} - sentence {} sample {}: already exists".format(idx, sent_i, sample_i))
                continue
            
            prompt = prompt_template.format(sample.replace("\n", " "), sentence)
            try:
                response = client.chat.completions.create(
                    model = model,
                    messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature = 0.0,
                    max_tokens = 10, # generated tokens 
                )
                gen_text = response.choices[0].message.content
                with open(outpath, "w") as f:
                    f.write(gen_text)
            except:
                with open(f"{out_dir}/failed_cases_gpt3_5.txt", "a") as f:
                    f.write("Passage: {}, Sentence: {}, Sample: {}\n".format(idx, sent_i, sample_i))