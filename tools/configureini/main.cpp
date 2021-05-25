#include <stdio.h>
#include "configini.h"

int main(int argc, char const *argv[])
{
    mini::OperatorINI config;
    config.readINI("./data/out.ini");
    config.writeINI("./data/in.ini");
    return 0;
}
