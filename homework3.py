class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def check_out(self):
        pass


class members:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []

    def add_book(self, book):
        return self.books[book.isbn] 

    def add_member(self, member):
        return self.members[member.member_id] 

    def check_out_book(self, member_id, isbn):
        if member_id not in self.members or isbn not in self.books:
            print("Invalid member ID or ISBN.")
            return
        
    
class borrowed_books:
    def __init__(self):
        pass
    # datetime function
    