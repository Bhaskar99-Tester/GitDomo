
with open('text.txt', 'r') as reader:
    pot = reader.readlines()
    reversed(pot)
    with open('text.txt','w') as writer:

        for line in reversed(pot):
            writer.write(line)


