package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Integer, Integer>, List<String>> anagrams = new HashMap<>();
        for (String s : strs) {
            HashMap<Integer, Integer> hashMap = new HashMap();
            s.chars().forEach(c -> {
                if (hashMap.containsKey(c)) hashMap.put(c, hashMap.get(c) + 1);
                else hashMap.put(c, 0);
            });
            if (!anagrams.containsKey(hashMap)) anagrams.put(hashMap, new ArrayList());
            anagrams.get(hashMap).add(s);
        }
        return anagrams.values().stream().toList();
    }

    public List<List<String>> groupAnagramsWithSort(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();
        for (String s : strs) {
            char[] characters = s.toCharArray();
            Arrays.sort(characters);
            String key = new String(characters);

            if (!anagrams.containsKey(key)) anagrams.put(key, new ArrayList());
            anagrams.get(key).add(s);

        }
        return new ArrayList<>(anagrams.values());
    }
}
