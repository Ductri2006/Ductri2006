from pathlib import Path
import re
import xml.etree.ElementTree as ET

svg = Path("assets/github-mario.svg")
root = ET.parse(svg).getroot()
ns = {"s": "http://www.w3.org/2000/svg"}
if root.tag != "{http://www.w3.org/2000/svg}svg" or not root.findall(".//s:animateMotion", ns):
    raise SystemExit("Mario SVG has no animation.")
desc = root.find("s:desc", ns)
if desc is None or "Real GitHub contributions for Ductri2006" not in (desc.text or ""):
    raise SystemExit("Mario SVG does not describe this profile's contribution data.")
blocks = [e for e in root.findall(".//s:rect", ns) if e.get("class") in {"empty", "lvl1", "lvl2", "lvl3", "lvl4"}]
if not 365 <= len(blocks) <= 371:
    raise SystemExit("Mario SVG has an incomplete contribution calendar.")
for animation in root.findall(".//*[@keyTimes]"):
    times = [float(t) for t in animation.get("keyTimes").split(";")]
    if times[0] != 0 or times[-1] != 1 or any(a > b for a, b in zip(times, times[1:])):
        raise SystemExit("Mario SVG contains invalid animation timing.")
    if len(animation.get("values", "").split(";")) != len(times):
        raise SystemExit("Mario SVG has mismatched animation frames.")

readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")
section = """<!-- ========== MARIO ANIMATION ========== -->
## 🍄 Mario Contribution World

<div align="center">
  <img width="100%" src="https://raw.githubusercontent.com/Ductri2006/Ductri2006/main/assets/github-mario.svg" alt="Mario jumping through Ductri2006's GitHub contribution calendar" />
</div>

---

"""
pattern = r"<!-- ========== (?:SNAKE|MARIO) ANIMATION ========== -->[\s\S]*?(?=<!-- ========== RANDOM QUOTE ========== -->)"
updated, count = re.subn(pattern, lambda _: section, readme, count=1)
if count != 1:
    raise SystemExit("Contribution section not found; keep the existing README.")
if updated != readme:
    readme_path.write_text(updated, encoding="utf-8")
print(f"Validated {len(blocks)} contribution days and activated Mario.")
