class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # so first we want to create a dictionary with the deafult values being a list
        # Then we want to basically give each key in the dictionary a signuatreue
        # of how frequent a specific character arizes
        # the values would then just be the words

        dicts = defaultdict(list)

        for word in strs:
            count = [0] * 26 # creating a bucket for each character

            for let in word:
                count[ord(let) - ord('a')] += 1
            
            dicts[tuple(count)].append(word)

        return list(dicts.values())


