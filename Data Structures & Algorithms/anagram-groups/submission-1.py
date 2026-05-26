class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            anagrams = {}
            for s in strs:
                key = "".join(sorted(s))

                if key in anagrams:
                    anagrams[key].append(s)
                else:
                    anagrams[key] = [s]
            
            return list(anagrams.values())


    """
    Whats my solution to this problem?
    Step 1: Create a hash map where each key is the sorted string and the values are a list 
    of strings that sort to that sorted string
    Step 2: iterate over each string -> sort it -> if its sorted string does not exist as a key
    in our dict then lets add that sorted string as a new key with a list as its value and add the original string
    Step 3: do this again if the sorted verison of teh string exists append it to the respective keys list. 
    Step 4: At the end after iterating over every string. Convert the dict into a list appending each value of each key 
    return that list

    Edge Cases:
    if the input is one item/string just return a list with that string inside another list.

    """

       