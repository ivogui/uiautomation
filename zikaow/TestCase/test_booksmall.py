from zikaow.Page.app import App


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    def test_get_book_list(self):
        self.BooksMall.TextComparison()


    def teardown(self):
        self.BooksMall.books_back()

    def teardown_class(self):
        self.testDriver.quit()

