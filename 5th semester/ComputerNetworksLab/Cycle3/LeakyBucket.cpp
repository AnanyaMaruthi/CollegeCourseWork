#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#define bucketsize 512
using namespace std;
void bucketInput(int packetSize, int outputRate);
int main(){
    int output, packetSize;
    cout << "Enter output rate";
    cin >> output;
    for (int i = 0; i <5; i++){
        usleep(rand() % 1000);
        packetSize = rand() % 1000;
        cout << "\nPacket Number: " << i << "\tSize = " << packetSize;
        bucketInput(packetSize, output);
        
    }
    return 0;
}

void bucketInput(int packetSize, int outputRate){
    if (packetSize > bucketsize){
        cout << "\nOverflow detected\n";
    }
    else{
        usleep(500);
    }
    while(packetSize > outputRate){
        cout << outputRate << " bytes outputtted\n";
        packetSize -= outputRate;
        usleep(500);
    }
    if (packetSize > 0){
        cout << "Last " << packetSize << " bytes outputted\n";
    }
    cout << "Bucket output successful\n";
}
