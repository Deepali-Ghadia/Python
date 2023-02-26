import webbrowser 

# opening a url with default browser
webbrowser.open("www.google.com", new = 2) # 0=>existing | tab 1=>new window | 2=>new tab


# open in new window using open_new method
webbrowser.open_new("www.stackoverflow.com")

# open in new tab using open_new method
webbrowser.open_new_tab("www.stackoverflow.com")


# opening a URL with different browser
browser_path = webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe")
ff = webbrowser.get(browser_path)
ff.open("http://stackoverflow.com/")
