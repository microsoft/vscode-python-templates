from datetime import datetime


class Developer:
    valid_languages: list[str] = [
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
        "HTML/CSS",
    ]

    def __init__(self, name, language) -> None:
        if language not in self.valid_languages:
            raise ValueError(f"{language} is not a valid language.")
        self.name = name
        self.language = language

    def get_info(self) -> str:
        return f"{self.name} is a developer who codes in {self.language}."


def start_coding() -> None:
    print("Start coding in Python today!")


def date() -> datetime:
    current_datetime: datetime = datetime.now()
    return current_datetime


def main() -> None:
    start_coding()
    print(date())
    dev = Developer("Alice", "Python")
    print(dev.get_info())


main()
