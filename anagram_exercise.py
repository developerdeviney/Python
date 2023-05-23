import asyncio
import aiohttp
import json
import hashlib
import os

def words_anagrams(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    return sorted(word1) == sorted(word2)

word1 = "duty"
word2 = "stud"

if words_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

def sum_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]

    sum_even = sum(even_numbers)

    return sum_even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers)
print("Even number sum is:", result)


def calculate_image_hashes(folder_path):
    image_hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = calculate_sha256_hash(file_path)
            if hash_value in image_hashes:
                image_hashes[hash_value].append(file_path)
            else:
                image_hashes[hash_value] = [file_path]
    return image_hashes

def calculate_sha256_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def are_images_same(image1_path, image2_path):
    hash1 = calculate_sha256_hash(image1_path)
    hash2 = calculate_sha256_hash(image2_path)
    return hash1 == hash2

# Example usage:
folder_path = "/Users/jon/Desktop/Photo_Comparison"
image_hashes = calculate_image_hashes(folder_path)

image1_path = "/Users/jon/Desktop/Photo_Comparison/IMG_0770.JPG"
image2_path = "/Users/jon/Desktop/Photo_Comparison/IMG_07701.JPG"
same_images = are_images_same(image1_path, image2_path)

if same_images:
    print("The images are the same.")
else:
    print("The images are not the same.")