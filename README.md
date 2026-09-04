# 🤖 AI Code Reviewer

An AI-powered **Code Review Assistant** built with **Python, Llama 3.2, and Streamlit**. The application analyzes source code locally and provides intelligent feedback on **bugs, code quality, security issues, performance, readability, and best practices**.

Unlike cloud-based AI code reviewers, this project uses **Ollama + Llama 3.2 locally**, so **no OpenAI API key, API credits, or internet connection is required for AI inference**.

## 🚀 Features

* 🔍 Automated code analysis
* 🐛 Detects potential bugs and issues
* 🔐 Identifies common security vulnerabilities
* ⚡ Suggests performance improvements
* ✨ Improves code readability and maintainability
* 📚 Recommends coding best practices
* 💡 Provides actionable suggestions
* 🦙 Runs **Llama 3.2 locally using Ollama**
* 🔑 **No API key required**
* 🖥️ Interactive **Streamlit interface**
* 🐍 Built entirely with Python

## 🛠️ Tech Stack

* **Python**
* **Llama 3.2**
* **Ollama**
* **Streamlit**
* **LangChain** 

## 🔄 How It Works

```text
User Code
   ↓
Streamlit Interface
   ↓
Python Code Reviewer
   ↓
Ollama
   ↓
Llama 3.2
   ↓
AI Analysis
   ↓
Review + Suggestions
```

The user submits code through the Streamlit interface. The application sends the code to a locally running **Llama 3.2 model through Ollama**, which analyzes it and generates a structured code review.

## 🔒 Privacy & Local AI

All AI inference is performed locally through Ollama. Your source code does **not need to be sent to an external AI API**, making the project useful for experimenting with **private and offline AI-powered developer tools**.

## 🎯 Use Cases

* Learning programming best practices
* Debugging and improving Python code
* Identifying potential security problems
* Reviewing student projects
* Understanding AI-assisted software development
* Building privacy-focused developer tools

## 📌 Project Highlights

This project demonstrates how **local Large Language Models (LLMs)** can be integrated into practical developer tools without relying on paid cloud APIs.

> **Code locally. Review intelligently. No API credits required.**

## 👨‍💻 Built With

**Python + Streamlit + Ollama + Llama 3.2**
