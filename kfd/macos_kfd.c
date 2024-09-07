#define TARGET_MACOS 1
#include "kfd/libkfd.h"

int main(void)
{
    u64 kfd = kopen(2048, puaf_wipl0it, kread_sem_open, kwrite_sem_open);
    // At this point, kfd can be used with kread() and kwrite().
    kclose(kfd);
}
