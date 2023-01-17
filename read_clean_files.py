
def read_lines_and_create_set(file_path):
    id_set = set()
    with open(file_path, "r") as f:
        for line in f:
            id1 = line.strip().split("|")[0]
            id_set.add(id1)
    return id_set


def remove_lines(file1_path, file2_path, output_path):
    id_set = read_lines_and_create_set(file2_path)
    with open(file1_path, "r") as file1, open(output_path, "w") as output:
        for line in file1:
            id1 = line.strip().split("|")[0]
            if id1 not in id_set:
                output.write(line)


