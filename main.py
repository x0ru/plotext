import plotext as plt
path = 'istockphoto-1361394182-1024x1024.jpg'
plt.download(plt.test_image_url, path)
plt.image_plot(path)
plt.title("A very Cute Cat")
plt.show()
plt.delete_file(path)