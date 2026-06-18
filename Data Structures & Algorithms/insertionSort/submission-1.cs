// Definition for a pair
// public class Pair {
//     public int Key;
//     public string Value;
//
//     public Pair(int key, string value) {
//         Key = key;
//         Value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> InsertionSort(List<Pair> pairs) {
        List<List<Pair>> results = new List<List<Pair>>();
        for(int i = 0; i<pairs.Count; ++i) {
            int k = i;
            for(int j = i-1; j >= 0; j--) {
                if(pairs[k].Key < pairs[j].Key) {
                    var temp = pairs[k];
                    pairs[k] = pairs[j];
                    pairs[j] = temp;
                    k--;
                }
                else {
                    break;
                }
            }
            results.Add(new List<Pair>(pairs));
        }

        return results;
    }
}
