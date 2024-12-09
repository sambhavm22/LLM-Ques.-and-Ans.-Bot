# FLAN-T5 Q&A Model 🤖

This project is a simple **Q&A bot** built using **FLAN-T5**, a pretrained text-to-text transformer from Hugging Face. The app leverages **Streamlit** for an interactive and user-friendly interface.

---

## Features

- **Ask Questions**: Input questions and get AI-generated responses.
- **Summarization Support**: FLAN-T5 can handle complex queries and generate coherent answers.
- **Streamlit-Powered Interface**: Intuitive, responsive, and easy to use.
- **Lightweight Transformer Model**: Uses `google/flan-t5-base` for efficient response generation.

---

## Installation

Follow these steps to set up and run the app:

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### Step 1: Clone the Repository

```python
git clone https://huggingface.co/spaces/mehtasambhav/flan-t5-qa
```


### Step 2: Install Dependencies
Install the required Python packages using:

```python
pip install -r requirements.txt
```

### Step 3: Run the Application

Launch the app locally using:

```python
streamlit run app.py
```
## Requirements
The following Python libraries are required to run the app:

1. streamlit: For building the web-based interface.
2. transformers: To load and interact with the FLAN-T5 model.
3. torch: Backend framework for running the transformer model.
4. Dependencies are listed in the requirements.txt file.

## Usage
1. Open the app in your browser after running it.
2. Enter a question in the input field.
3. Click the Generate Response button to get an answer.
4. View the model's output in the Response section.

## Example
1 .Question: Who is Albert Einstein?
1. Response: Albert Einstein was a theoretical physicist known for his theory of relativity.

2. Question: Summarize: Artificial Intelligence is transforming the world rapidly.
2. Response: AI is rapidly transforming the world.

## Customization

You can fine-tune the behavior of the model by modifying the parameters in the generate_response function:

1. max_length: Defines the maximum length of the response.
2. temperature: Controls the randomness of responses (higher values produce more diverse outputs).
3. num_return_sequences: Specifies how many answers the model should generate.
4. top_p: Configures nucleus sampling for improved diversity.

## Limitations

1. Knowledge Cutoff: FLAN-T5 is pretrained and may not have knowledge of recent events.
2. Short Responses: The model may generate brief answers for broad or complex questions.
3. Model Size: Uses flan-t5-base, which is lightweight but less powerful compared to larger versions.

## Future Enhancements

1. Add support for larger models like flan-t5-large for better response quality.
2. Implement UI sliders to allow users to adjust parameters in real-time.
3. Integrate more use cases, such as translation or paraphrasing.



## Acknowledgments
1. Hugging Face for providing the FLAN-T5 model.
2. Streamlit for the seamless interface.
3. PyTorch for the efficient backend framework.

#### Feel free to contribute to the project or suggest improvements! 😊
