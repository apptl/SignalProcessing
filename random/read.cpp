#include <iostream>
#include <string>
#include <fstream>



int main()
{

std::cout<<"hello"<<std::endl;
std::ifstream file("data-communications.csv"); // declare file stream: http://www.cplusplus.com/reference/iostream/ifstream/
std::string value;
int count=0;
while ( file.good() )
{
     std::getline ( file, value, ',' ); // read a string until next comma: http://www.cplusplus.com/reference/string/getline/
     std::cout<< std::string(value)<<std::endl; // display value removing the first and the last character from it
    count++;
}
std::cout<<"there were "<<count<<" values"<<std::endl;
}