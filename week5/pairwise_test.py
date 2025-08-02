import pytest
from pairwise import Item, can_purchase

items = [Item("apple", "food"), Item("wine", "alcohol"), Item("cigar", "tobacco")]
locations = ["us", "eu"]
ages = range(15, 23)

@pytest.mark.parametrize("item", items)
@pytest.mark.parametrize("age", ages)
@pytest.mark.parametrize("location", locations)
def test_can_purchase(item, age, location):
    result = can_purchase(item, age, location)
    
    if item.category == "food":
        assert result is True
    elif item.category == "alcohol":
        if location == "us":
            assert result is (age >= 21)
        else:
            assert result is (age >= 16)
    elif item.category == "tobacco":
        if location == "us":
            assert result is (age >= 21)
        else:
            assert result is (age >= 18)