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

def test_get_fruit(db_connection, page, test_web_address):
    db_connection.seed("seeds/fruit_store.sql")

    # We visit the books page
    page.goto(f"http://{test_web_address}/fruits")

    # Click the link with the text 'Bluets by Maggie Nelson'
    page.click("text=Mango, 8 calories")

    # The virtual browser acts just like a normal browser and goes to the next
    # page without us having to tell it to.

    # Then we look for specific test classes that we have put into the HTML
    # as targets for our tests to look for. This one is called `t-title`.
    # You can see it in `templates/books/show.html`
    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("Name: Mango")
    
    calory_element = page.locator(".t-calory")
    expect(calory_element).to_have_text("Calories: 8")

def test_create_fruit_form(db_connection, page, test_web_address):
    db_connection.seed("seeds/fruit_store.sql")
    page.goto(f"http://{test_web_address}/fruits")

    # This time we click the link with the text 'Add a new book'
    page.click("text=Add a new fruit")

    # Then we fill out the field with the name attribute 'title'
    page.fill("input[name='name']", "Strawberry")

    # And the field with the name attribute 'author_name'
    page.fill("input[name='calory']", "25")

    # Finally we click the button with the text 'Create Book'
    page.click("text=Create Fruit")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("Name: Strawberry")

    calory_element = page.locator(".t-calory")
    expect(calory_element).to_have_text("Calories: 25")
