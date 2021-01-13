"""

makes the dicing part faster, count the losses, make records

"""
import random


class Player:

    def __init__(self, name):
        self.name = name
        self.last_results = []
        self.units_killed = 0
        self.dice_sides = [x for x in range(1, 7)]

    def get_name(self):
        return self.name

    def roll(self, status):
        if status == "attack":
            random.shuffle(self.dice_sides)

            results = []
            for i in range(3):
                addable = random.choice(self.dice_sides)
                results.append(addable)

            results.sort(reverse=True)
            self.last_results = results

        else:
            results = []
            for i in range(2):
                addable = random.choice(self.dice_sides)
                results.append(addable)

            results.sort(reverse=True)
            self.last_results = results

    def get_last_results(self):
        return [self.last_results[0], self.last_results[1]]


class Game:

    def __init__(self):
        self.game_status = True
        self.players = []
        self.player_hash_map = {}

    def set_players(self, string):

        # factory method
        for index, player in enumerate(string.split(" ")):
            addable_player = Player(player)
            self.players.append(addable_player)

            self.player_hash_map[player] = int(index)
            print(self.player_hash_map)

    def turn_game_off(self):
        self.game_status = False

    def duel(self, attacker, attacker_unit, defender, defender_unit):
        attacker.roll("attack")
        defender.roll("defend")

        attacker_nums = attacker.get_last_results()
        defender_nums = defender.get_last_results()

        if attacker_nums[0] == defender_nums[0]:
            if attacker_nums[1] == defender_nums[1]:
                pass
            if attacker_nums[1] > defender_nums[1]:
                defender_unit -= 1
            else:
                attacker_unit -= 1

        if attacker_nums[0] < defender_nums[0]:
            attacker_unit -= 1
            if attacker_nums[1] == defender_nums[1]:
                pass
            if attacker_nums[1] > defender_nums[1]:
                defender_unit -= 1
            else:
                attacker_unit -= 1

        if attacker_nums[0] > defender_nums[0]:
            defender_unit -= 1
            if attacker_nums[1] == defender_nums[1]:
                pass
            if attacker_nums[1] > defender_nums[1]:
                defender_unit -= 1
            else:
                attacker_unit -= 1

        return [attacker_unit, defender_unit]

    def maainloop(self):
        players = input("Who are the players (string, whitespace separated): ")
        self.set_players(players)

        while self.game_status is True:
            whats_next = input("Whats next? ")

            if whats_next == "End game":
                self.turn_game_off()

            if whats_next == "attack":
                input_str = input("Who is attacking who, with how many soldiers? ")
                try:
                    players_involved_unit_nums = input_str.split(" ")
                    # nem mukodik
                    print(players_involved_unit_nums)
                    attacker = self.players[int(self.player_hash_map.get(players_involved_unit_nums[0]))]
                    attacker_name = attacker.get_name()
                    attacker_unit_num = int(players_involved_unit_nums[1])
                    defender = self.players[int(self.player_hash_map.get(players_involved_unit_nums[2]))]
                    defender_name = defender.get_name()
                    defender_unit_num = int(players_involved_unit_nums[3])

                    cond = True
                    while cond is True:
                        stop = input("vége a támadásnak? ")
                        if attacker_unit_num < 0 or attacker_unit_num == 0 or defender_unit_num <= 0 or stop == "Stop":
                            cond = False

                        else:
                            result = self.duel(attacker, attacker_unit_num, defender, defender_unit_num)
                            attacker_unit_num = result[0]
                            defender_unit_num = result[1]
                            print(f"{attacker_name}nek {attacker_unit_num} egysége marad míg {defender_name}nem {defender_unit_num} egysége van.")
                            continue

                except Exception:
                    continue


game = Game()
game.maainloop()





