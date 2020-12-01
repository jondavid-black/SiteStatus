# SiteStatus
A simple utility to check the status of a URL using the HTTP response code.

# Usage
python -m pip install requests <br>
python SiteStatus.py

Output: <br>
  ```
  ('https://www.google.com', 200)
  ('https://www.github.com', 200)
  ('https://devopsfordefense.org', 200)
  ('https://www.github.com/jondavid-black/notapage.html', 404)
  ('https://notasite.com', 'error')
  ```

# Improvement Ideas
Instead of just printing to a console, publish data that can be used in a online dashboard.
