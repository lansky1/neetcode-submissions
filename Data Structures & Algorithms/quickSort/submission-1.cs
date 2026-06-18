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
    public List<Pair> QuickSort(List<Pair> pairs) {
        QuickSortMethod(pairs, 0, pairs.Count-1);
        return pairs;
    }

    public void QuickSortMethod(List<Pair> arr, int s, int e) {
        if(e-s+1 <= 1) return;

        var pivot = arr[e];
        var left = s;

        for(int i = s; i < e; ++i) {
            if (arr[i].Key < pivot.Key) {
                Pair temp = arr[left];
                arr[left] = arr[i];
                arr[i] = temp;
                left++;
            }
        }

        arr[e] = arr[left];
        arr[left] = pivot;

        QuickSortMethod(arr, s, left-1);
        QuickSortMethod(arr, left+1, e);
    }
}
