#include <bits/stdc++.h>
using namespace std;

class Queue
{
    int *arr;
    int front, rear, currSize, maxSize;

public:
    Queue()
    {

        arr = new int[16];
        maxSize = 16;
        currSize = 0;
        front = 0;
        rear = 0;
    }
    void enqueue(int key)
    {
        if (currSize == maxSize)
        {
            cout << "Queue overflow";
            return;
        }
        rear = (rear + 1) % maxSize;
        if (rear != front)
        {
            arr[rear] = key;
            currSize += 1;
        }
        return;
    }
    int deque()
    {
        if (currSize == 0)
        {
            cout << "Queue underflow";
            return -1;
        }
        else
        {
            int x = arr[front];
            front = (front + 1) % maxSize;
            currSize -= 1;
            return x;
        }
    }
};

int main()
{
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(6);
    cout << q.deque();
    cout << q.deque();
    cout << q.deque();
    cout << q.deque();
    cout << q.deque();
    return 0;
}
