#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class WordCounter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Word and Sentence Counter")

        self.label = tk.Label(self.window, text="Enter your text here:")
        self.label.pack()

        self.text_area = tk.Text(self.window, height=20, width=60)
        self.text_area.pack()

        self.button = tk.Button(self.window, text="Count Words and Sentences", command=self.count_words_and_sentences)
        self.button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def count_words_and_sentences(self):
        text = self.text_area.get("1.0", tk.END)
        words = text.split()
        sentences = text.replace('?', '.').replace('!', '.').split('.')

        word_count = len(words)
        sentence_count = len([sentence for sentence in sentences if sentence.strip() != ''])

        result = f"Number of words: {word_count}\nNumber of sentences: {sentence_count}"
        self.result_label.config(text=result)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    counter = WordCounter()
    counter.run()

