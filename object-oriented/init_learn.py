import random
from functools import partial
'''
模拟21点游戏的规则。 其中：
suit = 花色
rank = 点数
'''

# 在基类中实现__init()__, 初始化父类
# note: self 指的是类对应的实例，而不是类本身

class Card:
    def __init__(self, rank, suit):
        # 利用__init__()函数初始化类中要用到的变量
        self.rank = str(rank)
        self.suit = suit
        self.hard, self.soft = self._points()


# NumberCard继承自Card类， 子类可以复用父类的__init()__方法
class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.suit)

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10, 10

# 定义花色类，用来创建花色常量
class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

#得到四个花色常量
(Club, Diamond, Heart, Spade) = Suit('Club', '♣️️'), Suit('Diamond', '◇'), Suit('Heart', '❤'), Suit('Spade', '♠️')


# 定义工厂函数：定义一个函数，可以批量化的返回不同的对象。即通过传给工厂函数不同的参数，来得到不同对象的实例
def card1(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}.get(rank)
        return FaceCard(name, suit)
    else:
        raise Exception('rank out of range')

# 使用映射和类简化设计

# 使用并行映射.但是该方法带来了映射键：1，11，12，13的重复逻辑
def card2(rank, suit):
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    #  完成1; 'A'和face card的名字映射
    rank_str = {1: 'A', 11:'J', 12: 'Q',13: 'K'}.get(rank, str(rank))
    return class_(rank_str, suit)

# 映射到牌面的元组
def card3(rank, suit):
    class_, rank_str = {1: (AceCard, 'A'),
                        11: (FaceCard, 'J'),
                        12: (FaceCard, 'Q'),
                        13: (FaceCard, 'k')}.get(rank, (NumberCard, str(rank)))
    return class_(rank_str, suit)

# 使用偏函数partial()进行对象初始化

def card4(rank, suit):
    class_ = {1: partial(AceCard, 'A'),
              11: partial(FaceCard, 'J'),
              12: partial(FaceCard, 'Q'),
              13: partial(FaceCard, 'K')}.get(rank, partial(NumberCard, str(rank)))
    return class_(suit)

# 实现集合类
# 定义了Deck类，实际上内部是对list的调用。我们只是用Deck类把list封装起来
class Deck:
    def __init__(self):
        self._cards = [card4(rank, suit) for rank in range(1, 14)
                                            for suit in (Club, Diamond, Heart, Spade)]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

# 扩展集合类。这样做的好处是不用重新实现pop()方法，只用简单的继承即可。此时不用显示实现pop()方法
class Deck2(list):
    def __init__(self):
        # 调用了基类中的__init__()函数初始化了list对象，构造了对象集合
        super().__init__(card4(rank, suit) for rank in range(1, 14)
                                                for suit in (Club, Diamond, Heart, Spade))
        random.shuffle(self)