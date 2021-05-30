#include <stdio.h>
#include "configini.h"

int main(int argc, char const *argv[])
{
    mini::OperatorINI config;
    config.readINI("./data/in.ini");
    config.writeINI("./data/out.ini");
    return 0;
}
