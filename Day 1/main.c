#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    // Open file in readonly
    FILE *fileptr = fopen("input.txt", "r");
    if(fileptr == NULL){
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    char line[100]; // Assume Line of characters is not longer than 100
    char chartmp[3]; // To capture the digit(characters) then combine them. Example string(1abc2), digits 1,2, combine to make 12
    int sum = 0;  // To add up the numbers after combining them.

    // Read each line in the File via loop.
    while(fgets(line, sizeof(line), fileptr) != NULL){
        printf("Line: %s", line);
        int len = strlen(line);
        // Find First Digit, store it.
        int i = 0;
        while (i < len) {
            if (isdigit(line[i])) {
                printf("  first: %c ", line[i]);
                chartmp[0] = line[i];
                break;
            }
            i++;
        }
        // Find Last digit, so go reverse into the string, then store it. 
        //   Note: in string(3fiveone), it would be First(3), Last(3), final number is 33
        int x = len - 1;
        while (x >= 0){
            if(isdigit(line[x])) {
                printf("last: %c ", line[x]);
                chartmp[1] = line[x];
                // Print Combined numbers, change to integer, add it to total sum
                printf("combined: %s", chartmp);
                // Change to interger from char/string
                int temp = atoi(chartmp);
                sum += temp;
                printf(" SUM %d", sum);
                break;
            }
            x--;
        }
        printf("\n");
    }

    printf("SUM: %d\n", sum);
    fclose(fileptr);
    return EXIT_SUCCESS;

}