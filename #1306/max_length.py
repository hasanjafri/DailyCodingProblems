def length_longest_path(file_system_string):
    stack = []
    max_length = 0

    for i in range(0, len(file_system_string)):
        level = 0
        while file_system_string[i] == '\t':
            level += 1
            i += 1
        name = ""
        while i < len(file_system_string) and file_system_string[i] != '\n':
            name += file_system_string[i]
            i += 1
        while len(stack) > level:
            stack.pop()
        if "." in name:
            max_length = max(max_length, len("/".join(stack)) + len(name))
        else:
            stack.append(name)

    return max_length

if __name__ == '__main__':
    file_system_string = "dir \tsubdir1 \tsubdir2 \t\tfile.ext"
    print(length_longest_path(file_system_string)) # Output 20