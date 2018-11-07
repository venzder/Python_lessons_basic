import Python_lessons_basic.lesson07.home_work.loto.cards as card

while True:
    x = input("Желаете ли сыграть в лото? Y/N ")
    if x.lower() == "y":
        barrel = cards.Barrel()
        card_my = cards.Cardplayer()
        card_comp = cards.Cardcomputer()
        i = 1
        while




        # i = 1
        # print(card.get_barrel(i))
        # card1 = card.Cardplayer()
        # card1.get_card()
        # card2 = card.Cardcomputer()
        # card2.get_card()
    elif x.lower() == "n":
        break
    else:
        print("Попробуйте выбрать еще раз")

if __name__ == "__main__":
    main()

