class DynamicArray {
   private:
    int myCapacity, size;
    int* myArray;

   public:
    DynamicArray(int capacity) {
        myCapacity = capacity;
        myArray = new int[myCapacity];
        size = 0;
    }

    int get(int i) {
        return myArray[i];
    }

    void set(int i, int n) {
        myArray[i] = n;
    }

    void pushback(int n) {
        if (size == myCapacity) {
            resize();
        }
        myArray[size++] = n;
    }

    int popback() {
        return myArray[--size];
    }

    void resize() {
        if (myCapacity == 0)
            myCapacity = 1;
        else    
            myCapacity *= 2;
        int *newArray = new int[myCapacity];
        for(int i = 0; i<size; ++i) newArray[i] = myArray[i];
        delete[] myArray;
        myArray = newArray;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return myCapacity;
    }

    ~DynamicArray() {
        delete[] myArray;
    }
};
