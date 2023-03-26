import numpy as np
import matplotlib.pyplot as plt


def random_sprites():
    sprite = np.zeros((5, 5))
    for i in range(5):
        for j in range(5):
            sprite[i][j] = np.random.randint(0, 2)
    for i in range(5):
        sprite[i][:2] = sprite[i][3:][::-1]
    return sprite


map_sprite = np.zeros((100, 200))
for i in range(1, 50, 5):
    for j in range(1, 100, 5):
        map_sprite[i*2:i*2+5, j*2:j*2+5] = random_sprites()

plt.imshow(map_sprite)
plt.show()
