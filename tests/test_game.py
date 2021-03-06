# -*- encoding: utf-8 -*-
from unittest import TestCase

try:  # pragma: no cover
    from unittest.mock import Mock, patch
except ImportError:  # pragma: no cover
    from mock import Mock, patch

from tekmate.game import Player, Map
from tekmate.items import Item


class PlayerTestCase(TestCase):
    @patch("tekmate.items.Item.fill_attributes")
    def setUp(self, mock_fill):
        mock_fill.return_value = None
        self.player = Player()

        self.create_obtainable_item()
        self.create_usable_item()
        self.create_invalid_items()

    def create_obtainable_item(self):
        self.obtainable_item = Item([])
        self.obtainable_item.obtainable = True

    def create_usable_item(self):
        self.usable_item = Item([])
        self.usable_item.usable = True

    def create_invalid_items(self):
        self.not_usable_item = Item([])
        self.not_obtainable_item = Item([])

    def test_player_position_defaults_at_zero_450(self):
        self.assertEqual(self.player.position, (0, 400))

    def test_when_picking_up_obtainable_item_size_of_bag_should_be_one(self):
        self.player.add_item(self.obtainable_item)
        self.assertEqual(len(self.player.bag), 1)

    def test_when_picking_up_obtainable_item_parent_container_should_be_changed_to_bag(self):
        self.player.add_item(self.obtainable_item)
        self.assertIs(self.obtainable_item.parent_container, self.player.bag)

    def test_when_looked_at_item_in_bag_description_should_be_returned(self):
        self.player.add_item(self.obtainable_item)
        self.assertEqual("INSPECT", self.player.look_at(self.obtainable_item))

    def test_when_looked_at_item_in_space_inspect_message_should_be_returned(self):
        self.assertEqual(self.player.look_at(self.obtainable_item), self.obtainable_item.get_look_at_message())

    def test_when_trigger_item_combination_is_called_item_combine_functions_are_called(self):
        mock_item1 = Mock(spec=Item)
        mock_item2 = Mock(spec=Item)
        self.player.trigger_item_combination(mock_item1, mock_item2)
        mock_item1.combine.assert_called_with(mock_item2)
        mock_item2.combine.assert_called_with(mock_item1)

    @patch("tekmate.items.Item.fill_attributes")
    def test_when_added_non_obtainable_item_return_false(self, mock_fill):
        mock_fill.return_value = None
        any_item = Item([])
        self.assertFalse(self.player.add_item(any_item))


class MapTestCase(TestCase):
    def test_when_creating_map_name_must_be_passed(self):
        test_map = Map("TestMap")
        self.assertEqual(test_map.name, "TestMap")
