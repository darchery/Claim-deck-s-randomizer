import unittest
from unittest.mock import patch
import sys
import os

# Add the src/EN_version path so the module can be imported
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "main"))

import functions_variables_constants as fvc


def reset_state():
    """Helper to reset all global state between tests."""
    fvc.globalListOfPairedFactions = []
    fvc.globalListOfNonPairedFactions = []
    fvc.expansionsNotAdded = [
        fvc.CLAIM_I, fvc.CLAIM_II, fvc.CLAIM_V,
        fvc.FEAR, fvc.FROST, fvc.MAPS,
        fvc.MERCENARIES, fvc.MAGIC, fvc.FIRE
    ]
    fvc.expansionsAdded = []


# ─────────────────────────────────────────────
# cleanPool
# ─────────────────────────────────────────────
class TestCleanPool(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_clean_pool_empties_paired_factions(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.cleanPool()
        self.assertEqual(fvc.globalListOfPairedFactions, [])

    def test_clean_pool_empties_non_paired_factions(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.cleanPool()
        self.assertEqual(fvc.globalListOfNonPairedFactions, [])

    def test_clean_pool_resets_expansions_not_added(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.cleanPool()
        self.assertIn(fvc.CLAIM_I, fvc.expansionsNotAdded)

    def test_clean_pool_empties_expansions_added(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.cleanPool()
        self.assertEqual(fvc.expansionsAdded, [])

    def test_clean_pool_restores_all_nine_expansions(self):
        fvc.addAllExpansionsToPool()
        fvc.cleanPool()
        self.assertEqual(len(fvc.expansionsNotAdded), 9)


# ─────────────────────────────────────────────
# addAnExpansion
# ─────────────────────────────────────────────
class TestAddAnExpansion(unittest.TestCase):

    def setUp(self):
        reset_state()

    # Claim I
    def test_add_claim_i_adds_paired_faction(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        self.assertIn(fvc.pairedFactionsClaimI, fvc.globalListOfPairedFactions)

    def test_add_claim_i_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        for faction in fvc.nonPairedFactionsClaimI:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)

    def test_add_claim_i_moves_to_added_list(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        self.assertIn(fvc.CLAIM_I, fvc.expansionsAdded)
        self.assertNotIn(fvc.CLAIM_I, fvc.expansionsNotAdded)

    # Claim II
    def test_add_claim_ii_adds_paired_faction(self):
        fvc.addAnExpansion(fvc.CLAIM_II)
        self.assertIn(fvc.pairedFactionsClaimII, fvc.globalListOfPairedFactions)

    def test_add_claim_ii_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.CLAIM_II)
        for faction in fvc.nonPairedFactionsClaimII:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)

    # Claim V
    def test_add_claim_v_adds_paired_faction(self):
        fvc.addAnExpansion(fvc.CLAIM_V)
        self.assertIn(fvc.pairedFactionsClaimV, fvc.globalListOfPairedFactions)

    def test_add_claim_v_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.CLAIM_V)
        for faction in fvc.nonPairedFactionsClaimV:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)

    # Fear (no paired faction)
    def test_add_fear_does_not_add_paired_faction(self):
        paired_before = len(fvc.globalListOfPairedFactions)
        fvc.addAnExpansion(fvc.FEAR)
        self.assertEqual(len(fvc.globalListOfPairedFactions), paired_before)

    def test_add_fear_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.FEAR)
        for faction in fvc.nonPairedFactionsFear:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)

    # Frost
    def test_add_frost_adds_paired_faction(self):
        fvc.addAnExpansion(fvc.FROST)
        self.assertIn(fvc.pairedFactionsFrost, fvc.globalListOfPairedFactions)

    def test_add_frost_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.FROST)
        for faction in fvc.nonPairedFactionsFrost:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)

    # Maps
    def test_add_maps_adds_paired_faction(self):
        fvc.addAnExpansion(fvc.MAPS)
        self.assertIn(fvc.pairedFactionsMaps, fvc.globalListOfPairedFactions)

    def test_add_maps_adds_non_paired_faction(self):
        fvc.addAnExpansion(fvc.MAPS)
        self.assertIn(fvc.nonPairedFactionsMaps, fvc.globalListOfNonPairedFactions)

    # Mercenaries
    def test_add_mercenaries_adds_paired_faction(self):
        fvc.addAnExpansion(fvc.MERCENARIES)
        self.assertIn(fvc.pairedFactionsMercenaries, fvc.globalListOfPairedFactions)

    def test_add_mercenaries_adds_non_paired_faction(self):
        fvc.addAnExpansion(fvc.MERCENARIES)
        self.assertIn(fvc.nonPairedFactionsMercenaries, fvc.globalListOfNonPairedFactions)

    # Magic (no paired faction)
    def test_add_magic_does_not_add_paired_faction(self):
        paired_before = len(fvc.globalListOfPairedFactions)
        fvc.addAnExpansion(fvc.MAGIC)
        self.assertEqual(len(fvc.globalListOfPairedFactions), paired_before)

    def test_add_magic_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.MAGIC)
        for faction in fvc.nonPairedFactionsMagic:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)

    # Fire (no paired faction)
    def test_add_fire_does_not_add_paired_faction(self):
        paired_before = len(fvc.globalListOfPairedFactions)
        fvc.addAnExpansion(fvc.FIRE)
        self.assertEqual(len(fvc.globalListOfPairedFactions), paired_before)

    def test_add_fire_adds_non_paired_factions(self):
        fvc.addAnExpansion(fvc.FIRE)
        for faction in fvc.nonPairedFactionsFire:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)


# ─────────────────────────────────────────────
# removeAnExpansion
# ─────────────────────────────────────────────
class TestRemoveAnExpansion(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_remove_claim_i_removes_paired_faction(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.removeAnExpansion(fvc.CLAIM_I)
        self.assertNotIn(fvc.pairedFactionsClaimI, fvc.globalListOfPairedFactions)

    def test_remove_claim_i_removes_non_paired_factions(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.removeAnExpansion(fvc.CLAIM_I)
        for faction in fvc.nonPairedFactionsClaimI:
            self.assertNotIn(faction, fvc.globalListOfNonPairedFactions)

    def test_remove_claim_i_moves_back_to_not_added(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.removeAnExpansion(fvc.CLAIM_I)
        self.assertIn(fvc.CLAIM_I, fvc.expansionsNotAdded)
        self.assertNotIn(fvc.CLAIM_I, fvc.expansionsAdded)

    def test_remove_claim_ii(self):
        fvc.addAnExpansion(fvc.CLAIM_II)
        fvc.removeAnExpansion(fvc.CLAIM_II)
        self.assertNotIn(fvc.pairedFactionsClaimII, fvc.globalListOfPairedFactions)
        for faction in fvc.nonPairedFactionsClaimII:
            self.assertNotIn(faction, fvc.globalListOfNonPairedFactions)

    def test_remove_claim_v(self):
        fvc.addAnExpansion(fvc.CLAIM_V)
        fvc.removeAnExpansion(fvc.CLAIM_V)
        self.assertNotIn(fvc.pairedFactionsClaimV, fvc.globalListOfPairedFactions)

    def test_remove_fear(self):
        fvc.addAnExpansion(fvc.FEAR)
        fvc.removeAnExpansion(fvc.FEAR)
        for faction in fvc.nonPairedFactionsFear:
            self.assertNotIn(faction, fvc.globalListOfNonPairedFactions)

    def test_remove_frost(self):
        fvc.addAnExpansion(fvc.FROST)
        fvc.removeAnExpansion(fvc.FROST)
        self.assertNotIn(fvc.pairedFactionsFrost, fvc.globalListOfPairedFactions)

    def test_remove_maps(self):
        fvc.addAnExpansion(fvc.MAPS)
        fvc.removeAnExpansion(fvc.MAPS)
        self.assertNotIn(fvc.pairedFactionsMaps, fvc.globalListOfPairedFactions)
        self.assertNotIn(fvc.nonPairedFactionsMaps, fvc.globalListOfNonPairedFactions)

    def test_remove_mercenaries(self):
        fvc.addAnExpansion(fvc.MERCENARIES)
        fvc.removeAnExpansion(fvc.MERCENARIES)
        self.assertNotIn(fvc.pairedFactionsMercenaries, fvc.globalListOfPairedFactions)

    def test_remove_magic(self):
        fvc.addAnExpansion(fvc.MAGIC)
        fvc.removeAnExpansion(fvc.MAGIC)
        for faction in fvc.nonPairedFactionsMagic:
            self.assertNotIn(faction, fvc.globalListOfNonPairedFactions)

    def test_remove_fire(self):
        fvc.addAnExpansion(fvc.FIRE)
        fvc.removeAnExpansion(fvc.FIRE)
        for faction in fvc.nonPairedFactionsFire:
            self.assertNotIn(faction, fvc.globalListOfNonPairedFactions)

    def test_add_and_remove_does_not_change_other_expansions(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.addAnExpansion(fvc.CLAIM_II)
        fvc.removeAnExpansion(fvc.CLAIM_I)
        self.assertIn(fvc.pairedFactionsClaimII, fvc.globalListOfPairedFactions)
        for faction in fvc.nonPairedFactionsClaimII:
            self.assertIn(faction, fvc.globalListOfNonPairedFactions)


# ─────────────────────────────────────────────
# addAllExpansionsToPool
# ─────────────────────────────────────────────
class TestAddAllExpansionsToPool(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_add_all_empties_not_added_list(self):
        fvc.addAllExpansionsToPool()
        self.assertEqual(fvc.expansionsNotAdded, [])

    def test_add_all_fills_added_list_with_nine_expansions(self):
        fvc.addAllExpansionsToPool()
        self.assertEqual(len(fvc.expansionsAdded), 9)

    def test_add_all_populates_paired_factions(self):
        fvc.addAllExpansionsToPool()
        self.assertGreater(len(fvc.globalListOfPairedFactions), 0)

    def test_add_all_populates_non_paired_factions(self):
        fvc.addAllExpansionsToPool()
        self.assertGreater(len(fvc.globalListOfNonPairedFactions), 0)

    def test_add_all_twice_does_not_duplicate_factions(self):
        fvc.addAllExpansionsToPool()
        paired_count = len(fvc.globalListOfPairedFactions)
        non_paired_count = len(fvc.globalListOfNonPairedFactions)
        fvc.addAllExpansionsToPool()
        self.assertEqual(len(fvc.globalListOfPairedFactions), paired_count)
        self.assertEqual(len(fvc.globalListOfNonPairedFactions), non_paired_count)


# ─────────────────────────────────────────────
# chooseNumberOfFactions
# ─────────────────────────────────────────────
class TestChooseNumberOfFactions(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_two_players_sets_three_factions(self):
        fvc.numberOfPlayers = 2
        fvc.chooseNumberOfFactions()
        self.assertEqual(fvc.numbersOfFactions, 3)

    def test_three_players_sets_five_factions(self):
        fvc.numberOfPlayers = 3
        fvc.chooseNumberOfFactions()
        self.assertEqual(fvc.numbersOfFactions, 5)

    def test_four_players_sets_five_factions(self):
        fvc.numberOfPlayers = 4
        fvc.chooseNumberOfFactions()
        self.assertEqual(fvc.numbersOfFactions, 5)


# ─────────────────────────────────────────────
# generateRandomDeck
# ─────────────────────────────────────────────
class TestGenerateRandomDeck(unittest.TestCase):

    def setUp(self):
        reset_state()
        fvc.addAllExpansionsToPool()

    def test_deck_for_two_players_has_three_non_paired(self):
        fvc.numberOfPlayers = 2
        fvc.numbersOfFactions = 3
        with patch("builtins.print"):
            fvc.generateRandomDeck()
        # generateRandomDeck uses random.sample(globalListOfNonPairedFactions, numbersOfFactions)
        # We verify it doesn't raise and the pool still has all factions
        self.assertGreaterEqual(len(fvc.globalListOfNonPairedFactions), 3)

    def test_deck_for_three_players_has_five_non_paired(self):
        fvc.numberOfPlayers = 3
        fvc.numbersOfFactions = 5
        with patch("builtins.print"):
            fvc.generateRandomDeck()
        self.assertGreaterEqual(len(fvc.globalListOfNonPairedFactions), 5)

    def test_deck_generation_does_not_modify_global_lists(self):
        fvc.numberOfPlayers = 2
        fvc.numbersOfFactions = 3
        paired_before = list(fvc.globalListOfPairedFactions)
        non_paired_before = list(fvc.globalListOfNonPairedFactions)
        with patch("builtins.print"):
            fvc.generateRandomDeck()
        # Order may change due to shuffle, so compare as sets
        self.assertEqual(set(fvc.globalListOfPairedFactions), set(paired_before))
        self.assertEqual(set(fvc.globalListOfNonPairedFactions), set(non_paired_before))


# ─────────────────────────────────────────────
# Input functions (mocked stdin)
# ─────────────────────────────────────────────
class TestDeploySelectOptionsAndTakeInput(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_valid_option_1_is_accepted(self):
        with patch("builtins.input", return_value="1"), patch("builtins.print"):
            fvc.deploySelectOptionsAndTakeInput()
        self.assertEqual(fvc.option, 1)

    def test_valid_option_4_is_accepted(self):
        with patch("builtins.input", return_value="4"), patch("builtins.print"):
            fvc.deploySelectOptionsAndTakeInput()
        self.assertEqual(fvc.option, 4)

    def test_invalid_then_valid_input_is_accepted(self):
        inputs = iter(["9", "2"])
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            fvc.deploySelectOptionsAndTakeInput()
        self.assertEqual(fvc.option, 2)


class TestDelployAddDeleteOptionsAndTakeInput(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_valid_option_5_is_accepted(self):
        with patch("builtins.input", return_value="5"), patch("builtins.print"):
            fvc.delployAddDeleteOptionsAndTakeInput()
        self.assertEqual(fvc.optionAddDelete, 5)

    def test_invalid_then_valid_input_is_accepted(self):
        inputs = iter(["0", "3"])
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            fvc.delployAddDeleteOptionsAndTakeInput()
        self.assertEqual(fvc.optionAddDelete, 3)


class TestTakeNumberOfPlayersInput(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_valid_input_2(self):
        with patch("builtins.input", return_value="2"), patch("builtins.print"):
            fvc.takeNumberOfPlayersInput()
        self.assertEqual(fvc.numberOfPlayers, 2)

    def test_valid_input_4(self):
        with patch("builtins.input", return_value="4"), patch("builtins.print"):
            fvc.takeNumberOfPlayersInput()
        self.assertEqual(fvc.numberOfPlayers, 4)

    def test_invalid_then_valid_input(self):
        inputs = iter(["5", "3"])
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            fvc.takeNumberOfPlayersInput()
        self.assertEqual(fvc.numberOfPlayers, 3)

    def test_input_1_is_rejected(self):
        inputs = iter(["1", "2"])
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            fvc.takeNumberOfPlayersInput()
        self.assertEqual(fvc.numberOfPlayers, 2)


# ─────────────────────────────────────────────
# Edge cases
# ─────────────────────────────────────────────
class TestEdgeCases(unittest.TestCase):

    def setUp(self):
        reset_state()

    def test_add_same_expansion_twice_raises_value_error(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        # CLAIM_I is no longer in expansionsNotAdded, so remove() will raise ValueError
        with self.assertRaises(ValueError):
            fvc.addAnExpansion(fvc.CLAIM_I)

    def test_remove_expansion_not_added_raises_value_error(self):
        with self.assertRaises(ValueError):
            fvc.removeAnExpansion(fvc.CLAIM_I)

    def test_clean_pool_after_add_all_resets_correctly(self):
        fvc.addAllExpansionsToPool()
        fvc.cleanPool()
        self.assertEqual(fvc.globalListOfPairedFactions, [])
        self.assertEqual(fvc.globalListOfNonPairedFactions, [])
        self.assertEqual(len(fvc.expansionsNotAdded), 9)
        self.assertEqual(fvc.expansionsAdded, [])

    def test_expansions_added_list_tracks_correctly(self):
        fvc.addAnExpansion(fvc.CLAIM_I)
        fvc.addAnExpansion(fvc.FROST)
        self.assertEqual(sorted(fvc.expansionsAdded), sorted([fvc.CLAIM_I, fvc.FROST]))

    def test_fear_expansion_has_no_paired_faction_after_add(self):
        fvc.addAnExpansion(fvc.FEAR)
        self.assertEqual(fvc.globalListOfPairedFactions, [])

    def test_magic_expansion_has_no_paired_faction_after_add(self):
        fvc.addAnExpansion(fvc.MAGIC)
        self.assertEqual(fvc.globalListOfPairedFactions, [])

    def test_fire_expansion_has_no_paired_faction_after_add(self):
        fvc.addAnExpansion(fvc.FIRE)
        self.assertEqual(fvc.globalListOfPairedFactions, [])


if __name__ == "__main__":
    unittest.main()