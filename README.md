# Analyzing the Robustness and the Reliability of Large Language Models

[Hanan Gani](), [Rohit K Bharadwaj](https://rohit901.github.io), [Muhammad Huzaifa]()

[![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://rohit901.github.io/media/LLM_Robustness_Reliability_NLP_701.pdf)

Official code for our NLP701 Project "Analyzing the Robustness and the Reliability of Large Language Models"

# Table of Contents
1. [Abstract](#abstract)
2. [Robustness](#robustness)
3. [Reliability](#reliability)
   1. [Code](#code)
   2. [Data](#data)
4. [Contact](#contact)

<hr>

<a name="abstract"></a>

# Abstract
> *Large Language Models (LLMs) are rapidly gaining traction in a variety of applications, performing impressively in numerous tasks. Despite their capabilities, there are rising concerns about the safety and the reliability of these systems, particularly when they are exploited by malicious users. This study aims to assess LLMs on two critical dimensions: Robustness and Reliability. For the Robustness component, we evaluate the robustness of LLMs against in-context attacks and adversarial suffix attacks. We further extend our analysis to Large Multi-modal models (LMMs) and examine the effect of visual perturbations on language output. Regarding Reliability, we examine the performance of well-known LLMs by generating passages about individuals from the WikiBio dataset and assessing the incidence of hallucinated responses. Our evaluation employs a black-box protocol conducted in a zero-resource setting. Despite security protocols embedded inside these models, our experiments demonstrate that these models are still vulnerable to different attacks.*
>

<a name="robustness"></a>

# Robustness

<a name="reliability"></a>

# Reliability
![Distribution of passage-level hallucination scores for GPT-3, GPT-4, Vicuna, MistralOrca by using BERTScore.](https://github.com/rohit901/LLM-Robustness-Reliability/assets/30185369/a2819c1b-e4fb-4435-8aa4-e7bc8d01b9ae)
* We observe that GPT-3.5, and GPT4 perform much better than existing open-source LLMs in terms of hallucinations as they have lower hallucination scores.
* Performance difference between GPT-3.5 and GPT-4 is almost negligible when we consider BERTScore to evaluate for hallucinations.

<a name="code"></a>

## Code
To replicate the environment for the project and run the code, follow these steps:
1. **Clone the Repository:**
   ```bash
   git clone git@github.com:rohit901/LLM-Robustness-Reliability.git
   cd LLM-Robustness-Reliability
   ```
2. **Create and Activate a Conda Environment:**
   ```bash
   conda create --name nlp_project python=3.11
   conda activate nlp_project
   ```
3. **Install Pip Packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **To Generate Data From GPT3_5/GPT4:**
   ```
   python reliability/generate_gpt_data.py
   ```
   Make sure that you have your OpenAI API key saved in a `.env` file, and place that file in `reliability/.env`. The content of the file should be:
   ```plaintext
   OPENAI_API_KEY=sk-<your_api_key>
   ```
5. **To Evaluate Hallucination using SelfCheckGPT-Prompt:**
   ```
   python reliability/evaluate_selfcheckgpt_prompt.py
   ```
6. **To Evaluate Hallucination using BERTScore:**
   ```
   python reliability/evaluate_bertscore.py
   ```

<a name="data"></a>

## Data
The data for the reliability experiments can be downloaded from the following link:

[Download Reliability Experiments Data](https://huggingface.co/datasets/rohit901/nlp_proj_llm_hallucination)

<a name="contact"></a>

# Contact
- For queries regarding Reliability part, contact [rohit.bharadwaj@mbzuai.ac.ae](mailto:rohit.bharadwaj@mbzuai.ac.ae)
- For queries regarding Robustness part, contact [hanan.ghani@mbzuai.ac.ae](hanan.ghani@mbzuai.ac.ae), [Muhammad.Huzaifa@mbzuai.ac.ae](Muhammad.Huzaifa@mbzuai.ac.ae)
