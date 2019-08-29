'''
RULES:
-the first charachter of the string should remain the same
-every other occurence of the first character in a string should be replaced with a dollar sign
-if the length of the string is less than 4 then do nothing

TEST DATA
avacado - av$c$do
apple - apple
mom - mom
smarts - smart$

'''


def replace_occurences_of_first_character_with_dollar_symbol(p_string):
    if len(p_string) < 4:
        return p_string
    first_character = p_string[0]
    remaining_string = p_string[1:]
    converted_string = remaining_string.replace(first_character, '$')
    return first_character + converted_string


def test_single_occurence_is_replaced_by_dollar():
    assert 'smart$' == replace_occurences_of_first_character_with_dollar_symbol('smarts')

def test_multiple_occurences_replaced_by_dollar():
    assert 'av$c$do' == replace_occurences_of_first_character_with_dollar_symbol('avacado')

def test_no_reoccurences_of_first_charachter_returns_same_string():
    assert 'apple' == replace_occurences_of_first_character_with_dollar_symbol('apple')

def test_when_len_less_than_4_chars_return_unchanged_string():
    assert 'mom' == replace_occurences_of_first_character_with_dollar_symbol('mom')
