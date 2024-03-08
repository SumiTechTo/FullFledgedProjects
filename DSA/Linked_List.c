#include<stdio.h>
#include<malloc.h>
struct link {
    int info;
    struct link *next;
};

void main(){
struct link *node=(struct link *)malloc(sizeof(struct link));
create link_list(node);
display(node);
}