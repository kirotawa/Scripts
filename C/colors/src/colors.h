/**
    Author: Leônidas S. Barbosa
    Email : kirotawa(arroba)gmail(dot)com
    Year  : 2011
**/

#ifndef COLORS_H
#define COLORS_H

#define foreground(color) FORE##color
#define background(color) BACK##color
#define style(style_) style_

/** Foreground Colors **/
#define FOREBLACK printf("\033[30m") 
#define FORERED printf("\033[31m") 
#define FOREGREEN printf("\033[32m") 
#define FOREYELLOW printf("\033[33m") 
#define FOREBLUE printf("\033[34m") 
#define FOREMARGENTA printf("\033[35m") 
#define FORECYAN printf("\033[36m") 
#define FOREWHITE printf("\033[37m") 
#define FORENORMAL_COLOR printf("\033[39m") 

/** Background Colors **/
#define BACKBLACK printf("\033[40m") 
#define BACKRED printf("\033[41m") 
#define BACKGREEN printf("\033[42m") 
#define BACKYELLOW printf("\033[43m") 
#define BACKBLUE printf("\033[44m") 
#define BACKMAGENTA printf("\033[45m") 
#define BACKCYAN printf("\033[46m") 
#define BACKWHITE printf("\033[47m") 
#define BACKNORMAL printf("\033[49m")

/** Style **/
#define BRIGHT printf("\033[1m")
#define DIM printf("\033[2m")
#define NORMAL printf("\033[22m")
#define RESETALL printf("\033[0m")
#define UNDERLINE printf("\033[4m")
#define BLINKSLOW printf("\033[5m")
#define BLINKRAPID printf("\033[6m")
#define ITALIC printf("\033[3m")
#define NEGATIVE printf("\033[7m")
#endif /* COLORS_H */
