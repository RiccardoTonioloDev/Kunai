## Suggestions for web-like exercises

1. Everytime there is an HTML page involved, <u>inspect the page</u>:
   - Look for comments containing vulnerable information;
   - Look for hidden links;
   - Look forms (for request methods, names)
2. Inspect the Javascript code (if there is any use of it):
   - It could lead to vulnerable links;
   - It could leak vulnerable information;
   - You can even inspect the values inside the variables, using the integrated debugger of the web browser;
   - You can run functions in the console;
3. **Look out for cookies in the browser/header in the request**
4. The basic SQL injection method is: 
   - `" OR 1 = 1` in case before the `"` there is probably a string (try to use `'` instead of `"` if it doesn't work);
   - `1 OR 1 = 1` if the required parameter is a number;
5. Wherever you see the `eval()` function, there is an injection vulnerability;
6. Look out for situations where it's probable to use **OS commands** (like `ping` or `ls` or ecc.);
7. Use the extention **ModHeader**(for custom headers in the requests);
8. Use [this](http://jsnice.org) to prettify an obfuscated javascript code.