# Dynamic MCQ Generator from Class Notes

**Status:** Currently In Progress  
**Domain:** NLP, EdTech, Python  
**Goal:** Turn raw classroom notes into intelligent, quiz-ready multiple-choice questions using NLP transformers and store them in an organized format.

---

## Features

- Parses .txt/.pdf/.docx notes and extracts meaningful statements
- Uses T5 transformer model to generate MCQs and answers
- Stores questions, options, answers, and topic tags in SQLite DB
- Allows easy export to CSV or PDF for quizzes
- CLI-based interface, GUI coming soon

---

## Tech Stack

- Python, HuggingFace Transformers (T5)
- NLTK/SpaCy for preprocessing
- SQLite for question DB
- Typer/argparse for CLI

---

## Roadmap

- [x] Load and chunk class notes
- [ ] Integrate T5-based question generation
- [ ] Build tagging and DB module
- [ ] CLI for quiz generation
- [ ] Export feature and GUI (Tkinter/Streamlit)

---

## 📁 Sample Output

