class GameStats:
    """Отслеживание статистики"""

    def __init__(self, ai_game):
        """Инициазириует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
    def reset_stats(self):
        """Инициализирует статистику, изменяюшуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit