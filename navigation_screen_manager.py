from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        self.screen_stack.append(self.current)
        self.transition.direction = 'left'
        self.current = screen_name

    def pop(self):
        if self.screen_stack:
            self.transition.direction = 'right'
            self.current = self.screen_stack[-1]
            self.screen_stack.pop()

    def special_push(self, screen_name):
        self.transition.direction = 'left'
        self.current = screen_name