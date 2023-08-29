import re
from collections import Counter

def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    
    total_words = len(words)
    unique_words = len(word_count)
    most_common_words = word_count.most_common(10)
    
    print("Text Analysis Report")
    print("--------------------")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}\n")
    print("Most common words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
    
    with open('text_analysis_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Text Analysis Report\n")
        report_file.write("--------------------\n")
        report_file.write(f"Total words: {total_words}\n")
        report_file.write(f"Unique words: {unique_words}\n\n")
        report_file.write("Most common words:\n")
        for word, count in most_common_words:
            report_file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    analyze_text(file_path)
