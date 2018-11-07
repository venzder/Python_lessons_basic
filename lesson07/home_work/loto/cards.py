import random



class Card:
    def __init__(self, name_card = ""):
        self.name_card = name_card
        self.game_set = random.sample(range(90), 30)
        self.player_set = random.sample(self.game_set, 15)
        self.player_field = [self.player_set[:5], self.player_set[5:10], self.player_set[10:]]

    @property
    def get_lines(self):
        for playerline in self.player_field:
            playerline.sort()
            playerline.insert(random.randint(0, 4), ' ')
            playerline.insert(random.randint(0, 5), ' ')
            playerline.insert(random.randint(0, 6), ' ')
            playerline.insert(random.randint(0, 7), ' ')
        return self.player_field


    def get_card(self):
        print("{:-^26}".format(self.name_card))
        for line in self.get_lines:
            for n in line:
                print('{0:>2}'.format(n), end=' ')
            print()
        print('{:-^26}\n'.format('-'))

    def strikeout(self, barrel):
        for line in self.player_field:
            for x in line:
                if x == barrel:
                    x = "><"
        return self.get_lines

class Cardplayer(Card):
    def __init__(self, name_card=" Ваша карта "):
        super(). __init__(self)
        self.name_card = name_card


class Cardcomputer(Card):
    def __init__(self, name_card=" Карта компьютера "):
        super(). __init__(self)
        self.name_card = name_card


class Barrel:
    def __init__(self):
        self.list_barrel = [itm for itm in range(1, 91)]
        self.barrel = 0
        self.rest_barrels = 0


    def get_barrel(self, round):
        i = 0
        while i < round:
            self.barrel = random.choice(self.list_barrel)
            self.list_barrel.remove(self.barrel)
            self.rest_barrels = len(self.list_barrel)
            i += 1
        return f"Новый боченок: {self.barrel} (Осталось {self.rest_barrels})"


# def get_run(round):
#     barrel = Barrel()




if __name__ == "__main__":

    card = Cardcomputer()
    card.strikeout(9)
    card.get_card()



    barrel = Barrel()
    print(barrel.get_barrel(8))
    print(barrel.rest_barrels)


