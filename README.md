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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
The second function will take a string path as input, then firstly check if this path is existing and if positive, align with the specified directory. Otherwise it will return a False.
In the positive case (existence of the input path) , then the function loops against the files available within the directory and for each verifies that:
- it is a .exe (file.endswith(".exe")
- has a size smaller than 14 Mbyte ( int((os.stat(file).st_size/1048576)) < 14 )
- owner is the root (os.stat(file).st_uid == 0) with all the admin rights

then when this conditions are matching it exists the loop and return a True value.
The file "checkpathChecker" is created and as well verifies that , an existing path with specific executable file accessible by the admin with a specific size can be found. also verifies the behaviour in specific cases like providing an impossible path "2" , or an integer as input.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
The third function takes an array as input, with the assumption that can have different lenghts and not only "0,1" values, and as first steps verifies that it is bigger than 1. If the first condition is matched it returns a False values (assumption) as no permutation is meaningful.
Then it explores the 2 different branches, in case the permutations should start with a leading 0 or a leading 1 and 2 separate counters are updated.
The first one (changeWithLeadingZero) update the counter every time the current array values is equal to 1 minus (index%2).
So all the even indexes should have a "1" value to trigger the update , and all the odd indexes should have a "0" value.

Then the additional counter (changeWithLeadingOne) is triggered based on the matching value between the current value and the (index%2) result. So even values should be 0 and odd should be matching with 1.

In the end the result is provided as the minimum value between the 2 different counters.

Also for this function the file "checkflipCoin" has been created verifying the behaviour against positive, negative and edge cases as input.
Inserting short interspersed arrays expecting the result to be 0 ([1,0]) , or inserting an array with one element, or inserting long arrays , or passing an integer as input, negative values or strings.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In general some questions and clarification , that can be discussion point within the interviewing process, could be done to limit and clarify the outcome and beavhiour of the functions requested and therefore leading the Unit tests creation.
