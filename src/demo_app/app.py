from ngapp.app import App
from ngapp.components import *

class DemoApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = Heading("Demo App")
        self.button = QBtn("Click me", ui_color="primary")
        self.counter_view = QInput(ui_model_value=0,
                                   ui_style="width: 200px;")
        self.button.on_click(self.increment_counter)
        self.component = Centered(
            self.title,
            self.button,
            self.counter_view,
            ui_style="padding-top: 50px;"
        )

    def increment_counter(self):
        self.counter_view.ui_model_value = int(self.counter_view.ui_model_value) + 1
