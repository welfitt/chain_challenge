# chain_challenge
An obvious choice was to use recursion and why not python?
There may be way better ways of doing this but I did it without googling a solution as that would spoil the fun.

The code reads the file into an array so that processing can then be done quicker in memory rather than io to disk.
And yeah I could have/should have done a try catch round the disk io but this is not for production. 

The main loop just loops through every element in the 2d array looking for a hash. When it finds one it then calls the function.
The job of the function is to use recursion to follow all elements of that chain, count them and delete them. Ulitimately it returns the length of the chain it just deleted. 
Once it's completely deleted a chain the main loop adds the length of that chain to the array chain_lengths. 
It then goes back to scanning the 2d array looking for the next element with a hash in it. Wash rinse repeat. 
Eventually it wipes the contents of the 2d array and prints out the results. 

Deleting an hash after it had been counted had the bonus of not having to keep track of what had already been counted and thus preventing double counting a chain or hash.
