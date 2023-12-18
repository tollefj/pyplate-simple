from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def run(self):
        pass


class MyPlugin(Plugin):
    def run(self):
        print("Running MyPlugin...")


class AnotherPlugin(Plugin):
    def run(self):
        print("Running AnotherPlugin...")


# Plugin registration
plugins = [MyPlugin(), AnotherPlugin()]

# Execute all registered plugins
for plugin in plugins:
    plugin.run()
