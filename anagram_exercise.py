from collections import Counter # Import needed to count the frequency of characters in the first function
import asyncio
import hashlib
import os

def words_anagrams(word1, word2): # function defined that takes arguements to compare two words
    word1 = word1.lower().replace(" ", "") # .lower and .replace methods standardizes the variables and removes whitespace
    word2 = word2.lower().replace(" ", "")
    
    return Counter(word1) == Counter(word2) # Counter class compares the frequency of letters in the words

word1 = "duty" # Sets word variables to specific strings for use in the "if" statement
word2 = "stud"

if words_anagrams(word1, word2): # redifined variables are passed in and printed to a string
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

# defining a function named 'sum_even_numbers'. This function accepts
# one argument, which is a list of numbers so we can iterate.
def sum_even_numbers(numbers): 
    return sum(num for num in numbers if num % 2 == 0)
# outside the function scope, we define a list of numbers that we want to add up.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# We call our 'sum_even_numbers' function, passing in our list of numbers. The 
# function will return the sum of the even numbers. We store this 
# returned value in a variable named result.
result = sum_even_numbers(numbers)
# We use a string function to calculate the sum of the even numbers and then we use a comma to separate this 
# string from the actual result. Python's 'print' function automatically inserts 
# a space where the comma is.
print("Even number sum is:", result)


# Define a function to calculate the SHA-256 hash of 2 images in a root directory folder.
def calculate_image_hashes(folder_path):
# Create a dictionary to store the hashes of the images. 
    image_hashes = {}
# Used os.walk to iterate over each file in the folder_path directory.
# This part of the code iterates over every file in the current directory, 
# generates the full path to each file, and calculates the SHA-256 hash for each file.
# The hash is a unique identifier for the file content and can compare if two files are identical.
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = calculate_sha256_hash(file_path)
            if hash_value in image_hashes:
                image_hashes[hash_value].append(file_path)
            else:
                image_hashes[hash_value] = [file_path]
    return image_hashes
# Define a function to calculate the SHA-256 hash of a given file.
def calculate_sha256_hash(file_path):
    hasher = hashlib.sha256()
    # Open the file specified by file_path in binary mode ('rb'). 'with' keyword is used to 
    # ensure that the file is properly closed after it is no longer needed.
    with open(file_path, 'rb') as file:
        # Read the file chunk by chunk (each chunk is 4096 bytes) to efficiently handle large files 
        # that may not fit in memory. The iter() function is used with a lambda function that reads 
        # the chunk from the file, and an end value of '' to continue reading until the end of the file.
        for chunk in iter(lambda: file.read(4096), b''):
            # Update the hash object with the chunk of data read from the file.
            hasher.update(chunk)
    # Return the hexadecimal digest of the hash object, this is a string representing the hash 
    # of the input file, which can be used for comparing with other hashes.
    return hasher.hexdigest()
# Define a function to check if two images are identical.
def are_images_same(image1_path, image2_path):
    hash1 = calculate_sha256_hash(image1_path)
    hash2 = calculate_sha256_hash(image2_path)
    return hash1 == hash2
folder_path = "/Users/jon/Desktop/Photo_Comparison"
# Set the path to the directory containing the images to compare.folder_path = "/Users/jon/Desktop/Photo_Comparison"
image_hashes = calculate_image_hashes(folder_path)
# Calculate the SHA-256 hashes for all images in the specified directory 
# and store them in 'image_hashes' dictionary.
image1_path = "/Users/jon/Desktop/Photo_Comparison/IMG_0770.JPG"
image2_path = "/Users/jon/Desktop/Photo_Comparison/IMG_07701.JPG"
# Use the 'are_images_same' function to compare the two specified images. 
# The function returns True if the images are identical (based on their SHA-256 hashes), 
# and False otherwise. The result is stored in the variable 'same_images'.
same_images = are_images_same(image1_path, image2_path)
# Based on the result of the image comparison, print a message to the user.
# If the images are the same (same_images == True), print "The images are the same."
# If the images are not the same (same_images == False), print "The images are not the same."
if same_images:
    print("The images are the same.")
else:
    print("The images are not the same.")