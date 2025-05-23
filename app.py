import os
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory, abort
from transformers import pipeline
from textstat import flesch_reading_ease

app = Flask(__name__)

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Folder to save summaries
HISTORY_DIR = 'summary_history'
if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    summary = word_count = readability = ''
    if request.method == 'POST':
        input_text = request.form['text']
        if len(input_text) > 0:
            result = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
            summary = result[0]['summary_text']
            word_count = len(summary.split())
            readability = round(flesch_reading_ease(summary), 2)

            # Save summary to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_filename = f'summary_{timestamp}.txt'
            filepath = os.path.join(HISTORY_DIR, safe_filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("Original Text:\n")
                f.write(input_text + "\n\n")
                f.write("Summary:\n")
                f.write(summary + "\n\n")
                f.write(f"Word Count: {word_count}\n")
                f.write(f"Readability Score: {readability}\n")

    return render_template('summarize.html', summary=summary, word_count=word_count, readability=readability)


@app.route('/history')
def history():
    # List all saved summary files sorted by newest first
    try:
        files = sorted(os.listdir(HISTORY_DIR), reverse=True)
    except FileNotFoundError:
        files = []
    return render_template('history.html', files=files)


@app.route('/history/<filename>')
def view(filename):
    # Security check: only serve files from the HISTORY_DIR folder
    if '..' in filename or filename.startswith('/'):
        abort(404)

    filepath = os.path.join(HISTORY_DIR, filename)
    if not os.path.isfile(filepath):
        abort(404)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    return render_template('view_summary.html', filename=filename, content=content)


if __name__ == '__main__':
    app.run(debug=True)
