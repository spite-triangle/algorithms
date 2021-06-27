#include <iostream>
#include <stdio.h>
#include <windows.h>

int main(int argc, char const *argv[])
{
    int i = 0;
    char bar[100] = {0};
    const char *Lab = "-\\/";
    while (i <= 100)
    {
        // \r : 将光标移动到一行的行首
        printf(" [%-100s][%d%%][%c]\r", bar, i, Lab[i % 4]);
        fflush(stdout);
        Sleep(100);
        bar[i++] = '#';
        bar[i] = '\0';
    }
    printf("\n");
    return 0;

}