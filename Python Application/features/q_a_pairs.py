import torch
from transformers import AutoTokenizer

# Load the model from a .pt file and ensure it's in evaluation mode based on your version of PyTorch
model = torch.load("features/qna_model.pt", map_location=torch.device("cpu"))

# Load a tokenizer corresponding to a pre-trained question-answering model
tokenizer = AutoTokenizer.from_pretrained("abhir00p/Qgen_model_ACM")

# Function to clean and parse question-answer pairs
def clean_qa_pairs(qa_pairs):
    cleaned_qa_pairs = []
    for pair in qa_pairs:
        if "answer" in pair:   # Check if the keyword 'answer' is in the pair string
            question, answer = pair.split(", answer: ") # Check if the keyword 'answer' is in the pair string
            question_parts = question.split("question: ")  # Further split the question to remove the 'question: ' prefix
            cleaned_question = question_parts[1] # Take the actual question part
            answer_parts = answer.split("|") # Split the answer to remove any trailing characters after '|'
            cleaned_answer = answer_parts[0] # Take the actual answer part
            cleaned_answer = cleaned_answer.capitalize() # Capitalize the answer
            # Append the cleaned question and answer as a dictionary to the list
            cleaned_qa_pairs.append(
                {"question": cleaned_question, "answer": cleaned_answer}
            )
        else:
            # If the pair does not contain 'answer', do nothing 
            pass
    return cleaned_qa_pairs


# Function to generate question-answer pairs from a context
def generate_qa_pairs(context, model, tokenizer, num_pairs=1, max_length=256):
    qa_pairs = []

    current_start = 0
    # Process the context in chunks of max_length
    while current_start < len(context):
        # Determine the end index of the current chunk being processed
        current_end = min(current_start + max_length, len(context))
        chunk = context[current_start:current_end]

        # Tokenize the chunk for input into the model
        encoding = tokenizer.encode_plus(
            chunk, max_length=max_length, truncation=True, return_tensors="pt"
        )
        input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

        # Generate responses from the model
        output_sequences = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            early_stopping=True,
            num_beams=3,
            num_return_sequences=num_pairs,
            no_repeat_ngram_size=2,
            max_length=200,
        )

        # Decode each output sequence to text and split it into question-answer parts
        for sequence in output_sequences:
            qa_text = tokenizer.decode(sequence, skip_special_tokens=True)
            qa_parts = qa_text.split("[SEP]")  # This may not be used; could be a leftover
            qa_pairs.append(qa_text)  # Appends the entire QA text to the list

        # Move to the next chunk of text
        current_start = current_end

    # Clean the generated question-answer pairs
    cleaned_pairs = clean_qa_pairs(qa_pairs)
    return cleaned_pairs