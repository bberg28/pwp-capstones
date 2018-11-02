class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        print("Updating email address from {old_email} to {new_email".format(old_email=self.email,new_email=address))
        self.email = address

    def __repr__(self):
        print("User {user_name}, email: {email}, books read: {num_read}".format(user_name=self.name, email=self.email, num_read=len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user and self.email == other_user:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        count = 0
        score = 0
        for item in self.books.keys():
            count += 1
            if self.books[item] is not None:
                score += self.books[item]
        avg_value = score/count
        return avg_value

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "{title} with ISBN {isbn}".format(title=self.title, isbn=self.isbn)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, update_isbn):
        print("Updating ISBN number from {old_isbn} to {new_isbn}".format(old_isbn=self.isbn, new_isbn=update_isbn))

    def add_rating(self, rating_score):
        if rating_score >= 0 and rating_score <= 4:
            self.ratings.append(rating_score)
        else:
            print("Invalid rating! Rating must be from 0 to 4")

    def __eq__(self, other):
        if self.title == other and self.isbn == other:
            return True
        else:
            return False

    def get_average_rating(self):
        aggregate_rating = 0
        for value in self.ratings:
            aggregate_rating += value
        if len(self.ratings) == 0 or aggregate_rating == 0:
            avg_rating = 0
        else:
            avg_rating = aggregate_rating/len(self.ratings)
        return avg_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        my_book = Book(title, isbn)
        return my_book

    def create_novel(self, title, author, isbn):
        my_novel = Fiction(title, author, isbn)
        return my_novel

    def create_non_fiction(self, title, subject, level, isbn):
        my_non_fiction = Non_Fiction(title, subject, level, isbn)
        return my_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book,rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}".format(email=email))

    def add_user(self, name, email, user_books=None):
        my_user = User(name, email)
        self.users[email] = my_user

        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        highest_name = ""
        highest_read_count = 0

        for book in self.books.keys():
            if self.books[book].get() > highest_read_count:
                highest_name = book.title
                highest_read_count = self.books[book].get()
        print("The most read book is {name}, with a read count of {count}.".format(name=highest_name, count=highest_read_count))

    def highest_rated_book(self):
        highest_avg_name = ""
        highest_avg_rating = 0

        for book in self.books.keys():
            if book.get_average_rating() > highest_avg_rating:
                highest_avg_rating = book.get_average_rating()
                highest_avg_name = book.title
        print("The book with highest rating is {name}, with an average rating of {rating}".format(name=highest_avg_name, rating=highest_avg_rating))

    def most_positive_user(self):
        highest_avg_rating = 0
        highest_name = ""

        for user in self.users.values():
            my_avg = user.get_average_rating()
            if  my_avg > highest_avg_rating:
                highest_avg_rating = my_avg
                highest_name = user.name
        print("The most positive user is {name}, with an average rating of {rating}".format(name=highest_name, rating=highest_avg_rating))

    def get_most_read_book(self):
        high_read_count = 0
        high_read_name = ""
        for book in self.books.keys():
            if self.books[book] > high_read_count:
                high_read_count = self.books[book]
                high_read_name = book.title
        print("The book with highest read count is {name}".format(name=high_read_name))
