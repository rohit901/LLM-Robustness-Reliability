# Analyzing the Robustness and the Reliability of Large Language Models

[Hanan Gani](), [Rohit K Bharadwaj](https://rohit901.github.io), [Muhammad Huzaifa]()

Official code for our NLP701 Project "Analyzing the Robustness and the Reliability of Large Language Models"

# Table of Contents
1. [Abstract](#abstract)
2. [Robustness](#robustness)
3. [Reliability](#reliability)
   1. [Code](#code)
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

<a name="contact"></a>

# Contact
- For queries regarding Reliability part, contact [rohit.bharadwaj@mbzuai.ac.ae](mailto:rohit.bharadwaj@mbzuai.ac.ae)
- For queries regarding Robustness part, contact [hanan.ghani@mbzuai.ac.ae](hanan.ghani@mbzuai.ac.ae), [Muhammad.Huzaifa@mbzuai.ac.ae](Muhammad.Huzaifa@mbzuai.ac.ae)
