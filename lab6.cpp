#include <iostream>

using namespace std;
double harmonic(int n) {
if (n==1)
    return 1.0;
return 1.0/n+harmonic(n-1);
}
double harmonic() {
int n;
cout<<"Question 5 icin deger gir:";
cin>>n;
return harmonic(n);
}

int main()
{
    int n;
    cout<<"Question 4 icin deger:";
    cin>>n;
    cout<<"Harmonik degeri(Question 4 ):"<<harmonic(n)<<endl;
    cout<<"---Question 5 icin harmonik deger hesaplama----"<<endl<<harmonic()<<endl;
    return 0;
}
