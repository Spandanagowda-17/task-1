import datetime

class LibraryItem:
    def __init__(self, title, category, author_or_director, item_type, id):
        self.title = title
        self.category = category
        self.author_or_director = author_or_director
        self.item_type = item_type  # Book, Magazine, or DVD
        self.id = id
        self.checked_out = False
        self.due_date = None
        self.fine = 0

    def checkout(self, days_to_due=14):
        """Check out the item for a specific number of days."""
        self.checked_out = True
        self.due_date = datetime.date.today() + datetime.timedelta(days=days_to_due)
        print(f"Item '{self.title}' checked out. Due date: {self.due_date}.")

    def return_item(self):
        """Return the item and calculate any fines."""
        if not self.checked_out:
            print(f"Item '{self.title}' is not checked out.")
            return

        overdue_days = (datetime.date.today() - self.due_date).days
        if overdue_days > 0:
            self.fine = overdue_days * 0.5  # Fine of $0.50 per day overdue
            print(f"Item '{self.title}' returned. Overdue fine: ${self.fine:.2f}.")
        else:
            print(f"Item '{self.title}' returned. No overdue fine.")
        
        self.checked_out = False
        self.due_date = None

    def search(self, search_term):
        """Search by title, author/director, or category."""
        return (search_term.lower() in self.title.lower() or
                search_term.lower() in self.author_or_director.lower() or
                search_term.lower() in self.category.lower())

    def __str__(self):
        return f"{self.title} ({self.item_type}) - {self.category} - Author/Director: {self.author_or_director} - ID: {self.id}"


class Library:
    def __init__(self):
        self.items = {}
        self.next_id = 1

    def add_item(self, title, category, author_or_director, item_type):
        """Add a new item to the library collection."""
        new_item = LibraryItem(title, category, author_or_director, item_type, self.next_id)
        self.items[self.next_id] = new_item
        self.next_id += 1
        print(f"Item '{title}' added to the library with ID: {new_item.id}.")

    def checkout_item(self, item_id, days_to_due=14):
        """Check out an item from the library."""
        if item_id not in self.items:
            print(f"Item with ID {item_id} not found.")
            return

        item = self.items[item_id]
        if item.checked_out:
            print(f"Item '{item.title}' is already checked out.")
        else:
            item.checkout(days_to_due)

    def return_item(self, item_id):
        """Return an item to the library."""
        if item_id not in self.items:
            print(f"Item with ID {item_id} not found.")
            return

        item = self.items[item_id]
        item.return_item()

    def search_items(self, search_term):
        """Search for items by title, author, or category."""
        results = [item for item in self.items.values() if item.search(search_term)]
        if results:
            for item in results:
                print(item)
        else:
            print(f"No items found matching '{search_term}'.")

    def list_available_items(self):
        """List all available items (not checked out)."""
        available_items = [item for item in self.items.values() if not item.checked_out]
        if available_items:
            print("Available items in the library:")
            for item in available_items:
                print(item)
        else:
            print("No items are currently available.")

    def list_checked_out_items(self):
        """List all checked out items."""
        checked_out_items = [item for item in self.items.values() if item.checked_out]
        if checked_out_items:
            print("Checked out items:")
            for item in checked_out_items:
                print(item)
        else:
            print("No items are currently checked out.")


# Example Usage
def main():
    library = Library()

    # Adding items to the library
    library.add_item("The Great Gatsby", "Fiction", "F. Scott Fitzgerald", "Book")
    library.add_item("National Geographic", "Magazine", "Various", "Magazine")
    library.add_item("The Dark Knight", "Action", "Christopher Nolan", "DVD")

    # Listing available items
    library.list_available_items()

    # Searching for items
    print("\nSearching for books by 'Fitzgerald':")
    library.search_items("Fitzgerald")

    # Checkout an item
    print("\nChecking out 'The Great Gatsby'...")
    library.checkout_item(1)

    # Checking out an already checked-out item
    library.checkout_item(1)

    # Returning the item
    print("\nReturning 'The Great Gatsby'...")
    library.return_item(1)

    # Listing checked out items
    library.list_checked_out_items()

    # Listing available items again
    library.list_available_items()


if __name__ == "__main__":
    main()
