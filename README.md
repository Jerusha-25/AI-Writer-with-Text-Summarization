# AI Writer with Text Summarization

## Objective
Build an AI-powered web application to generate concise summaries from large articles using Natural Language Processing (NLP).

---

## Tools & Technologies
- **Python** – Core programming language
- **Hugging Face Transformers** – Pre-trained models for text summarization (BART or T5)
- **Flask** – Lightweight web framework for building the app backend
- **textstat** – For calculating readability scores

---

## Features & Mini-Guide

1. **Use BART or T5 Summarization Model**  
   The app leverages advanced Hugging Face models like `facebook/bart-large-cnn` to generate high-quality summaries.

2. **Build Text Input Interface**  
   A clean, user-friendly web interface allows users to paste or type large text articles.

3. **Process Long Articles**  
   Handles long inputs by chunking them into manageable segments before summarization.

4. **Run Model and Return Summary**  
   The backend processes the input text through the summarization model and returns a concise summary.

5. **Add Word Count and Readability Score**  
   Alongside the summary, the app displays useful insights such as the word count and the Flesch reading ease score.

6. **Save History of Summaries** (Optional Feature)  
   Each summary is automatically saved in a local folder for later review.

7. **Deploy Using Flask**  
   The entire application is wrapped in a Flask server for easy local deployment or cloud hosting.

---

## Deliverables

- Fully functional **Web Application** with user-friendly UI  
- Integrated **NLP summarization model** for text processing  
- Display of **summary stats**: word count and readability  
- **History page** to browse all saved summaries  
- Sample output summaries included

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ai-writer-text-summarization.git
   cd ai-writer-text-summarization
