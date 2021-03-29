def read_from_file(filename, count):
    words_list = list()
    with open(filename) as file_handle:
        i = 1
        for line in file_handle:
            splitted_line = line.split()
            for word in splitted_line:
                words_list.append(word)
                if i == count:
                    return words_list
                i += 1
