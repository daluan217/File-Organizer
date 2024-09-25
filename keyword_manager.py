# keyword_manager.py

class KeywordManager:
    def __init__(self):
        # Define categories and keywords
        self.categories = {
            "Python": ["python", "pandas", "numpy", "flask"],
            "Machine Learning": ["machine learning", "scikit-learn", "tensorflow", "neural network"],
            "Data Science": ["data", "statistics", "data analysis", "data science"],
            "Web Development": ["html", "css", "javascript", "react", "django"]
        }

    def get_categories(self):
        return self.categories
