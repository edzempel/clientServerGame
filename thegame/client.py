# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame

pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x = in_window(self.x - self.vel)

        if keys[pygame.K_RIGHT]:
            self.x = in_window(self.x + self.vel)

        if keys[pygame.K_UP]:
            self.y = in_window(self.y - self.vel)

        if keys[pygame.K_DOWN]:
            self.y = in_window(self.y + self.vel)

        self.rect = (self.x, self.y, self.width, self.height)


def in_window(val):
    val = min(400, val)
    val = max(0, val)
    return val


def redraw_window(win, player: Player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

        p.move()
        redraw_window(win, p)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
