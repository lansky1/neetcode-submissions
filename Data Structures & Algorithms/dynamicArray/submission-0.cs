public class DynamicArray {
    
    private int size;
    private int capacity;
    private int[] arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.arr = new int[this.capacity];
    }

    public int Get(int i) {
        return this.arr[i];
    }

    public void Set(int i, int n) {
        this.arr[i] = n;
    }

    public void PushBack(int n) {
        if (this.size == this.capacity) {
            Resize();
        }
        this.arr[this.size] = n;
        this.size++;
    }

    public int PopBack() {
        return this.arr[--this.size];
    }

    private void Resize() {
        int[] temp = (int[])arr.Clone();
        this.capacity = 2*this.capacity;
        this.arr = new int[this.capacity];
        temp.CopyTo(this.arr, 0);
    }

    public int GetSize() {
        return this.size;
    }

    public int GetCapacity() {
        return this.capacity;
    }
}
