import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sorting algorithm visualisation")

BLUE = (100, 149, 237)

class Datapoint:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def draw(self):
        pygame.draw.rect(WIN, BLUE, (self.index*10, 800-self.value, 9, self.value))

    def reposition(self, position_idx):
        pygame.draw.rect(WIN, BLUE, (position_idx*10, 800-self.value, 9, self.value))

def main():
    run = True
    clock = pygame.time.Clock()

    datapoints = []  # Initializing data points array

    # creating an array of data points
    for i in range(80):
        datapoints.append(Datapoint(random.randint(1, 70)*10, i))

    for i in range(len(datapoints)):
        min_idx = i  # min_idx is the index of the element with the minimal value
        for k in range(i + 1, len(datapoints)):
            if datapoints[min_idx].value > datapoints[k].value:
                min_idx = k

        datapoints[i], datapoints[min_idx] = datapoints[min_idx], datapoints[i]

    sort = False

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                sort = not sort

        if not sort:
            # drawing the data points, unsorted.
            for i in range(len(datapoints)):
                datapoints[i].draw()
        if sort:
            # drawing the data points, sorted.
            for i in range(len(datapoints)):
                datapoints[i].reposition(i)

        pygame.display.update()

    pygame.quit()


main()