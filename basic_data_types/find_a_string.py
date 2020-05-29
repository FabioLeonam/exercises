def count_substring(string, sub_string):
    occurences = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            occurences += 1
    return occurences

    
if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    count = count_substring(string, sub_string)
    print(count)