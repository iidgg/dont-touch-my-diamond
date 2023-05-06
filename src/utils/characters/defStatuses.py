class CharacterStatuses:
    def __init__(self):
        # All available animations
        self.animations = a = ["walking", "running"]
        
        """"
        Structure:
        "Animation"
        "AnimationSpeed"
        "Speed * Number = the player speed *Speed = The given speed to the class*"
        """ # With spaces between each
        self.AI = [f"{a[0]} 0.1 1", f"{a[1]} 0.2 2"] # Animation information

        self.characterStatuses = {
            # Player direction
            "direction": "right",  # Is player facing left or right?

            # Player skin
            "skin": "Scar_L_Solider",

            # Animation
            "animation": {
                "frame": 0,
            }

            
        }

        for e in self.AI: # e Stands for element
            eSplitted = e.split()

            print(float(eSplitted[1]))
