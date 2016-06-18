import pytest
from models import Player


class TestPlayer:
    def test_player_creation(self):
        brave = Player()
        assert brave.name == 'Brave Hero', 'Default name not working'

        bob = Player('Bob')
        assert bob.name == 'Bob', 'Chosen player name not assigned'

        assert not bob.get_class('archaelogist'), \
            'Disallowed class not returning False'
        with pytest.raises(AttributeError):
            bob.p_class  # TODO: find way to return custom error message
        assert bob.get_class('mage'), 'get_class method not returning True'
        assert bob.p_class == 'mage', \
            'Allowed chosen player class not assigned'
        assert bob.get_class('MaGe'), \
            'Allowed class with upper case not returning True'
        assert not bob.p_class == 'MaGe', \
            'Allowed class with upper case not dropping to lower case'
        assert bob.p_class == 'mage', \
            'Allowed class with upper case not saving as lower case'
