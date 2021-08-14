# tt-apyi

## Configuring API key

To avoid pushing API keys into github, create a `config.py` as follows:

```python
# This file should be saved in `tt-apyi/tt-apyi/config.py`
API_KEY = "API-KEY goes here"
```

## Examples

### Get projects data

```python
# https://docs.tokenterminal.com/api#get-all-projects
import services
projects_data = services.get_projects()
```

### Get historical data of a specific project

```python
# https://docs.tokenterminal.com/api#get-projects-historical-metrics
import services
uniswap_data = services.get_historical("uniswap")
```
