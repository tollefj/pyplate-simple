from time import sleep

from tqdm import tqdm, trange

# Basic progress bar
for i in tqdm(range(10)):
    sleep(0.1)

# Custom description and unit
for i in tqdm(range(10), desc="Processing", unit="item"):
    sleep(0.1)

# Progress bar for file download simulation
total_file_size = 1024
with tqdm(
    total=total_file_size, unit="B", unit_scale=True, unit_divisor=1024
) as progress_bar:
    for chunk_size in range(0, total_file_size, 128):
        sleep(0.1)
        progress_bar.update(128)

# Nested progress bars
for i in trange(3, desc="Outer"):
    for j in trange(5, desc="Inner", leave=False):
        sleep(0.1)
