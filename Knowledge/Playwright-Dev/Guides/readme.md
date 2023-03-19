# ⭐️ Guides ⭐️

## ⭐️ Actions ⭐️

- interact with HTML Input elements such as
  - text inputs, checkboxes, radio buttons,
  - select options, mouse clicks, type characters, keys and shortcuts
  - upload files and focus elements
  
- [Function](https://playwright.dev/python/docs/input)
  - get_by_role | get_by_label .. fill -------- text inputs
  - get_by_label .. check / is_checked() is ... -------- checkboxes, radio buttons
  - select_option(label='Blue') | select_option(['red', 'green', 'blue']) -------- select buttons
  - **click**(), **click**(button="right"), **click**(modifiers=["Shift"]), dblclick(), hover(), **click**(position={ "x": 0, "y": 0}), **click**(force=True), dispatch_event('**click**')  -------- mouse clicks
  - locator('#area').type('Hello World!') and optional delay between the key presses to simulate real user behavior. -------- type characters
  - get_by_text("Submit").press("Enter"), get_by_role ... press("Control-ArrowRight"), press("$") -------- Keys and shortcuts
  - get_by_label("Upload file").set_input_files('myfile.pdf') -------- Upload files
  - get_by_label ... focus -------- For the dynamic pages that handle **focus events**
  - locator ... drag_to(another_locator) or can using manually Dragging: hover -> mouse.down -> hover -> mouse.up

## ⭐️ [Auto-waiting](https://playwright.dev/python/docs/actionability) ⭐️

- elements actionability checks before making actions
- auto-waits for all the relevant checks
- Actions list: Attached | Visible | Stable | Receives Events | Enabled | Editable
- Forcing actions: disables non-essential actionability checks
- Assertions: check the actionability state of the element, helps writing assertive tests that ensure that after certain actions, elements reach actionable state
  
## ⭐️ API testing - IMPORTANT - NOT UNDERSTAND ⭐️

- access to the REST API: send requests to the server directly from Python without loading a page and running js code
  - test server API
  - Prepare server side state
  - Validate server side post-conditions
- [APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext) methods
- add Playwright fixtures to the Pytest test-runner with [pytest-playwright](https://playwright.dev/python/docs/test-runners) package
- Writing API Test
  - APIRequestContext can send all kinds of HTTP(S) requests over network.
  - Configure
  - Write tests
  - Setup and teardown
  - Complete test example
- Prepare server state via API calls
- Check the server state after running user actions
- Reuse authentication state

## ⭐️ [Assertions](https://playwright.dev/python/docs/test-assertions) ⭐️

## ⭐️ Authentication ⭐️

- recommend to create playwright/.auth directory and add it to your .gitignore
  - mkdir -p playwright/.auth
  - echo "\nplaywright/.auth" >> .gitignore
- Signing in before each test
  
```python
page = await context.new_page()
await page.goto('https://github.com/login')

# Interact with login form
await page.get_by_label("Username or email address").fill("username")
await page.get_by_label("Password").fill("password")
await page.page.get_by_role("button", name="Sign in").click()
# Continue with the test
```

- Reusing signed in state
  
```python
# Save storage state into the file.
storage = await context.storage_state(path="state.json")

# Create a new context with the saved storage state.
context = await browser.new_context(storage_state="state.json")
```

- Advanced scenarios
  - Session storage
  
```python
import os
# Get session storage and store as env variable
session_storage = await page.evaluate("() => JSON.stringify(sessionStorage)")
os.environ["SESSION_STORAGE"] = session_storage

# Set session storage in a new context
session_storage = os.environ["SESSION_STORAGE"]
await context.add_init_script("""(storage => {
  if (window.location.hostname === 'example.com') {
    const entries = JSON.parse(storage)
    for (const [key, value] of Object.entries(entries)) {
      window.sessionStorage.setItem(key, value)
    }
  }
})('""" - session_storage - "')")
```

## ⭐️ Browsers ⭐️

- Chromium Firefox WebKit Chrome Edge
- playwright install msedge : "chrome" or "msedge"
- download browsers into a specific location
  - PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers python -m playwright install
  - PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers python playwright_script.py
- proxies
  - HTTPS_PROXY=https://192.0.2.1 playwright install
  - set your custom root certificates before installing the browsers
    - export NODE_EXTRA_CA_CERTS="/path/to/cert.pem"
    - PLAYWRIGHT_DOWNLOAD_CONNECTION_TIMEOUT=120000 playwright install
- playwright install firefox

## ⭐️ Extensions ⭐️

- only work in Chrome / Chromium

## ⭐️ Command line tools ⭐️

- playwright
- playwright install --help
- dependencies
  - playwright install-deps
  - playwright install-deps chromium
  - playwright install --with-deps chromium
- Codegen
  - playwright codegen
  - playwright codegen --save-storage=auth.json
  - playwright open --load-storage=auth.json my.web.app
  - playwright codegen --load-storage=auth.json my.web.app
- Codegen with custom setup
- Open pages
  - Chromium: playwright open example.com
  - WebKit: playwright wk example.com
- playwright open --device="iPhone 11" wikipedia.org
- playwright open --viewport-size=800,600 --color-scheme=dark twitter.com
- playwright open --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" maps.google.com
- Inspect selectors
- playwright screenshot --help
- playwright pdf https://en.wikipedia.org/wiki/PDF wiki.pdf

## ⭐️ Debugging Selectors ⭐️

- Playwright Inspector
- DevTools
- DEBUG=pw:api pytest -s

## ⭐️ Debugging Tests ⭐️

## ⭐️ Dialogs ⭐️

## ⭐️ Downloads ⭐️
