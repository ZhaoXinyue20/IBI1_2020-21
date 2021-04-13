def reverse_complement_calculator(sequence):
    """
    Input: a DNA sequence
    Returns: the reverse complementary strand of the input DNA
    """
    sequence = sequence.upper() #capitalize all letters
    sequence = sequence.replace('A', 't')
    sequence = sequence.replace('T', 'a')
    sequence = sequence.replace('C', 'g')
    sequence = sequence.replace('G', 'c')
    sequence = sequence.upper()
    return sequence[::-1] #make the reverse sequence
# test sequence:AAttCCgg
reverse_complement_calculator("AAttCCgg")

