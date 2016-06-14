from models import Player


class TestPlayer:
    def test_player_creation(self):
        pal = Player("Paladin")
        assert pal.name == "Paladin"
