/*
    Approach: Using Two Deque
    Time complexity: O(n^2)
    Space complexity: O(n)
*/

#include <deque>
using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        deque<int> sandwich_queue(sandwiches.begin(), sandwiches.end()); 
        deque<int> student_queue(students.begin(), students.end()); 
        int distance_of_unhappy_student = -1;

        while (student_queue.size() and distance_of_unhappy_student != student_queue.size()) {
            if (student_queue[0] == sandwich_queue[0]) {
                student_queue.pop_front();
                sandwich_queue.pop_front();
                distance_of_unhappy_student = -1;
            }
            else {
                int front = student_queue.front();  
                student_queue.pop_front();          
                student_queue.push_back(front);
                distance_of_unhappy_student++;
            }
        }

        return student_queue.size();
    }
};
