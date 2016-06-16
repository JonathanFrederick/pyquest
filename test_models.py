import pytest
from models import Player


class TestPlayer:
    def test_player_creation(self):
        pal = Player("Paladin")
        assert pal.name == "Paladin"

    def test_player_default_name(self):
        brave = Player()
        assert brave.name == "Brave Hero"

    def test_player_class(self):
        bob = Player('Bob')
        assert bob.get_class('mage')
        assert bob.p_class == 'mage'

    def test_player_wrong_class(self):
        jim = Player('Jim')
        assert not jim.get_class('archaeologist')
        with pytest.raises(AttributeError):
            jim.p_class
