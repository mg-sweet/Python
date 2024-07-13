import random

name_list = ['Myat Pan', 'Kay Khaing', 'Kaung Zaw Shin','Thet Paing Htoo','Thazin Soe','Aung Myat Hein','Aung gf',
             'Su Su Naing','May Thet Phyu','Hnin Wutt Yi Zaw']

# Define the range of numbers you want to generate
start = 1
end = 10

# Generate non-repeating random numbers using random.sample()
random_numbers = random.sample(range(start, end + 1), end - start + 1)

# Print the generated random numbers
# print(random_numbers)
for num in range(10):
    print(f"{name_list[num]} : {random_numbers[num]}")