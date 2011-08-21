#include "src/colors.h"
#include <stdio.h>

int main(void){
    /** foreground function change the letter of color **/
    foreground(BLUE);
    printf("Testing...");
    foreground(GREEN);
    printf("\nOne");
    foreground(YELLOW);
    printf("\nTWO");
    foreground(CYAN);
    printf("\nThree\n");
    foreground(WHITE);
    /** background function change the back(ground - obviously) of print **/
    background(GREEN);
    printf("The background color is green! And the foreground is white!");
    /** I believe that dont say what style do, right? - change the style **/
    style(RESETALL);
    printf("\nNow, no more colors from colors.h\n");

    return 0;


}
