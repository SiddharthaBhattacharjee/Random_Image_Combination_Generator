import os
import random
from PIL import Image

# Define the paths of the four folders
background_folder = 'background/'
body_folder = 'body/'
head_folder = 'head/'
pet_folder = 'pet/'

# Define the output folder path
output_folder = 'generated/'

# Get a list of file names from each folder
background_files = os.listdir(background_folder)
body_files = os.listdir(body_folder)
head_files = os.listdir(head_folder)
pet_files = os.listdir(pet_folder)

# Set the number of images to generate
num_images = 100

# Generate the images
for i in range(num_images):
    # Randomly select a file from each folder
    background_file = random.choice(background_files)
    body_file = random.choice(body_files)
    head_file = random.choice(head_files)
    pet_file = random.choice(pet_files)

    # Open the four PNG files and combine them using Pillow
    background = Image.open(background_folder + background_file)
    body = Image.open(body_folder + body_file)
    head = Image.open(head_folder + head_file)
    pet = Image.open(pet_folder + pet_file)
    
    combined = Image.alpha_composite(background, body)
    combined = Image.alpha_composite(combined, head)
    combined = Image.alpha_composite(combined, pet)

    # Save the generated image to the output folder
    output_path = output_folder + f'image_{i+1}.png'
    combined.save(output_path)

    print(f'Generated image {i+1}/{num_images}...')
