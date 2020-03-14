''' C-1.21
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
'''

lines = []
while True:
    try:
        line = input('Enter anything (ctrl-d to stop):')
        lines.append(line)
    except EOFError:
        break

print('\n'.join(reversed(lines)))
