def test_quote_1():
    search = "Bitcoin Billionaires"
    result = quote(search, limit=5)
    one = result[0]
    assert (
        one["author"] == "Ben Mezrich" and one["book"] and isinstance(one["quote"], str)
    )