################################################################################
####################### ------ ALIEN INVASION ------ ###########################
################################################################################

# In Alien Invasion, the player controls a ship that appears at
# the bottom center of the screen. The player can move the ship
# right and left using the arrow keys and shoot bullets using the
# spacebar. When the game begins, a fleet of aliens fills the sky
# and moves across and down the screen. The player shoots and
# destroys the aliens. If the player shoots all the aliens, a new fleet
# appears that moves faster than the previous fleet. If any alien hits 
# the player’s ship or reaches the bottom of the screen, the player
# loses a ship. If the player loses three ships, the game ends.

import pygame
from pygame.sprite import Group

from ship import Ship
from button import Button
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play btton.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)

run_game()
