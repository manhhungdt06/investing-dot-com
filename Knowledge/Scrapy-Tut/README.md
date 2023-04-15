# ⭐️ scrapy ⭐️

- Data Crawler Library written in Python

## ⭐️ Basic concepts ⭐️

### ⭐️ Command line tool ⭐️

- scrapy
- new : scrapyd-[deploy](https://scrapyd.readthedocs.io/en/latest/overview.html)
- scrapy.cfg
- [SCRAPY_SETTINGS_MODULE](https://scrapy-gallaecio.readthedocs.io/en/latest/topics/settings.html#topics-settings-module-envvar)
- [SCRAPY_PROJECT](https://scrapy-gallaecio.readthedocs.io/en/latest/topics/commands.html#topics-project-envvar)
- [SCRAPY_PYTHON_SHELL](https://scrapy-gallaecio.readthedocs.io/en/latest/topics/shell.html#topics-shell)
- Sharing the root directory between projects
- scrapy <command> [options] [args]
  - scrapy startproject myproject [project_dir]
  - scrapy genspider mydomain mydomain.com
  - scrapy -h
- Global commands:
    startproject
    genspider
    settings
    runspider
    shell
    fetch
    view
    version
- Project-only commands:
    crawl
    check
    list
    edit
    parse
    bench
