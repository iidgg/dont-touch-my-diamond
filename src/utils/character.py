from src.utils.characters.defStatuses import CharacterStatuses

class Character(CharacterStatuses):
    def __init__(self):
        super().__init__()

        print("Hi from Character class")