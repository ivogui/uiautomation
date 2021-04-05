from zikaow.Page.app import App



class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def teardown_class(self):
        self.testDriver.quit()

    def test_daily_login(self):
        self.testDriver.go_homepage().booksmall()
        self.testDriver.go_my_login().oneclicklogin()
