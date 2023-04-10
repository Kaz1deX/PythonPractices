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


my_sprite = random_sprites()
plt.imshow(my_sprite)
plt.show()
