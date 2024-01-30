# Study Easy
Welcome to ACM-VIT powered by VIT Vellore presents **Study Easy** - our project to help students and researchers alike to revise and learn smarter and better.

## What is Study-Easy?
A combination of two popular language models that allow summarization and generating question-answer pairs, connected by a backend that automatically converts your documents (pdf, pptx) into text for the models to run on.

As mentioned above, it comprises of two primary models:
1. *Summarization model* - Fine-tuned Mistral-7B model
2. *Question-Answer model* - Fine-tuned T5 model

<br>

> *UNDERSTANDING THE PROCESS* <br>
If you want to know more about the models and how we went about training them, please look into the documentation within the notebooks in the repository. All information regarding usage, fine-tuning and training datasets are mentioned in great detail.

## Study-Easy Summarizer

*In our model, we have fine-tuned the mistralai/Mistral-7B-v0.1 version.*

### Why Mistral 7B 
Mistral 7B is 7.3 billion parameter language model that uses [Grouped-query Attention (GQA)](https://aliissa99.medium.com/-a596e4d86f79), which allows for faster inference times compared to standard full attention. Mistral 7B [Sliding Window Attention (SWA)](https://medium.com/@gopalgoyal612002/mistral-llm-architectural-details-8dc0447fea62) gives it the ability to handle longer text sequences at a low cost. <br><br>
You can access Mistral 7B on HuggingFace, Vertex AI, Replicate, Sagemaker Jumpstart, Baseten and via the Kaggle "Models" feature.

#### What our model can do :
1. Dual capability to excel in both Natural language tasks and coding tasks.
2. Understands a variety of verbal nuances, resulting in more complex interactions and perceptive answers.

> *Competition Check!* <br>
It outperforms the 13 billion parameter model Llama 2 on most benchmarks!<br>
~More parameters = greater efficiency~



### Uses & Advantages of LoRa fine-tuned Mistral 7B
1. Can be used to summarize any form of literature including technical subjects like Discrete Mathematics.
2. Can produce varying types of summaries, depending on the document.
3. Primed for using on research and college notes.

### Limitations of our model
1. Need more larger training data set for college notes summarization.
2. Large computing power required.
3. Slow loading time since it's heavy to load.

<br>

## Study-Easy Q&A Generator

As the name suggests, this model uses the T5 (Text-To-Text Transfer Transformer) model to generate question and answer pairs based on a given context i.e., the text from the document.

To understand how QAG models work, read [here](https://github.com/asahi417/lm-question-generation?tab=readme-ov-file). 

### Uses & Advantages of Our Model
1. Generation of flashcards - can be used as a study tool.
2. Content Creation - Content generation platforms can use this model to automatically create questions and answers based on provided content.
3. Educational Tools - Our model can be employed to create educational materials in quizzes & assessments.

### Limitations of Our Model
1. Context Sensitivity - It may generate answers based on superficial patterns rather than deep comprehension.
2. Domain Specificity - If the model is trained on a specific domain, it may not generalize well to other domains. The model struggles with math related problems.
3. Length Limitations - Transformers have a maximum sequence length, so very long paragraphs may be truncated.
4. More Training Data Required - Training large transformer models requires significant computational resources, hence training them has been a challenge

## OUR LIMITATIONS & HOW YOU COULD HELP US
> No, we aren't asking for money.

Despite our best efforts, there are certain aspects that render this project far from fully useful and operational.
1. *Locally run only* - Due to resource limitations, we cannot deploy this project.
2. *No OCR* - For pictoral understanding and handwritting recognition, OCR is key. However, we faced multiple issues in that regard.
3. *Recurring Problems* - Even after the model shows no problem in running, there are instances where complex errors arise. While we have tried out best to mitigate that, the underlining issues may take time to erase.

If you see any obvious problems that can be taken care of, please feel free to put a pull request. Your contribution will be highly appreciated.

## Meet The Team

The ACM-VIT Study Easy team is 10 members strong.
> None of the members were limited to one particular task and all are regularly chipped in other domains.

### Project Mentors & Lead
- *Vidit Kothari* - ACM Developer Relations Lead 2024-25
- *Hari Kartha* - ACM HR Head

### Our Inspiration
- *Manav Muthanna* - ACM Chairperson 2024-25
- *Sarthak Gupta* - ACM Projects Lead 2024-25
- *Saharsh Bhansali* - ACM Research Lead 2024-25

<br>

| DOMAIN | PEOPLE | DESCRIPTION |
|-------|--------|-----|
|Summarization Model|Yasha Pacholee <br> Rohit Jindal <br> Sunny Gogoi| Dealt with Hugging Face, LoRa, manual data collection and attempted OCR & text extraction from documents.|
|Question-Answer Model| Abhirup Das <br> Nikhil <br> Raghav Sampath | Worked with QAG models and its types to try and resolve domain specificity. |
|Frontend Design & <br> Integration | Aditi Sridhar <br> Raghav Sampath | Used Python streamlit for simple frontend-backend interactioin and later switched to HTML, CSS & JS|

<br>

> *SPECIAL MENTIONS* <br>
This project wouldn't reach this stage without the help of Google, Stack Overflow, Medium & YouTube

> *USE OF CHATGPT* <br>
This project employed limited use of chatbots like ChatGPT and Bard due to their lack of integration & deployment understanding. However, they were quite handy in helping us understand the billion lines of error messages we encountered.
