from models import Player


class TestPlayer:
    def test_player_creation(self):
        pal = Player("Paladin")
        assert pal.name == "Paladin"

    def test_player_default_name(self):
        brave = Player()
        assert brave.name == "Brave Knight"
