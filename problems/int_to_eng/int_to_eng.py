#solving:https://leetcode.com/problems/integer-to-english-words/
def complete_dictionary_teens(key,dictionary):
    aux_dict = {}
    for n in range(1,10):
        aux_dict[key+n] = dictionary[key] + " "+ dictionary[n]
    return aux_dict

def complete_dictionary_thousands(dictionary):
    aux_dict = {}
    for n in range(2,10):
        aux_dict[n*100] = dictionary[n] + " " + "Hundred"
        aux_dict[n*1000] = dictionary[n] + " " + "Thousand"

    return aux_dict

def create_word_dictionary():
    word_dict = {
            0: "Zero",
            1: "One",
            2 : "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "One Hundred",
            1000: "One Thousand",
            1000000: "One Million",
            1000000000: "One Billion",
            200: "Two Hundred",
            2000: "Two Thousand",
            2000000: "Two Million",
            2000000000: "Two Billion",



        }
    list_of_aux_dicts = []
    for key in word_dict:
        if key>19 and key !=100:
            aux_dict = complete_dictionary_teens(key,word_dict)
            list_of_aux_dicts.append(aux_dict)
    for aux_dictionary in list_of_aux_dicts:
        word_dict.update(aux_dictionary)
    hundreds = complete_dictionary_thousands(word_dict)
    word_dict.update(hundreds)
    return word_dict

def numberToWords(num:int)->str:
    """
    Convert non negative integer num to English word representation.
    
    :param num: The number. Greater equal than zero lesser equal than 2,147,483,646
    :type num: int
    :return: Description
    :rtype: str
    """
    if num==0:
        return "Zero"
    numbers_as_words_dict =create_word_dictionary()
    string_number = str(num)
    if num in numbers_as_words_dict:
        return numbers_as_words_dict[num]
    if len(string_number)==3:
        key_number = int(list(string_number)[0])*100
        key_number_rest = int(list(string_number)[1]  + list(string_number)[2])
        string = numbers_as_words_dict[key_number] + " " + numbers_as_words_dict[key_number_rest]
        return string
    if len(string_number)>3:
        string_number_as_list = list(string_number)
        first_three_pair = "".join(string_number_as_list[-3:]).lstrip("0")
        second_three_pair = "".join(string_number_as_list[-6:-3]).lstrip("0")
        third_three_pair = "".join(string_number_as_list[-9:-6]).lstrip("0")
        fourth_three_pair = "".join(string_number_as_list[-12:-9]).lstrip("0")

        first_string = numberToWords(int(fourth_three_pair)) + " " + "Billion"  if len(fourth_three_pair)>0 else ""
        second_string = numberToWords(int(third_three_pair)) + " " + "Million" if len(third_three_pair)>0 else ""
        third_string = numberToWords(int(second_three_pair))+ " " + "Thousand" if len(second_three_pair)>0 else ""
        fourth_string = numberToWords(int(first_three_pair)) if len(first_three_pair)>0 else ""
        all_strings = [first_string,second_string,third_string,fourth_string]
        all_strings = [x for x in all_strings if len(x)>0]
        final_string = (" ").join(all_strings)

        return final_string.strip(" ")


#number = 1 000 010
number = 1000010
words = numberToWords(number)
print(f"The number {number} is read {words}")