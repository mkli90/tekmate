# -*- encoding: utf-8 -*-

from tekmate.configuration import PyGameInitializer, TekmateFactory
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)
    initializer = PyGameInitializer({"display_width": 1024, "display_height": 576})
    game_factory = TekmateFactory(initializer)
    game = game_factory.create()
    game.enter_mainloop()

if __name__ == "__main__":
    main()
