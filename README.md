1. Imported the requests and BeautifulSoup modules, which are used for sending HTTP requests and parsing HTML pages, respectively.

2. Defined a variable texterr for error messages, as well as the base URL of the target website and the session ID.

3. Used nested loops to iterate through the ASCII codes for database names 1-4.

4. Constructed a payload string demot, and then sent it as a parameter to the target website URL.

5. Parsed the page content from the response, then searched within the page for the content of the tag (pre) that contains the response text.

6. Checked each found result; if the text was not equal to the error message and contained a specified hint, then the query string was written into a file named "example.txt", and the current loop was stopped.

7. Since in actual testing, testing the payload would return a 404 response, but it does not affect the page return, there was no need to set a check for the response code.
