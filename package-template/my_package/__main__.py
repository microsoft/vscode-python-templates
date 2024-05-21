from datetime import datetime

class Developer:
    valid_languages = [
        "Python", 
        "Java", 
        "JavaScript", 
        "C", 
        "C++", 
        "C#", 
        "PHP", 
        "Swift", 
        "Go", 
        "Kotlin", 
        "Ruby", 
        "Rust", 
        "TypeScript", 
        "Scala", 
        "Perl", 
        "Lua", 
        "Groovy", 
        "R", 
        "Shell", 
        "Objective-C", 
        "SQL", 
        "HTML/CSS"
    ]
    
    def __init__(self, name, language):
        if language not in self.valid_languages:
            raise ValueError(f"{language} is not a valid language.")
        self.name = name
        self.language = language

    def get_info(self):
        return f"{self.name} is a developer who codes in {self.language}."

def start_coding():
    print("Start coding in Python today!")

def date():
    current_datetime = datetime.now()
    return current_datetime

def main():
    start_coding()
    print(date())
    dev = Developer("Alice", "Python")
    print(dev.get_info())
    

main()
