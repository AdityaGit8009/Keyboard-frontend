from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Keys(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

class LayoutTests(unittest.TestCase):
    def test_original_entry_and_local_resources(self):
        self.assertIn("keyboard/index.html", (ROOT / "index.html").read_text(encoding="utf-8-sig"))
        self.assertTrue((ROOT / "keyboard" / "style.css").is_file())
        self.assertTrue((ROOT / "keyboard" / "keys.js").is_file())

    def test_unique_key_codes_and_accessible_modifiers(self):
        layout = Keys()
        layout.feed((ROOT / "keyboard" / "index.html").read_text(encoding="utf-8-sig"))
        entries = [a for tag, a in layout.elements if tag == "button"]
        codes = {a["data-code"] for a in entries}
        self.assertEqual(len(codes), len(entries))
        self.assertEqual(len(codes), 60)
        self.assertTrue({"Enter", "Backspace", "Space", "ShiftLeft", "ShiftRight"} <= codes)
        for key in entries:
            if key["data-code"].endswith(("Left","Right")):
                self.assertTrue(key.get("aria-label"))

if __name__ == "__main__":
    unittest.main()
