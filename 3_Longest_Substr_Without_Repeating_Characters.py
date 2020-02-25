def main():
    # _input = "abcabcbb"
    _input = "tmmzubt"

    currentSubstrDict = {}
    currentSubstrLength = 0
    currentSubstr = ""

    longestSubstrLength = 0
    longestSubstr = ""

    for i, x in enumerate(_input):
        if x not in currentSubstrDict:
            currentSubstrDict[x] = True 
            currentSubstrLength += 1
            currentSubstr += str(x)

            if currentSubstrLength > longestSubstrLength:
                longestSubstrLength = currentSubstrLength
                longestSubstr = currentSubstr
        else:
            letters_before_offender, index_of_match, index_of_match_in_substr = find_letters_before_offender(currentSubstr, i, x)
            
            # here need to remove only letters up to the char that the offender matched with
            for y in range(letters_before_offender):
                if index_of_match < y:
                    del currentSubstrDict[_input[y]]
                # if _input[index_of_match + y] == x:
                #     del currentSubstrDict[x]
            currentSubstrDict[x] = True
            # index_of_match_in_substr = 
            currentSubstr = currentSubstr[index_of_match_in_substr + 1:] + str(x)
            currentSubstrLength = len(currentSubstr)
    print(longestSubstr)

def find_letters_before_offender(s, current_index_in_whole_str, char):
    current_index_in_substr = -1
    for i, x in enumerate(s):
        if x == char:
            current_index_in_substr = i
    substr = s[::-1]
    letters_away = 1
    
    index_of_offenders_match = -1
    for x in substr:
        if x != char:
            letters_away += 1
            index_of_offenders_match = current_index_in_whole_str - letters_away
    return letters_away, index_of_offenders_match, current_index_in_substr

        
    



if __name__ == "__main__":
    main()