In order to run the file, open a terminal window and navigate to the current directory where the numbers.py file is contained.

Then, run:

python numbers.py arg1 arg2

Time complexity: O(n)

The reason for this is that the algorithm uses a regex expression which seeks numeric values in the string.  Here, n is the length of the string.  It also loops though the returned array of numeric values, also n time.  Combined, the coefficients drop so the complexity is just O(n).

Space complexity: O(n)

The array takes up O(n) space where n is the number of elements in the array.

