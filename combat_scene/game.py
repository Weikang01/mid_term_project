import pygame
from combat_scene.network import Network


class Game:
    def __init__(self):
        self.net = Network()
        self.width = 500
        self.height = 500
        self.player = Player()
        self.player2 = Player()
        self.canvas = Canvas(self.width, self.height, 'Diamond Warrior')

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.K_ESCAPE:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.player.move(1)

            self.canvas.draw_background()
            self.player.draw(self.canvas.get_canvas())
            self.player2.draw(self.canvas.get_canvas())
            self.canvas.update()
        pygame.quit()

    def send_data(self):
        # data = player id: action id: position.x, position.y   "0-0:155,230"
        # action id: 0: movement
        #            1: attack
        data = str(self.net.id) + ":" + str(self.player.x) + "," + str(self.player.y)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0, 0


class Canvas:
    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0, 0, 0))

        self.screen.draw(render, (x, y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((0, 0, 0))
