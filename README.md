# Keyboard-frontend

A keyboard layout built with HTML buttons and CSS pressed-key styling. The root page opens the original [keyboard layout](keyboard/index.html).

## Local preview

From the repository root, run the following command, then open [localhost on port 8000](http://localhost:8000/).

```sh
python -m http.server 8000
```

## Source

Edit [keyboard/index.html](keyboard/index.html) for the key labels and rows. The [stylesheet](keyboard/style.css) sets key sizes, spacing and pressed states. Focus the keyboard region and press a physical key to highlight it. Select an on-screen key to show its name; left and right modifiers have distinct accessible names. On a narrow screen, scroll the keyboard region horizontally.

Run `python tests/test_layout.py` to verify the routes and physical key mapping. Run `node --check keyboard/keys.js` to check the event script.
