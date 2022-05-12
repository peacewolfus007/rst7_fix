testsite_array = []
with open('a.rst7') as my_file:
    for line in my_file:
        testsite_array.append(line)

def replace_char_at_index(org_str, index, replacement):
    ''' Replace character at index in string org_str with the
    given replacement character.'''
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str

sample_str = "This is a sample string"
# Replace character at 3rd index position
sample_str = replace_char_at_index(sample_str, 13, 'sss')
print(sample_str)

for x in range(len(testsite_array)):
    testsite_array[x]=replace_char_at_index(testsite_array[x], 13, '   ')
    testsite_array[x]=replace_char_at_index(testsite_array[x], 26, '   ')
    testsite_array[x]=replace_char_at_index(testsite_array[x], 64, '   ')
    #testsite_array[x]=replace_char_at_index(testsite_array[x], 56, '')
    #testsite_array[x]=replace_char_at_index(testsite_array[x], 65, '   ')



with open("text.txt", 'w') as file:
    file.write(''.join(testsite_array))