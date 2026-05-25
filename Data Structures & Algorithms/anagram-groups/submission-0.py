class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
       
        for word in strs:
           sorted_word = sorted(word) # cat --> "a","c","t"

           final_sorted_word = "".join(sorted_word)
           
           if final_sorted_word in hashmap:  # if act is in hashmap
               hashmap[final_sorted_word].append(word)
               #append word to key (sorted word).
               # add cat to act. append cat to map.
           else:
               hashmap[final_sorted_word] = [word]
       
        return list(hashmap.values())
