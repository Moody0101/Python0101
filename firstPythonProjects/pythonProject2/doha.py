class minecraft_character:

    def __init__(self, name, speed: int, attack_power, defense_power, height):
        self.name = name
        self.speed = speed
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.height = height

    def fast(self):
        if self.speed >= 50:
            return True

        else:
            return False
