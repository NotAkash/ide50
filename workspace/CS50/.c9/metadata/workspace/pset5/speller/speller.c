{"filter":false,"title":"speller.c","tooltip":"/pset5/speller/speller.c","undoManager":{"mark":5,"position":-1,"stack":[[{"start":{"row":201,"column":5},"end":{"row":202,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":1,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":[" Watch 1","  Star 0  Fork 6 raju249/CS50"," Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights","Branch: master Find file Copy pathCS50/pset5/pset5/speller.c","b307b64  on 6 Jul 2015","@raju249 raju249 spell-checker in C using TRIE datastructure","1 contributor","RawBlameHistory     ","203 lines (167 sloc)  5.14 KB",""],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":8,"column":9},"action":"remove","lines":["Skip to content","This repository","Search","Pull requests","Issues","Marketplace","Explore"," @NotAkash"," Sign out"],"id":8}],[{"start":{"row":219,"column":1},"end":{"row":220,"column":0},"action":"remove","lines":["",""],"id":9}],[{"start":{"row":220,"column":0},"end":{"row":232,"column":0},"action":"remove","lines":["© 2017 GitHub, Inc.","Terms","Privacy","Security","Status","Help","Contact GitHub","API","Training","Shop","Blog","About",""],"id":10}],[{"start":{"row":0,"column":0},"end":{"row":197,"column":0},"action":"remove","lines":["/**"," * Implements a spell-checker."," */","","#include <ctype.h>","#include <stdio.h>","#include <sys/resource.h>","#include <sys/time.h>","","#include \"dictionary.h\"","#undef calculate","#undef getrusage","","// default dictionary","#define DICTIONARY \"dictionaries/large\"","","// prototype","double calculate(const struct rusage *b, const struct rusage *a);","","int main(int argc, char *argv[])","{","    // check for correct number of args","    if (argc != 2 && argc != 3)","    {","        printf(\"Usage: speller [dictionary] text\\n\");","        return 1;","    }","","    // structs for timing data","    struct rusage before, after;","","    // benchmarks","    double time_load = 0.0, time_check = 0.0, time_size = 0.0, time_unload = 0.0;","","    // determine dictionary to use","    char* dictionary = (argc == 3) ? argv[1] : DICTIONARY;","","    // load dictionary","    getrusage(RUSAGE_SELF, &before);","    bool loaded = load(dictionary);","    getrusage(RUSAGE_SELF, &after);","","    // abort if dictionary not loaded","    if (!loaded)","    {","        printf(\"Could not load %s.\\n\", dictionary);","        return 1;","    }","","    // calculate time to load dictionary","    time_load = calculate(&before, &after);","","    // try to open text","    char *text = (argc == 3) ? argv[2] : argv[1];","    FILE *fp = fopen(text, \"r\");","    if (fp == NULL)","    {","        printf(\"Could not open %s.\\n\", text);","        unload();","        return 1;","    }","","    // prepare to report misspellings","    printf(\"\\nMISSPELLED WORDS\\n\\n\");","","    // prepare to spell-check","    int index = 0, misspellings = 0, words = 0;","    char word[LENGTH+1];","","    // spell-check each word in text","    for (int c = fgetc(fp); c != EOF; c = fgetc(fp))","    {","        // allow only alphabetical characters and apostrophes","        if (isalpha(c) || (c == '\\'' && index > 0))","        {","            // append character to word","            word[index] = c;","            index++;","","            // ignore alphabetical strings too long to be words","            if (index > LENGTH)","            {","                // consume remainder of alphabetical string","                while ((c = fgetc(fp)) != EOF && isalpha(c));","","                // prepare for new word","                index = 0;","            }","        }","","        // ignore words with numbers (like MS Word can)","        else if (isdigit(c))","        {","            // consume remainder of alphanumeric string","            while ((c = fgetc(fp)) != EOF && isalnum(c));","","            // prepare for new word","            index = 0;","        }","","        // we must have found a whole word","        else if (index > 0)","        {","            // terminate current word","            word[index] = '\\0';","","            // update counter","            words++;","","            // check word's spelling","            getrusage(RUSAGE_SELF, &before);","            bool misspelled = !check(word);","            getrusage(RUSAGE_SELF, &after);","","            // update benchmark","            time_check += calculate(&before, &after);","","            // print word if misspelled","            if (misspelled)","            {","                printf(\"%s\\n\", word);","                misspellings++;","            }","","            // prepare for next word","            index = 0;","        }","    }","","    // check whether there was an error","    if (ferror(fp))","    {","        fclose(fp);","        printf(\"Error reading %s.\\n\", text);","        unload();","        return 1;","    }","","    // close text","    fclose(fp);","","    // determine dictionary's size","    getrusage(RUSAGE_SELF, &before);","    unsigned int n = size();","    getrusage(RUSAGE_SELF, &after);","","    // calculate time to determine dictionary's size","    time_size = calculate(&before, &after);","","    // unload dictionary","    getrusage(RUSAGE_SELF, &before);","    bool unloaded = unload();","    getrusage(RUSAGE_SELF, &after);","","    // abort if dictionary not unloaded","    if (!unloaded)","    {","        printf(\"Could not unload %s.\\n\", dictionary);","        return 1;","    }","","    // calculate time to unload dictionary","    time_unload = calculate(&before, &after);","","    // report benchmarks","    printf(\"\\nWORDS MISSPELLED:     %d\\n\", misspellings);","    printf(\"WORDS IN DICTIONARY:  %d\\n\", n);","    printf(\"WORDS IN TEXT:        %d\\n\", words);","    printf(\"TIME IN load:         %.2f\\n\", time_load);","    printf(\"TIME IN check:        %.2f\\n\", time_check);","    printf(\"TIME IN size:         %.2f\\n\", time_size);","    printf(\"TIME IN unload:       %.2f\\n\", time_unload);","    printf(\"TIME IN TOTAL:        %.2f\\n\\n\", ","     time_load + time_check + time_size + time_unload);","","    // that's all folks","    return 0;","}","","/**"," * Returns number of seconds between b and a."," */","double calculate(const struct rusage *b, const struct rusage *a)","{","    if (b == NULL || a == NULL)","    {","        return 0.0;","    }","    else","    {","        return ((((a->ru_utime.tv_sec * 1000000 + a->ru_utime.tv_usec) -","                 (b->ru_utime.tv_sec * 1000000 + b->ru_utime.tv_usec)) +","                ((a->ru_stime.tv_sec * 1000000 + a->ru_stime.tv_usec) -","                 (b->ru_stime.tv_sec * 1000000 + b->ru_stime.tv_usec)))","                / 1000000.0);","    }","}",""],"id":11},{"start":{"row":0,"column":0},"end":{"row":232,"column":0},"action":"insert","lines":["Skip to content","This repository","Search","Pull requests","Issues","Marketplace","Explore"," @NotAkash"," Sign out"," Watch 1","  Star 0  Fork 6 raju249/CS50"," Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights","Branch: master Find file Copy pathCS50/pset5/pset5/speller.c","b307b64  on 6 Jul 2015","@raju249 raju249 spell-checker in C using TRIE datastructure","1 contributor","RawBlameHistory     ","203 lines (167 sloc)  5.14 KB","/****************************************************************************"," * speller.c"," *"," * Computer Science 50"," * Problem Set 5"," *"," * Implements a spell-checker."," ***************************************************************************/","","#include <ctype.h>","#include <stdio.h>","#include <sys/resource.h>","#include <sys/time.h>","","#include \"dictionary.h\"","#undef calculate","#undef getrusage","","// default dictionary","#define DICTIONARY \"/home/cs50/pset5/dictionaries/large\"","","// prototype","double calculate(const struct rusage* b, const struct rusage* a);","","int main(int argc, char* argv[])","{","    // check for correct number of args","    if (argc != 2 && argc != 3)","    {","        printf(\"Usage: speller [dictionary] text\\n\");","        return 1;","    }","","    // structs for timing data","    struct rusage before, after;","","    // benchmarks","    double time_load = 0.0, time_check = 0.0, time_size = 0.0, time_unload = 0.0;","","    // determine dictionary to use","    char* dictionary = (argc == 3) ? argv[1] : DICTIONARY;","","    // load dictionary","    getrusage(RUSAGE_SELF, &before);","    bool loaded = load(dictionary);","    getrusage(RUSAGE_SELF, &after);","","    // abort if dictionary not loaded","    if (!loaded)","    {","        printf(\"Could not load %s.\\n\", dictionary);","        return 1;","    }","","    // calculate time to load dictionary","    time_load = calculate(&before, &after);","","    // try to open text","    char* text = (argc == 3) ? argv[2] : argv[1];","    FILE* fp = fopen(text, \"r\");","    if (fp == NULL)","    {","        printf(\"Could not open %s.\\n\", text);","        unload();","        return 1;","    }","","    // prepare to report misspellings","    printf(\"\\nMISSPELLED WORDS\\n\\n\");","","    // prepare to spell-check","    int index = 0, misspellings = 0, words = 0;","    char word[LENGTH+1];","","    // spell-check each word in text","    for (int c = fgetc(fp); c != EOF; c = fgetc(fp))","    {","        // allow only alphabetical characters and apostrophes","        if (isalpha(c) || (c == '\\'' && index > 0))","        {","            // append character to word","            word[index] = c;","            index++;","","            // ignore alphabetical strings too long to be words","            if (index > LENGTH)","            {","                // consume remainder of alphabetical string","                while ((c = fgetc(fp)) != EOF && isalpha(c));","","                // prepare for new word","                index = 0;","            }","        }","","        // ignore words with numbers (like MS Word can)","        else if (isdigit(c))","        {","            // consume remainder of alphanumeric string","            while ((c = fgetc(fp)) != EOF && isalnum(c));","","            // prepare for new word","            index = 0;","        }","","        // we must have found a whole word","        else if (index > 0)","        {","            // terminate current word","            word[index] = '\\0';","","            // update counter","            words++;","","            // check word's spelling","            getrusage(RUSAGE_SELF, &before);","            bool misspelled = !check(word);","            getrusage(RUSAGE_SELF, &after);","","            // update benchmark","            time_check += calculate(&before, &after);","","            // print word if misspelled","            if (misspelled)","            {","                printf(\"%s\\n\", word);","                misspellings++;","            }","","            // prepare for next word","            index = 0;","        }","    }","","    // check whether there was an error","    if (ferror(fp))","    {","        fclose(fp);","        printf(\"Error reading %s.\\n\", text);","        unload();","        return 1;","    }","","    // close text","    fclose(fp);","","    // determine dictionary's size","    getrusage(RUSAGE_SELF, &before);","    unsigned int n = size();","    getrusage(RUSAGE_SELF, &after);","","    // calculate time to determine dictionary's size","    time_size = calculate(&before, &after);","","    // unload dictionary","    getrusage(RUSAGE_SELF, &before);","    bool unloaded = unload();","    getrusage(RUSAGE_SELF, &after);","","    // abort if dictionary not unloaded","    if (!unloaded)","    {","        printf(\"Could not unload %s.\\n\", dictionary);","        return 1;","    }","","    // calculate time to unload dictionary","    time_unload = calculate(&before, &after);","","    // report benchmarks","    printf(\"\\nWORDS MISSPELLED:     %d\\n\", misspellings);","    printf(\"WORDS IN DICTIONARY:  %d\\n\", n);","    printf(\"WORDS IN TEXT:        %d\\n\", words);","    printf(\"TIME IN load:         %.2f\\n\", time_load);","    printf(\"TIME IN check:        %.2f\\n\", time_check);","    printf(\"TIME IN size:         %.2f\\n\", time_size);","    printf(\"TIME IN unload:       %.2f\\n\", time_unload);","    printf(\"TIME IN TOTAL:        %.2f\\n\\n\", ","     time_load + time_check + time_size + time_unload);","","    // that's all folks","    return 0;","}","","/**"," * Returns number of seconds between b and a."," */","double calculate(const struct rusage* b, const struct rusage* a)","{","    if (b == NULL || a == NULL)","    {","        return 0.0;","    }","    else","    {","        return ((((a->ru_utime.tv_sec * 1000000 + a->ru_utime.tv_usec) -","                 (b->ru_utime.tv_sec * 1000000 + b->ru_utime.tv_usec)) +","                ((a->ru_stime.tv_sec * 1000000 + a->ru_stime.tv_usec) -","                 (b->ru_stime.tv_sec * 1000000 + b->ru_stime.tv_usec)))","                / 1000000.0);","    }","}","© 2017 GitHub, Inc.","Terms","Privacy","Security","Status","Help","Contact GitHub","API","Training","Shop","Blog","About",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":39},"end":{"row":21,"column":39},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1512042024379,"hash":"c41f17119de9a22c3c7dcd5524d516cf9a4b0297"}