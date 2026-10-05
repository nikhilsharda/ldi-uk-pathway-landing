# LDI Online Pathway landing page

Co-branded landing page for LD International (LDI) and MSM Unify. Static HTML, no dependencies.

Review site: https://ldi-uk-pathway.vercel.app (noindex while in review)

## Files
- `index.html` - the page. Images load from `img/`.
- `img/` - hero and section photography (AI-generated), LD Training and MSM Unify logos.
- `build.py` - optional: inlines `img/` into one shareable file `index.single.html` and fails if an em or en dash is present.
- `vercel.json` and `robots.txt` - noindex headers and image caching. Remove both when the page goes live for search.

## Connect lead capture to Zoho CRM
Edit the `CONFIG` block at the bottom of `index.html`:
- `ZOHO_ACTION`, `ZOHO_XNQSJSDP`, `ZOHO_XMIWTLD` come from a Zoho Web-to-Lead form.
- Leave them blank to run in preview mode (nothing is sent).

Market links: `?m=india|pakistan|srilanka|uae|nigeria|ghana|nepal` swaps the hero line and pre-fills country and dial code. UTM parameters are captured into the lead description.

## Notes
- Logos belong to their owners. LD Training's brand guidelines require written consent for logo use.
- Copy rules: UK English, no em dashes, and progression to a UK university is always described as "potential" and conditional.
