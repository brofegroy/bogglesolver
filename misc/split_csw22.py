words = []

with open("raw/csw22_no_Qs.txt") as file:
    words = [word.strip() for word in file.readlines()]

for x in range (3,17):
    Q_letter_words = [word for word in words if len(word)==x]

    with open(f"output\csw22_{x}s.txt", "w") as output_file:
        for word in Q_letter_words:
            output_file.write(word + '\n')