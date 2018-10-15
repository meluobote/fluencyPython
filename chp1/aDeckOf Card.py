# -*- coding: utf-8 -*-
"""
   File Name：     aDeckOf Card
   Description :
   Author :       meluobote
   date：          2018/10/15
"""
import collections

# rank : 代表点数
# suit: 代表花色
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    suits = 'spades diamonds clubs hearts '.split()
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks
                      for suit in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]


'''
    排序： 假设花色从大到小排序依次是 clubs， diamonds, hearts, spades，  设值分别为3,2,1,0
            2...10 J Q K A   对应： 0.....12
           然后就有了两种排序方案， 一种是先按花色排，再按点数排； 另一种是先按点数排，再按花色拍
    方案控制方式： 排的比较值计算
        先按花色排： 梅花的排在最后，梅花中最小的一张的比较值为3*13
        先按数字排： A的拍咋爱最后， A中最小的一张花色的比较值为12*4 
'''


# 计算比较值的函数
def calculateCardValue(card: Card):
    suits = 'spades hearts diamonds clubs'.split()
    suit_dict = {key: value for value, key in enumerate(suits)}
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    rank_dict = {key: value for value, key in enumerate(ranks)}
    #先按花色排
    return suit_dict[card.suit]*13+rank_dict[card.rank]
    #先按点数排
    # return rank_dict[card.rank]*4 + suit_dict[card.suit]
fd = FrenchDeck()
print(fd.cards)
print(sorted(fd, key=calculateCardValue))
