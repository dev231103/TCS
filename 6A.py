import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from minisom import MiniSom

iris = datasets.load_iris()
iris_data = iris.data
iris_label = iris.target
iris_data = iris_data[:, :2]

som = MiniSom(x=3, y=1, input_len=2, random_seed=1234)
som.train(iris_data, 100)

predictions = [som.winner(x) for x in iris_data]

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(5, 7))
x = iris_data[:, 0]
y = iris_data[:, 1]
colors = ['red', 'green', 'blue']

ax[0].scatter(x, y, c=iris_label, cmap=ListedColormap(colors))
ax[0].title.set_text('Actual Classes')

pred_labels = [prediction[0] for prediction in predictions]
ax[1].scatter(x, y, c=pred_labels, cmap=ListedColormap(colors))
ax[1].title.set_text('SOM Predictions')

plt.show()

