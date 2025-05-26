## Hash Set vs List Lookup Time Comparison

Hey! 👋

This little script is something I put together to explore the difference in lookup performance between Python's built in `set` and `list` data structures.

### What it does:

* I create a list and a set, both filled with a million integers (`0` to `999,999`).
* Then I try to check if an item **that doesn’t exist** (`1,000,001`) is in the list and the set 100 times each.
* I measure how long those lookups take for both data types and print the results.

Task wanted me to demonstrate how sets offer **constant time (`O(1)`)** lookups compared to lists, which take **linear time (`O(n)`)**. So with a large number of elements, checking membership in a set is **way faster** than in a list.
Infact the time aspect threw me off initially, I had to sit and chew on it for a bit.

### To run it:

Just make sure you have Python installed and run the script like this:

```bash
python filename.py
```
footnote - probably could have done a better job on the comments as I left some of the task ones up and added a few more.
