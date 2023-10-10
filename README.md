# Ai_Search

Welcome to the README file!

This code implements a Breadth First Search, Iterative Deepening and an A* search.

HOW TO USE THE SEARCH

The terminal command used to run this program is as follows:

python "filename" "test case" "type of search"

When inputting what files we actually want to use, we don't include the " symbols. For example, if we wanted to test the file labeled "test_case_2.txt" with our breadth first search we would do this:

python Ai_searches.py test_case_2.txt bfs

Similarly, if we wanted to do the iterative-deepening search instead with the file named "test_case_3.txt" we would type this in the terminal:

python Ai_searches.py test_case_4.txt iddfs

We type "iddfs" because that is the name of the acronym the function calls, but more on that in a later paragraph. Every time the user inputs the terminal command above, the filename will be "Ai_searches.py" since that's the only file containing the searches. 

As you can see, there are no " symbols when we type our files and the search we want. When running this program with the test cases, make sure all files are in the same directory/folder as to not cause any problems with file locations. When inputting the type of search, they will be acronyms. Obviously right now the only search we have implemented is breadth first search labeled as "bfs". Upper or lower case doesn't matter, the program will convert your text automatically as long as you spell the acronym correctly. 

If you have any typos or miss any parameters when inputting the terminal command, the program and compiler will let you know. Otherwise refer to the instructions above if any issues occur. 