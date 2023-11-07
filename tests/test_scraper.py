from scraper import fetch_data


def test_fetch_data():
    data = fetch_data("http://example.com")
    assert "Example Domain" in data.title
