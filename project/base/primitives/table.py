from mahjong.constants import EAST, NORTH, SOUTH, WEST

from base.primitives.player import Player


class Table:
    def __init__(self):
        self.dora_indicators = []

        self.dealer_seat = None
        self.current_hand = None
        self.step = None
        self.log_id = None

        self.players = []

    def init(self, dealer_seat, current_hand, dora_indicator, step, scores):
        self.dora_indicators = [dora_indicator]

        self.dealer_seat = dealer_seat
        self.current_hand = current_hand
        self.step = step

        self.players = [Player(self, x, dealer_seat) for x in range(0, 4)]

        for i in range(0, len(scores)):
            self.get_player(i).scores = scores[i] * 100

    def get_player(self, player_seat):
        return self.players[player_seat]

    def add_dora(self, dora):
        self.dora_indicators.append(dora)

    @property
    def round_wind(self):
        if self.current_hand < 4:
            return EAST
        elif 4 <= self.current_hand < 8:
            return SOUTH
        elif 8 <= self.current_hand < 12:
            return WEST
        else:
            return NORTH
