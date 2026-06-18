// Definition for a pair.
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
    public List<Pair> MergeSort(List<Pair> pairs) {
        if(pairs.Count == 0 || pairs.Count == 1) return pairs;

        int mid = pairs.Count/2;
        List<Pair> left = pairs.GetRange(0, mid);
        List<Pair> right = pairs.GetRange(mid, pairs.Count-mid);

        List<Pair> sleft = MergeSort(left);
        List<Pair> sright = MergeSort(right);

        return Merge(sleft, sright);
    }

    private List<Pair> Merge(List<Pair> left, List<Pair> right) {
        int i = 0;
        int j = 0;
        List<Pair> combined = new List<Pair>();
        while(i < left.Count && j < right.Count) {
            if(left[i].Key <= right[j].Key) {
                combined.Add(left[i]);
                i++;
            }
            else {
                combined.Add(right[j]);
                j++;
            }
        }
        if(j != right.Count) {
            while(j!=right.Count) combined.Add(right[j++]); 
        }
        else if(i != left.Count) {
            while(i!=left.Count) combined.Add(left[i++]);
        }
        return combined;
    }
}
