#include <stdio.h>
 
 void main(void){
    int choice = 0;
    do {
        //menu
        
        printf("----------------------------------Choose one----------------------------------\n");
        printf("0 - Exit program\n");
        printf("1 - List users and yours status\n");
        printf("2 - Create groupn\n");
        printf("3 - List registred groups (group name, lead, members)\n");
        printf("4 - Request conversation for debug\n");
        scanf("%d", &choice);
        printf("%d\n", choice);
    } while (choice != 0);
 }