// Example: define member function without argument within the class

#include <iostream>
using namespace std;

class Person
{
    int id;
    char name[100];

public:
    void set_p()
    {
        cout << "Enter the Id:";
        cin >> id;
        // fflush(stdin);
        cout << "Enter the Name:";
        cin >> name;
        //     cin.get(name, 100);
    }

    void display_p()
    {
        cout << endl
             << id << "\t" << name;
    }
};

class Student : private Person
{
    char course[50];
    int fee;

public:
    void set_s()
    {
        set_p();
        cout << "Enter the Course Name:";
        fflush(stdin);
        cin.getline(course, 50);
        cout << "Enter the Course Fee:";
        cin >> fee;
    }

    void display_s()
    {
        display_p();
        cout << "t" << course << "\t" << fee;
    }
};

#include <iostream>

class ClassA
{
public:
    int a;
};

class ClassB : virtual public ClassA
{
public:
    int b;
};

class ClassC : virtual public ClassA
{
public:
    int c;
};

class ClassD : public ClassB, public ClassC
{
public:
    int d;
};

// int main()
// {
//     ClassD obj;

//     obj.a = 10;  // Statement 3
//     obj.a = 100; // Statement 4

//     obj.b = 20;
//     obj.c = 30;
//     obj.d = 40;

//     cout << "\n a : " << obj.a;
//     cout << "\n b : " << obj.b;
//     cout << "\n c : " << obj.c;
//     cout << "\n d : " << obj.d << '\n';
// }
// only one copy

// CPP program to illustrate
// Operator Overloading
#include <iostream>
using namespace std;

class Complex
{
private:
    int real, imag;

public:
    Complex(int r = 0, int i = 0)
    {
        real = r;
        imag = i;
    }

    // This is automatically called when '+' is used with
    // between two Complex objects
    Complex operator+(Complex &obj)
    {
        Complex res;
        res.real = real + obj.real;
        res.imag = imag + obj.imag;
        return res;
    }
    void print() { cout << real << " + i" << imag << endl; }
};

int main()
{
    Complex c1(10, 5), c2(2, 4);
    Complex c3 = c1 + c2; // An example call to "operator+"
    c3.print();
}

// int main()
// {
//     Student s;
//     s.set_s();
//     s.display_s();
//     return 0;
// }
