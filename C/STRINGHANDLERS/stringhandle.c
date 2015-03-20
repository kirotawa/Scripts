#include "stringhandle.h"


char * append_char_to_string(const char * string,
		const char char_to_append,
		const char where_append)
{
	size_t string_size;
	int index_to_string = 0;
	int index_to_new;
	int count_char_to_where_append = 0;
	char * new_string;

	string_size = strlen(string);

	while (string[index_to_string] != '\0') {
		if (string[index_to_string] == where_append)
			count_char_to_where_append += 1;

		index_to_string += 1;
	}

	new_string = (char*) malloc(sizeof(char*) * string_size +
			count_char_to_where_append);

#ifdef DEBUG
	new_string = NULL;
#endif

	if (new_string == NULL) {
		printf("Intern error: In line %d, cannot alloc memory to new_string\n",
				__LINE__ - 8);
		exit(1);
	}

	index_to_string = 0;
	index_to_new = index_to_string;

	while (string[index_to_string] != '\0') {
		if (string[index_to_string] == where_append) {
			new_string[index_to_new] = string[index_to_string];
			new_string[index_to_new+1] = char_to_append;
			index_to_new += 1;

		} else {
			new_string[index_to_new] = string[index_to_string];

		}
		index_to_new += 1;
		index_to_string += 1;
	}

	new_string[index_to_new] = '\0';
	return new_string;
}

void str_replacechar(char * string, const char char_to_subs,
		     const char char_to_replace)
{
	do {
		if (*(string) == char_to_subs)
			*(string) = char_to_replace;

	} while(*(string)++ != '\0');

}

void print_str_to_ascii_code(char * string)
{
	do {
		if (*(string) != '\0')
			printf("%d", *(string));

	} while (*(string)++);

}
