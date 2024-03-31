import heapq
from collections import defaultdict
import math
from tabulate import tabulate



def huffman_tree(frequency_of_occurrence):
    h = [[weight, [char, ""]] for char, weight in frequency_of_occurrence.items()]
    heapq.heapify(h)
    while len(h) > 1:
        lo = heapq.heappop(h)
        hi = heapq.heappop(h)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(h, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return h[0][1:]
# *********************************************************DONE**************************************************

def huffman_coding(story):
    # Creating a defaultdict with a default value of 0 for nonexistent keys
    frequency_of_occurrence = defaultdict(int)

    # Updating the count for each character in the input text
    for char in story.upper():
# if char in valid_characters:
          frequency_of_occurrence[char] += 1
    # value = frequency counts (how many times each character appears in the text).
    total_chars = sum(freq for freq in frequency_of_occurrence.values())

    probabilities = {}

    for char, count in frequency_of_occurrence.items():
        probability = count / total_chars
        probabilities[char] = probability#adds a key-value pair to the probabilities dictionary. The key is the character (char), and the value is the calculated probability.

    huffmantree = huffman_tree(frequency_of_occurrence)
    huffman_codes = {}
    for char, code in huffmantree:
        huffman_codes[char] = code

    return frequency_of_occurrence, total_chars, probabilities, huffman_codes


def entropy_calc(probabilities):
    entropy = 0
    for prob in probabilities:
        entropy += prob * (-(math.log2(prob)))
    return entropy


def huffman_bits_perchar(probabilities, huffman_codes, frequency_of_occurrence):

    total = 0
    for char in frequency_of_occurrence.keys():
        total += probabilities[char] * len(huffman_codes[char])
    return total


def total_huffman_bitsfunction( huffman_codes, frequency_of_occurrence):
    total = 0
    for char in frequency_of_occurrence.keys():
        total += len(huffman_codes[char]) * frequency_of_occurrence[char]
    return total

def bits_needed(total_chars):
    return total_chars * 8



        # Read the story
with open("story2.txt", "r", encoding="utf-8") as file:
    story = file.read().upper().replace('\n' , '')

    # perform Huffman coding
    #frequency_of_occurrence, total_chars, probabilities, huffman_codes = huffman_coding(story)
    result = huffman_coding(story)
    frequency_of_occurrence = result[0]
    total_chars = result[1]
    probabilities = result[2]
    huffman_codes = result[3]




    print("***************************-> Final Result: <-********************************")

    print("\n total char :", total_chars)

    entropy = entropy_calc(probabilities.values())
    print(" Entropy of the alphabet: ",round( entropy,4), "Bits/character ")

    total_huffman_bits_per_char = huffman_bits_perchar(probabilities, huffman_codes, frequency_of_occurrence)
    print(" Average number of bits/character using Huffman code: ", round(total_huffman_bits_per_char, 4), "Bits/character ")


    print(f" Compression ratio (Entropy to Huffman bits): {(entropy / total_huffman_bits_per_char)*100:.2f}%")



    nascci_bits = bits_needed(total_chars)
    print(" Number of bits needed using ASCII encoding: ", nascci_bits,"Bits ")

    Nhuffman =total_huffman_bitsfunction( huffman_codes, frequency_of_occurrence)
    print( " Total number of bits needed using Huffman code:  ", round(Nhuffman,4), "Bits ")

    percentage_of_compression = (Nhuffman / nascci_bits)
    print(" Percentage of compression compared to ASCII code: " + str(round(percentage_of_compression*100, 4))+"%")


    print(" -----------------------------------------------------------------------------")


    scharacters = {'A', 'B', 'C', 'D', 'E', 'F', 'M', 'Z', ' ', '.'}
    chtable = sorted(
        [(char, freq, round(probabilities[char], 4), huffman_codes[char], len(huffman_codes[char])) for char, freq in frequency_of_occurrence.items()if char in scharacters])
    print(tabulate(chtable, headers=["Character", "Frequency", "Probability", "Huffman Code", "Code Length"],
                   tablefmt="pipe", colalign=("center", "center", "center", "center", "center")))

    print(" -----------------------------------------------------------------------------")

