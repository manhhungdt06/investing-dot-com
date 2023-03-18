# ⭐️ Playwright-Dev ⭐️

## ⭐️ Installation ⭐️

- pip install pytest-playwright
- playwright install

## ⭐️ Writing Tests ⭐️

- expect [assertions](https://playwright.dev/python/docs/test-assertions)

```python
Eg: expect(page).to_have_title(re.compile("Playwright"))
```

- Locators: represent a way to find element(s) on the page at any moment and are used to perform actions on elements such as .click .fill etc

``` python
get_started = page.get_by_role("link", name="Get started")
get_started.click()
```

- Test Hooks

```python
@pytest.fixture(scope="function", autouse=True)
```
  
## ⭐️ Running Tests ⭐️

- params: --numprocesses, --browser, --headed, -k
- [PWDEBUG](https://unix.stackexchange.com/questions/56444/how-do-i-set-an-environment-variable-on-the-command-line-and-have-it-appear-in-c)=1/console pytest -s
- page.pause()
- [investing.com](https://www.investing.com/)
  
```python
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.investing.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

```

- [marketmilk.babypips.com](https://marketmilk.babypips.com/)

```python
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://marketmilk.babypips.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

```

## ⭐️ Test Generator ⭐️

- **playwright codegen** command
- Emulate viewport size:
  
```bash
playwright codegen --viewport-size=800,600
```

- **--device**
- device list??
- **--color-scheme**
- **--timezone**="Europe/Rome" **--geolocation**="41.890221,12.492348" **--lang**="it-IT"

```python
playwright codegen --timezone="Asia/Saigon" --geolocation="21.039632,105.8828287" --lang="vn-VN" maps.google.com
```

- **--save-storage**
- --load-storage
- Record using custom setup in some non-standard setup:
  
```python
browser_context.route()
page.pause()
```

## ⭐️ Trace Viewer ⭐️

- a GUI tool that lets you explore recorded Playwright traces

## ⭐️ Pytest Reference ⭐️

- pytest --browser webkit --headed
- CLI:
    * --headed: Run tests in headed mode (default: headless).
    * --browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times  *default:chromium).
    * --browser-channel Browser channel to be used.
    * --slowmo Run tests with slow mo.
    * --device Device to be emulated.
    * --output Directory for artifacts produced by tests (default: test-results).
    * --tracing Whether to record a trace for each test. on, off, or retain-on-failure (default: off).
    * --video Whether to record video for each test. on, off, or retain-on-failure (default: off).
    * --screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off)

- Fixtures: fixture name as an argument to the test
  + Function scope: context, page
  + Session scope: playwright, browser_type, browser, ...
  + Customizing fixture options: browser_type_launch_args, browser_context_args

- Parallelism: Running Multiple Tests at Once
  + pip install pytest-xdist
  + pytest --numprocesses auto
  + @pytest.mark.skip_browser("firefox")
  + @pytest.mark.only_browser("chromium")
  + --browser-channel chrome
  + --base-url
  + Ignore HTTPS errors
  + Custom viewport size
  + --device="iPhone 11 Pro"
  + Persistent context: ???launch_persistent_context
  + unittest.TestCase
  + 