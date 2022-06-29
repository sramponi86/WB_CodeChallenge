# WB_CodeChallenge

Part 1
The folowing 3 classes were created to satisfy the requirements.
findFirstRepeatedN
pathChecker
coinFlip

The first one is iterating with nested loops verifiyng the presence of the current indexed value, from the first array , against the second one
(assumption on my side). Another assumption was that arrays with different lenght could be passed. No specific output was defined in case of missing match between the arrays , then i defined the 0 return (this can lead to issues and false results). 
During the process, at one point, i considered to sort the arrays to "fasten" the match....this was as well an error as it was not specified into the challenge description and also can lead to false results. I lefted as comments to mention it during the discussion.
The file "checkfindFirstRepeatedN" was then created to cover the function created verying not only the current returning abilities against clear scenarios , but also the results with specific negative paths and edge cases (strings, no arrays ...)

The second function will take a string path as input, then firstly check if this path is existing and if positive, align with the specified directory. Otherwise it will return a False.
In the positive case (existence of the input path) , then the function loops against the files available within the directory and for each verifies that:
- it is a .exe (file.endswith(".exe")
- has a size smaller than 14 Mbyte ( int((os.stat(file).st_size/1048576)) < 14 )
- owner is the root (os.stat(file).st_uid == 0) with all the admin rights

then when this conditions are matching it exists the loop and return a True value.

The third function 
