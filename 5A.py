import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm

# Load the first image
im = Image.open(r"C:\Users\Rohsn Chimbaikar\Downloads\Practical files-20241228T184052Z-001\Practical files\me.jpeg")
size = 64, 64
im.thumbnail(size, Image.Resampling.LANCZOS)
im_np = np.asarray(im)
im_np = np.where(im_np < 128, -1, 1)

# Display the first image
plt.imshow(im_np, cmap='gray')
plt.title("Original Image")
plt.show()

N = im_np.shape[0] * im_np.shape[1]
P = 1
N_sqrt = int(np.sqrt(N))
NO_OF_ITERATIONS = 10
im_np = im_np.reshape(1, N)
epsilon = im_np
epsilon.reshape(N_sqrt, N_sqrt)

# Load the masked image
im = Image.open(r'C:\Users\Rohsn Chimbaikar\Downloads\Practical files-20241228T184052Z-001\Practical files\me_half_masked.jpeg')
im.thumbnail(size,Image.Resampling.LANCZOS)
im_masked_np = np.asarray(im)

# Handle potential color channels
try:
    im_masked_np = im_masked_np[:, :, 0]
except IndexError:
    pass

im_masked_np = np.where(im_masked_np < 128, -1, 1)
im_masked_np = im_masked_np.reshape(1, N)
test_array = im_masked_np

# Display the masked image
plt.imshow(test_array.reshape(N_sqrt, N_sqrt), cmap='gray')
plt.title("Masked Image")
plt.show()

# Initialize weight matrix and bias
w = np.zeros((N, N))
h = np.zeros((N))

# Train the Hopfield network
for i in tqdm(range(N), desc="Training weights"):
    for j in range(N):
        w[i, j] = epsilon[0, i] * epsilon[0, j]
        if i == j:
            w[i, j] = 0
w /= N

# Display the weight matrix
plt.imshow(w, cmap='hot')
plt.title("Weight Matrix")
plt.show()

# Initialize hamming distance tracking
hamming_distance = np.zeros((NO_OF_ITERATIONS, 1))

# Iteratively update the test array
fig = plt.figure(figsize=(8, 8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)

for iteration in tqdm(range(NO_OF_ITERATIONS), desc="Updating test array"):
    for i in range(N):
        idx = np.random.randint(N)
        h[idx] = 0
        for j in range(N):
            h[idx] += w[idx, j] * test_array[0, j]
        test_array[0, idx] = 1 if h[idx] >= 0 else -1

    hamming_distance[iteration, 0] = ((epsilon - test_array) != 0).sum()
    plt.subplot(4, 3, iteration + 1)
    plt.imshow(np.where(test_array.reshape(N_sqrt, N_sqrt) < 1, 0, 256), cmap='gray')
    plt.title(f"Iteration {iteration + 1}")

# Display Hamming distances over iterations
plt.show()

fig = plt.figure(figsize=(8, 8))
plt.plot(hamming_distance)
plt.xlabel('Number of Iterations')
plt.ylabel('Hamming Distance')
plt.ylim([0, N])
plt.title("Hamming Distance Over Iterations")
plt.show()
