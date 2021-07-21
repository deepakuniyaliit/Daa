#include<iostream>
using namespace std;

int main(){
    int n, size, key;
    cin>>n;

    cout<<"No. of test cases "<<n<<endl;

    for(int i=0; i<n; i++){
        cin>>size;
        int array[size];
        for(int j=0; j<size; j++){
            cin>>array[j];
        }
        cin>>key;

        cout<<"Size "<<size<<endl;
        for(int k=0; k<size; k++){
            cout<<array[k]<<" ";
        }
        cout<<endl;
        cout<<"Key "<<key<<endl;
    }


}