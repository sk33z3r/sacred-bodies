from PIL import Image, ImageDraw, ImageFont
from IPython.display import display
import random
import json
import os
import torch
import torchvision
import torchvision.transforms as T
import re
import argparse
import shutil

# check for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("total", help="Total number of images to generate", type=int)
parser.add_argument("-c", "--clear", help="Empty the generated directory", action="store_true")
parser.add_argument("--id", nargs=1, help="Specify starting ID for images", type=int)
args = parser.parse_args()

# Define amount of images to generate
TOTAL_IMAGES = args.total

genPath = "./images/generated"
dataPath = "./metadata"

# Remove directories if asked to
if args.clear:
    if os.path.exists(genPath):
        shutil.rmtree(genPath)
    if os.path.exists(dataPath):
        shutil.rmtree(dataPath)

# Make paths if they don't exist
if not os.path.exists(genPath):
    os.makedirs(genPath)
if not os.path.exists(dataPath):
    os.makedirs(dataPath)

# Set starting tokenId
if args.id:
    startingId = args.id[0]
else:
    startingId = 0

## Default credit for using hubblesite.org's images as outlined here: https://hubblesite.org/copyright
hubbleText = "Credit: NASA and the Space Telescope Science Institute (STScI)"
## Top level image directories
hubbleDir = "./images/source_layers/hubble"
chakraDir = "./images/source_layers/chakras"
## Match colors to chakra names
redDir = chakraDir + "/muladhara/"
orangeDir = chakraDir + "/svadhishtana/"
yellowDir = chakraDir + "/manipura/"
greenDir = chakraDir + "/anahata/"
blueDir = chakraDir + "/vishuddha/"
indigoDir = chakraDir + "/ajna/"
purpleDir = chakraDir + "/sahasrara/"
## Define hubble pieces
hubbleList = os.listdir(hubbleDir)
hubbleList.sort()

# Define image traits and give them weights
chakra = ["Muladhara", "Svadhishtana", "Manipura", "Anahata", "Vishuddha", "Ajna", "Sahasrara"]
chakra_weights = [20, 20, 15, 15, 15, 10, 5]

cover = ["Full", "Thin"]
cover_weights = [85, 15]

shape = ["Flower of Life", "Fruit of Life", "Merkaba", "Metatron's Cube", "Seed of Life", "Vesica Pisces"]
shape_weights = [10, 20, 35, 15, 15, 5]

opacity = ["50%", "35%"]
opacity_weights = [75, 25]

background = hubbleList
background_weights = [2, 2, 2, 4, 4, 2, 2, 4, 2, 6, 6, 2, 2, 4, 6, 4, 2, 6, 2, 4, 4, 6, 4, 2, 2, 2, 2, 2, 6, 2]

crop = ["Center", "Random"]
crop_weights = [15, 85]

# Correlate traits with filenames
chakra_paths = {
    "Muladhara": redDir,
    "Svadhishtana": orangeDir,
    "Manipura": yellowDir,
    "Anahata": greenDir,
    "Vishuddha": blueDir,
    "Ajna": indigoDir,
    "Sahasrara": purpleDir
}

cover_types = {
    "Full": "full",
    "Thin": "thin"
}

shape_files = {
    "Flower of Life": "flower_of_life",
    "Fruit of Life": "fruit_of_life",
    "Merkaba": "merkaba",
    "Metatron's Cube": "metatrons_cube",
    "Seed of Life": "seed_of_life",
    "Vesica Pisces": "vesica_pisces"
}

opacity_values = {
    "50%": 127,
    "35%": 90
}

def Convert(lst):
    res_dct = {lst[i]: lst[i] for i in range(0, len(lst))}
    return res_dct

background_files = Convert(hubbleList)

crop_values = {
    "Center": 0,
    "Random": 1
}

## Generate Traits

all_images = []

# A recursive function to generate unique image combinations
def create_new_image():

    # New, empty dictionary
    new_image = {}

    # For each trait category, select a random trait based on the weightings
    new_image ["Chakra"] = random.choices(chakra, chakra_weights)[0]
    new_image ["Cover"] = random.choices(cover, cover_weights)[0]
    new_image ["Shape"] = random.choices(shape, shape_weights)[0]
    new_image ["Opacity"] = random.choices(opacity, opacity_weights)[0]
    new_image ["Hubble Image"] = random.choices(background, background_weights)[0]
    new_image ["Crop Location"] = random.choices(crop, crop_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
for item in all_images:
    item["tokenId"] = startingId
    startingId = startingId + 1

print(all_images)

# Get Trait Counts
print("How many of each trait exist?")

chakra_count = {}
for item in chakra:
    chakra_count[item] = 0

cover_count = {}
for item in cover:
    cover_count[item] = 0

shape_count = {}
for item in shape:
    shape_count[item] = 0

opacity_count = {}
for item in opacity:
    opacity_count[item] = 0

background_count = {}
for item in background:
    background_count[item] = 0

crop_count = {}
for item in crop:
    crop_count[item] = 0

for image in all_images:
    chakra_count[image["Chakra"]] += 1
    cover_count[image["Cover"]] += 1
    shape_count[image["Shape"]] += 1
    opacity_count[image["Opacity"]] += 1
    background_count[image["Hubble Image"]] += 1
    crop_count[image["Crop Location"]] += 1

print(chakra_count)
print(cover_count)
print(shape_count)
print(opacity_count)
print(background_count)
print(crop_count)

#### Generate Images

# Center crop function
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

for item in all_images:

    # Define and convert images
    fgFile = Image.open(f'{chakra_paths[item["Chakra"]]}{cover_types[item["Cover"]]}-{shape_files[item["Shape"]]}.png').convert('RGBA')
    bgFile = Image.open(f'{hubbleDir}/{background_files[item["Hubble Image"]]}').convert('RGBA')
    # Define image text
    imgText1 = item["Shape"] + " - " + item["Chakra"]
    imgText2 = "Background cropped from \"" + os.path.splitext(background_files[item["Hubble Image"]])[0].replace("_", " ") + "\"\n" + hubbleText

    # Crop the background
    width, height = bgFile.size
    if crop_values[item["Crop Location"]] == 0:
        bgFileCrop = crop_center(bgFile, 798, 798)
    else:
        # crop somewhere random
        transform = T.RandomCrop(798)
        bgFileCrop = transform(bgFile)

    # Set foreground opacity if it's not thin
    if cover_types[item["Cover"]] == "full":
        data = fgFile.getdata()
        newData = []
        for value in data:
            if value[3] == 255:
                newData.append((value[0], value[1], value[2], opacity_values[item["Opacity"]]))
            elif value[3] < 255 and value[3] > 127:
                newData.append((value[0], value[1], value[2], (opacity_values[item["Opacity"]] - 30)))
            elif value[3] < 127 and value[3] > 64:
                newData.append((value[0], value[1], value[2], (opacity_values[item["Opacity"]] - 60)))
            elif value[3] < 64 and value[3] > 0:
                newData.append((value[0], value[1], value[2], (opacity_values[item["Opacity"]] - 80)))
            else:
                newData.append(value)
        fgFile.putdata(newData)
    else:
        pass

    # Create the composite image
    composite = Image.alpha_composite(bgFileCrop, fgFile)

    # Add image text
    title = ImageFont.truetype("./ttp.ttf", 14)
    credit = ImageFont.truetype("./ttp.ttf", 10)
    ImageDraw.Draw(composite).text((20, 20), imgText1, fill=(255, 255, 255), font=title)
    ImageDraw.Draw(composite).text((20, 758), imgText2, fill=(200, 200, 200), font=credit)

    #Convert to RGB
    rgb_im = composite.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save(genPath + "/" + file_name)
    print("Generated " + genPath + "/" + file_name)

#### Generate Metadata for all Traits

METADATA_FILE_NAME = dataPath + '/all-traits.json';
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)
