from playwright.sync_api import Page, expect

def test_get_fruits(db_connection, page, test_web_address):
    # We seed our database with the book store seed file
    db_connection.seed("seeds/fruit_store.sql")

    # We load a virtual browser and navigate to the /books page
    page.goto(f"http://{test_web_address}/fruits")

    # We look at all the <li> tags
    list_items = page.locator("li")

    # We assert that it has the books in it
    expect(list_items).to_have_text([
        "Apple, 15 calories",
        "Pear, 1 calories",
        "Orange, 3 calories",
        "Mango, 8 calories",
        "Kiwi, 25 calories"
    ])