def checkTitle(text: str) -> None:
    return True if text == text.title() else False
    
if __name__ == "__main__":
    test_cases = [
            "A Mind Boggling Achievement",
            "A Simple C++ Program!",
            "Water is transparent",
        ]
    
    for t in test_cases:
        print(checkTitle(t))