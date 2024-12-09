import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer once for efficiency
@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large") 
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")
    return tokenizer, model

# Function to generate the response
def generate_response(prompt):
    tokenizer, model = load_model()
    # Tokenize the input
    input_text = f"Answer the question: {prompt}"  # Add task-specific context
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    # Generate the response
    outputs = model.generate(
        input_ids, 
        max_length=200,  
        min_length=50,   
        temperature=0.9,  
        top_p=0.95,       
        repetition_penalty=1.2,
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Streamlit app UI
st.set_page_config(page_title="FLAN-T5 Q&A", page_icon="🤖")
st.title("FLAN-T5 Q&A Model 🤖")
st.write("Ask a question")

# Get user input
input_text = st.text_input("Your Q&A bot")

# Button to generate the output
if st.button("Generate Response"):
    if not input_text.strip():
        st.warning("Please enter a prompt!")
    else:
        st.subheader("Response:")
        with st.spinner("Generating response..."):
            response = generate_response(input_text)
        st.write(response)
