import pygame


class PlanetCard:
    def __init__(self, name, description, price=6, chips=0, mult=0, image=None, isActive=False):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)

# TODO (TASK 6.1): Implement the Planet Card system for Balatro.
#   Create a dictionary called PLANETS that stores all available PlanetCard objects.
#   Each entry should use the planet's name as the key and a PlanetCard instance as the value.
#   Each PlanetCard must include:
#       - name: the planet's name (e.g., "Mars")
#       - description: the hand it levels up or affects
#       - price: how much it costs to purchase
#       - chips: the chip bonus it provides
#       - mult: the multiplier it applies
#   Example structure:
#       "Gusty Garden": PlanetCard("Gusty Garden", "levels up galaxy", 6, 15, 7)
#   Include all planets up to "Sun" to complete the set.
#   These cards will be used in the shop and gameplay systems to upgrade specific poker hands.

PLANETS = {
    'Mercury': PlanetCard(
        "Mercury",
        "Increases High Card hand value",
        2,
        10,
        1,
        image = pygame.image.load('../graphics/cards/Planets/PlanetMercury.png'),
        isActive = True
    ),
    'Venus': PlanetCard(
        "Venus",
        "Increases One Pair hand value",
        2,
        15,
        1,
        image = pygame.image.load('../graphics/cards/Planets/PlanetVenus.png'),
        isActive = True
    ),
    'Earth': PlanetCard(
        "Earth",
        "Increases Two Pair hand value",
        2,
        15,
        2,
        image = pygame.image.load('../graphics/cards/Planets/PlanetEarth.png'),
        isActive = True
    ),
    'Mars': PlanetCard(
        "Mars",
        "Increases Three Of a Kind hand value",
        2,
        25,
        2,
        image = pygame.image.load('../graphics/cards/Planets/PlanetMars.png'),
        isActive = True
    ),
    'Jupiter': PlanetCard(
        "Jupiter",
        "Increases Straight hand value",
        3,
        25,
        3,
        image = pygame.image.load('../graphics/cards/Planets/PlanetJupiter.png'),
        isActive = True
    ),
    'Saturn': PlanetCard(
        'Saturn',
        "Increases Flush hand value",
        3,
        30,
        3,
        image = pygame.image.load('../graphics/cards/Planets/PlanetSaturn.png'),
        isActive = True
    ),
    'Uranus': PlanetCard(
        "Uranus",
        "Increases Full House hand value",
        3,
        35,
        3,
        image = pygame.image.load('../graphics/cards/Planets/PlanetUranus.png'),
        isActive = True
    ),
    'Neptune': PlanetCard(
        "Neptune",
        "Increases Four Of a Kind hand value",
        3,
        40,
        4,
        image = pygame.image.load('../graphics/cards/Planets/PlanetNeptune.png'),
        isActive = True
    ),
    'Sun': PlanetCard(
        "Sun",
        "Increases all hands value",
        12,
        30,
        2,
        image = pygame.image.load('../graphics/cards/Planets/PlanetSun.png'),
        isActive = True
    )
}
