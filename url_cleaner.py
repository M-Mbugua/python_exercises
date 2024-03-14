# Question: Please download the attached urls.txt file. The file
# contains some broken URLs. Here's what the file contains:
#     https:/www.google.com
#     https:/www.yahoo.com
#     https:/www.stackoverflow.com
#     https:/www.pythonhow.com
#
# Please use Python to remove the "s" from "https" and add another
# forward slash next to the existing slash, so the content looks
# like in the expected output.
#
# Expected output:
#     http://www.google.com
#     http://www.yahoo.com
#     http://www.stackoverflow.com
#     http://www.pythonhow.com

with open('urls.txt', 'r') as f:
    urls = f.readlines()

with open('urls_correct.txt', 'w') as file:

    for url in urls:
        url_remove_s = url.replace('s', '', 1)
        url_add_slash = url_remove_s[:6] + '/' + url_remove_s[6:]
        file.write(url_add_slash)
