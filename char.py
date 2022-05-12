#tried this command (min1. in downloaded from here: https://ambermd.org/tutorials/basic/tutorial3/files/min1.in) :
#sander -O -i min1.in -o min1.out -p a.prmtop -c text.txt -r min1.ncrst
#text.txt is fixed of a.rst7 file


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
#sample_str = replace_char_at_index(sample_str, 13, 'sss')
#print(sample_str)
print(f"\n before text :\n{testsite_array[5155]}")
for x in range(571,5181,1):
    
    testsite_array[x]=replace_char_at_index(testsite_array[x], 12, ' ')
    testsite_array[x]=replace_char_at_index(testsite_array[x], 23, ' ')
    testsite_array[x]=replace_char_at_index(testsite_array[x], 36, ' ')
    testsite_array[x]=replace_char_at_index(testsite_array[x], 60, ' ')
    #testsite_array[x]=replace_char_at_index(testsite_array[x], 56, '')
    #testsite_array[x]=replace_char_at_index(testsite_array[x], 65, '   ')
print(f"\n after text:\n{testsite_array[5155]}")



with open("text.txt", 'w') as file:
    file.write(''.join(testsite_array))
