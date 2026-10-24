# Local AI Chatbot with Ollama and Streamlit

A conversational AI chatbot built with **Python**, **Streamlit**, and **Ollama** that runs entirely on a local machine. The application provides an interactive chat interface powered by a locally hosted Large Language Model (LLM), enabling private, low-latency conversations without relying on cloud-based AI services.

## Features

- Interactive chat interface built with Streamlit
- Runs completely offline after the model is downloaded
- Powered by a locally hosted LLM using Ollama
- Maintains conversation history during the session
- Clear chat functionality
- Fast, private, and secure AI interactions

## Technologies Used

- Python
- Streamlit
- Ollama
- Qwen 2.5 (1.5B)

## Project Structure

```
ollama-model-chatbot/
│
├── app.py
├── requirements.txt
└── README.md
├── .gitignore
```

## Prerequisites

Ensure the following are installed before running the application:

- Python 3.10 or later
- Ollama

Download Ollama from:

https://ollama.com

## Installation

Clone the repository:

```bash
git clone https://github.com/padmabalasundar/ollama-model-chatbot.git
```

Navigate to the project directory:

```bash
cd ollama-model-chatbot
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Download the Model

Pull the language model using Ollama:

```bash
ollama run qwen2.5:1.5b
```

The model is downloaded only once and stored locally for subsequent use.

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Once started, the application will open in your default web browser.

## Application Workflow

1. The user enters a prompt through the chat interface.
2. Streamlit forwards the conversation history to Ollama.
3. The local language model processes the request.
4. The generated response is displayed in the chat.
5. The conversation continues until the session is cleared or the application is closed.

## Example

```
User:
What is Machine Learning?

Assistant:
Machine Learning is a branch of Artificial Intelligence that enables computers to identify patterns from data and make predictions or decisions without being explicitly programmed for every task.

User:
Can you provide a real-world example?

Assistant:
Recommendation systems used by streaming platforms and online retailers are common examples of Machine Learning applications.
```

## Requirements

```
streamlit
ollama
```

## Future Enhancements

- Support for multiple Ollama models
- Streaming responses
- Chat history export
- File and document-based question answering
- Voice input and speech synthesis
- Configurable system prompts

## Author

**PadmaBalasundar** — Developed a locally hosted AI chatbot powered by **Ollama**, **Python**, and **Streamlit**, featuring a conversational interface with persistent session context. The project demonstrates the integration of local Large Language Models (LLMs) into a lightweight web application, enabling private, low-latency AI interactions without relying on cloud-based services.