from typing import Dict, Any


class GameEventException(Exception):
    """Exception raised to signal that a game-related event has occurred."""

    def __init__(self, event_type: str, details: Dict[str, Any]) -> None:
        """
        Initialize the game event exception.
        """
        self.event_type: str = event_type
        self.details: Dict[str, Any] = details
        super().__init__(f"Game Event Occurred: {event_type}")

    def __str__(self) -> str:
        """Return a readable string representation of the game event."""
        return f"Event: {self.event_type}. Details {self.details}"


class InsufficientResourcesException(Exception):
    """Exception raised when the player does not have enough resources to perform an action."""

    def __init__(
            self,
            required_resource: str,
            required_amount: int,
            current_amount: int
    ) -> None:
        """
        Initialize the insufficient resources exception.

        """
        self.required_resource: str = required_resource
        self.required_amount: int = required_amount
        self.current_amount: int = current_amount

        super().__init__(
            f"Not enough {required_resource}: "
            f"need {required_amount}, have {current_amount}"
        )


class Game:
    """Represents a simple game model with player stats and actions."""

    def __init__(self) -> None:
        """Initialize player attributes."""
        self.player_level: int = 1
        self.player_health: int = 100
        self.mana: int = 30

    def take_damage(self, damage: int, source: str) -> None:
        """
        Apply damage to the player.
        """
        self.player_health -= damage
        if self.player_health <= 0:
            raise GameEventException("death", {
                "cause": source,
                "damage": damage,
                "final_health": self.player_health
            })

    def gain_experience(self, xp: int) -> None:
        """
        Increase experience and possibly level up the player.
        """
        if xp > 50:
            self.player_level += 1
            raise GameEventException("levelUp", {
                "new_level": self.player_level,
                "xp_gained": xp,
            })

    def cast_spell(self, mana_cost: int) -> None:
        """
        Attempt to cast a spell that costs mana.
        """
        if self.mana < mana_cost:
            raise InsufficientResourcesException(
                "mana",
                mana_cost,
                self.mana
            )
        self.mana -= mana_cost


game = Game()

try:
    game.gain_experience(100)
    game.take_damage(150, "dragon")
    game.cast_spell(50)

except InsufficientResourcesException as e:
    print(e)

except GameEventException as e:
    print(e)
