from zikaow.Page.app import App


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()
        self.loginPage = self.testDriver.go_my_login()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    def test(self):
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        self.testDriver.quit()

