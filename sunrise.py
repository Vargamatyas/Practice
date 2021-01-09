from random import shuffle


class Tower:

    def __init__(self, height, name):
        self.height = int(height)
        self.see_sunrise = True
        self.title = name
        self.highest_so_far = 0

    def set_highest_so_far(self, num):
        self.highest_so_far = num

    def get_highest_so_far(self):
        return int(self.highest_so_far)

    def get_name(self):
        return str(self.title)

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def set_seenable_sunrise_false(self):
        self.see_sunrise = False

    def get_see_sunrise(self):
        return self.see_sunrise

    def compare(self, other_tower):
        if other_tower == " ":
            self.set_highest_so_far(self.get_height())
            pass
        else:
            if self.get_height() > other_tower.get_highest_so_far():
                self.set_highest_so_far(self.get_height())

            else:
                self.set_seenable_sunrise_false()
                self.set_highest_so_far(other_tower.get_highest_so_far())

    def __str__(self):
        return str(self.see_sunrise)


taipei_oneone = Tower(300, "taipei_oneone")
burj_kalif = Tower(1000, "burj_kalif")
tower_elfeil = Tower(100, "tower_elfeil")
warsaw_radio_mast = Tower(800, "warsaw_radio_mast")
tokyo_skytree = Tower(700, "tokyo_skytree")
shanghai_tower = Tower(400, "shanghai_tower")

list_of_tower = [taipei_oneone, burj_kalif, tower_elfeil, warsaw_radio_mast, tokyo_skytree, shanghai_tower]
shuffle(list_of_tower)
printable_list = []
for tower in list_of_tower:
    printable_list.append(tower.get_name() + " " + str(tower.get_height()))

print(printable_list)

seenable_list = []
prev_tower = " "
for tower in list_of_tower:
    tower.compare(prev_tower)
    seenable_list.append(str(tower.get_see_sunrise()))
    prev_tower = tower

print(seenable_list)
towers_n_heights = "   ".join(printable_list)
seeing = "              ".join(seenable_list)
data = f"\n{towers_n_heights}\n{seeing}\n"

with open("data.txt", "a") as f:
    f.write(data)
