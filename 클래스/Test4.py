class Game:
    def __init__(self, player_name, player_hp, player_attack, monster_name, monster_hp, monster_attack):
        self.player_name = player_name
        self.player_hp = player_hp
        self.player_attack = player_attack
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack

    def fight(self):
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"{self.player_name}의 체력: {self.player_hp}")
            print(f"{self.monster_name}의 체력: {self.monster_hp}")
            self.monster_hp -= self.player_attack
            print(f"{self.player_name}이 {self.monster_name}을 공격하여 {self.player_attack}의 데미지를 입혔습니다.")
            if self.monster_hp <= 0:
                print(f"{self.monster_name}을 물리쳤습니다.")
                break
            self.player_hp -= self.monster_attack
            print(f"{self.monster_name}이 {self.player_name}을 공격하여 {self.monster_attack}의 데미지를 입혔습니다.")
            if self.player_hp <= 0:
                print(f"{self.player_name}이 죽었습니다.")
                break
game = Game("Alice",120,15, "Goblin", 60, 8)
print(game.fight())
