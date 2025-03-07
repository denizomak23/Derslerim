for i in range(1, 11):
    filename = f"file_{i}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file number {i}\n")
    