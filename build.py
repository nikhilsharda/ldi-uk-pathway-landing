"""Inline img/ into one shareable file: index.single.html."""
import base64, re, os, sys
d = os.path.dirname(os.path.abspath(__file__)) + "/"
h = open(d + "index.html", encoding="utf-8").read()
def inline(m):
    f = m.group(1)
    mime = "image/png" if f.endswith(".png") else "image/jpeg"
    return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(open(d + "img/" + f, "rb").read()).decode())
h = re.sub(r'src="img/([^"]+)"', inline, h)
bad = [c for c in ("\u2014", "\u2013") if c in h]
if bad:
    sys.exit("DASH FOUND: %r" % bad)
open(d + "index.single.html", "w", encoding="utf-8").write(h)
print("built index.single.html", len(h) // 1024, "KB")
