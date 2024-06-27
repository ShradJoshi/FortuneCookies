import random

lucky_number = random.randint(1, 100)
fortune_number = random.randint(1, 3)
fortune_text = ''

if fortune_number == 1:
    fortune_text = "You will find your IKIGAI"
if fortune_number == 2:
    fortune_text = "You will feel alive and inspired"
if fortune_number == 3:
    fortune_text = "You will be make 80,000 a year"

print(f"{fortune_text}! Your lucky number is:{lucky_number}")
