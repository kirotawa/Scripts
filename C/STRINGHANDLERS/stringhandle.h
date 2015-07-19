#ifndef __STRINGHANDLE__
#define __STRINGHANDLE__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* append_char_to_string(const char*, const char, const char);
void str_replacechar(char*, const char, const char);
void print_str_to_ascii_code(char*);
int str_rotate(char *, unsigned int, unsigned int);

#endif /* __STRINGHANDLE__ */
