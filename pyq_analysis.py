# pyq_analysis.py

def analyze_pyqs(file_path="pyqs.txt"):
    keywords = ["OOP", "recursion", "pointers", "inheritance", "loops"]
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("PYQs file not found.")
        return

    count = {k: content.lower().count(k.lower()) for k in keywords}
    important_topics = sorted(count.items(), key=lambda x: x[1], reverse=True)

    for topic, freq in important_topics:
        print(f"🔸 {topic} - Appeared {freq} times")
