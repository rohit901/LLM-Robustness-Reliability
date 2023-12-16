import spacy
from selfcheckgpt.modeling_selfcheck import SelfCheckBERTScore
from datasets import load_dataset
import numpy as np
import pickle
from tqdm import tqdm


bert_score = SelfCheckBERTScore(rescale_with_baseline=True)

nlp = spacy.load("en_core_web_sm")

def split_into_sentences(text):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences

dataset = load_dataset("rohit901/nlp_proj_llm_hallucination")['gpt3_5'] # Model to be evaluated for.

out_dir = "./output/hallucination_evaluation/bertscore"

score_dict = {}
for idx in tqdm(range(len(dataset))):
    sentences = dataset[idx]['sentences']
    text_samples = dataset[idx]['text_samples']
    passage_key = f"passage_{idx}"
    sentence_scores = bert_score.predict(sentences = sentences, sampled_passages = text_samples)
    score_dict[passage_key] = np.mean(sentence_scores)

with open(f"{out_dir}/score_dict_gpt3_5.pkl", "wb") as f:
    pickle.dump(score_dict, f)