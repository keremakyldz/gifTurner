import imageio

im = imageio.imread("Astronaut.png")

imageio.imwrite("Astronaut.jpg",im[:,:, 0])
