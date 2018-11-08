import random


class Card:

    def __init__(self, name: str, numbers_lst):
        self._name = name[0:24] if len(name) > 24 else name
        self._numbers_list = numbers_lst
        self._numbers = self._fill_card()
        self._cross = 0

    def _fill_card(self):
        random_list = []
        while len(random_list) <= 27:
            n = random.choice(self._numbers_list)
            if n not in random_list:
                random_list.append(n)
        random_list.sort()
        dct = dict(zip(range(27), random_list))
        for i in range(0, 3):
            for_delete = random.sample(range(i, len(dct), 3), 4)
            for j in range(i, len(dct), 3):
                if j in for_delete:
                    dct[j] = ' '
        return dct

    def validate_number(self, number):
        if number in self._numbers.values():
            return True
        return False

    def cross_number(self, number):
        for key in self._numbers.keys():
            if self._numbers[key] == number:
                self._numbers[key] = 'XX'
                self._cross += 1

    def get_cross(self):
        return self._cross

    def print_card(self):
        name = ' ' + self._name + ' '
        print('{:-^26}'.format(name))
        for i in range(0, 3):
            for j in range(i, len(self._numbers), 3):
                print('{: >2} '.format(self._numbers[j]), end='')
            print()
        print('-' * 26)


class Game:

    def __init__(self):
        self._bag = list(range(1, 91))
        self._player_card = Card('Ваша карточка', self._bag)
        self._ai_card = Card('Карточка компьютера', self._bag)
        self._notice = ['Вы проиграли!', 'Поздравляем! Вы выиграли!', 'Нажмите "y" или "n"']

    def game(self):
        while self._bag:
            random.shuffle(self._bag)
            keg = self._bag.pop()
            print('Зачеркнуто номеров: {} - {}'.format(self._player_card.get_cross(), self._ai_card.get_cross()))
            print('Новый бочонок: {} (осталось {})'.format(keg, len(self._bag)))
            self._player_card.print_card()
            self._ai_card.print_card()
            while True:
                choose = input('Зачеркнуть цифру? (y/n)').lower()
                if choose != 'y' and choose != 'n':
                    print(self._notice[2])
                    continue
                break
            if choose == 'y':
                if self._player_card.validate_number(keg):
                    self._player_card.cross_number(keg)
                else:
                    print(self._notice[0])
                    break
            else:
                if self._player_card.validate_number(keg):
                    print(self._notice[0])
                    break
            if self._ai_card.validate_number(keg):
                self._ai_card.cross_number(keg)
            if self._player_card.get_cross() == 15:
                print(self._notice[1])
                self._player_card.print_card()
                break
            if self._ai_card.get_cross() == 15:
                print(self._notice[0])
                break
            print()


game_session = Game()
game_session.game()




