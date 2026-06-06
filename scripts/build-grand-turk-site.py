#!/usr/bin/env python3
"""Generate Grand Turk Shore Excursion static site files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://grandturkshoreexcursion.com"
SITE = "Grand Turk Shore Excursion"
DATE = "2026-06-06"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Lora:wght@400;600;700"
    "&family=Work+Sans:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(21, 94, 117, 0.82) 0%, "
    "rgba(8, 145, 178, 0.72) 45%, rgba(6, 182, 212, 0.58) 100%)"
)
ACCENT = "text-cyan-200"

HOME_HERO = "images/hero-grand-turk.png"
HOME_HERO_ALT = (
    "Carnival cruise ship at Grand Turk Cruise Center pier with turquoise water, "
    "white sand beach and blue striped loungers"
)
BEST_IMG = "images/best-grand-turk-excursions.png"
BEST_ALT = "Best Grand Turk shore excursions including beaches stingrays and snorkelling"
PORT_IMG = "images/grand-turk-cruise-port.png"
PORT_ALT = "Cruise ship docked at Grand Turk Cruise Center in Turks and Caicos"
ONE_DAY_IMG = "images/one-day-grand-turk.png"
ONE_DAY_ALT = "One day in Grand Turk for cruise passengers visiting Turks and Caicos"
GIBBS_IMG = "images/gibbs-cay-stingray.png"
GIBBS_ALT = (
    "Gibbs Cay stingray excursion in Grand Turk with stingrays in shallow turquoise water"
)
SNORKEL_IMG = "images/grand-turk-snorkelling.png"
SNORKEL_ALT = (
    "Snorkelling tour in Grand Turk with coral reefs and tropical fish "
    "in clear Caribbean water"
)
BEACH_BREAK_IMG = "images/grand-turk-beach-breaks.png"
BEACH_BREAK_ALT = (
    "Grand Turk beach break near the cruise port with GRAND TURK sign on white wall and palm trees"
)
GOVERNORS_IMG = "images/governors-beach.png"
GOVERNORS_ALT = "Governor's Beach in Grand Turk with white sand and turquoise water"
ISLAND_IMG = "images/grand-turk-island-tours.png"
ISLAND_ALT = (
    "Grand Turk island sightseeing tour from the cruise port showing Cockburn Town "
    "coastline and turquoise water"
)
GOLF_IMG = "images/grand-turk-golf-cart.png"
GOLF_ALT = "Golf cart tour exploring Grand Turk from the cruise port"
LIGHTHOUSE_IMG = "images/grand-turk-lighthouse.png"
LIGHTHOUSE_ALT = "Grand Turk Lighthouse on an island sightseeing tour"
PRIVATE_IMG = "images/grand-turk-private-tours.png"
PRIVATE_ALT = "Private Grand Turk shore excursion with flexible island sightseeing"
FAMILY_IMG = "images/grand-turk-family.png"
FAMILY_ALT = "Family friendly Grand Turk shore excursion from the cruise port"
BEACHES_IMG = "images/grand-turk-beaches.png"
BEACHES_ALT = (
    "Grand Turk Cruise Center beach with GRAND TURK sign on white wall and palm trees"
)
FAQ_IMG = "images/grand-turk-faq.png"
FAQ_ALT = "Cruise passengers exploring Grand Turk Cruise Center"
INTRO_IMG = "images/grand-turk-intro.png"
INTRO_ALT = (
    "Aerial view of Grand Turk coastline with turquoise water, boats and cruise port area"
)


def page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    hero: str,
    content: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: bool = True,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_attr = '\n  data-trust-strip="partials/trust-strip.html"' if trust else ""
    content_file = content if content.startswith("content/") else f"content/{content}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{data_page}"
  data-base=""
  data-hero="{hero}"
  data-content="{content_file}"{trust_attr}
>

  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>

  <script src="js/site.js"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    activity_level: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Activity Level</dt><dd>{activity_level}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def _hero_wave() -> str:
    return '<div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'


def _hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
    tags_html = ""
    if tags:
        tags_html = '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">' + "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
            for t in tags
        ) + "</div>"
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-cyan-300 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {_hero_wave()}
</section>"""


def _internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Grand Turk guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="grand-turk-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-grand-turk-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="gibbs-cay-stingray-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Gibbs Cay</a>
    <span class="text-gray-300">·</span>
    <a href="grand-turk-snorkelling-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Snorkelling</a>
    <span class="text-gray-300">·</span>
    <a href="grand-turk-beach-breaks.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Beach Breaks</a>
    <span class="text-gray-300">·</span>
    <a href="grand-turk-island-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Island Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grand-turk-golf-cart-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Golf Cart Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grand-turk-private-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Private Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grand-turk-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def _comparison_section() -> str:
    rows = [
        ("Cruise Center Beach", "2–6 hrs", "Walk-off beach day", "Low — swim &amp; relax", "grand-turk-beach-breaks.html"),
        ("Gibbs Cay Stingrays", "2–3 hrs", "Shallow-water stingray swim", "Low to moderate", "gibbs-cay-stingray-excursions.html"),
        ("Snorkelling", "2–3 hrs", "Reef &amp; clear turquoise water", "Moderate — swim", "grand-turk-snorkelling-tours.html"),
        ("Island Tour", "2–4 hrs", "Cockburn Town &amp; viewpoints", "Low — van touring", "grand-turk-island-tours.html"),
        ("Golf Cart Tour", "1.5–3 hrs", "Coastline &amp; town at your pace", "Low — self-drive", "grand-turk-golf-cart-tours.html"),
        ("Lighthouse Visit", "2–3 hrs", "Historic lighthouse &amp; views", "Low to moderate", "grand-turk-lighthouse-tours.html"),
        ("Private Tour", "3–5 hrs", "Custom pacing for groups", "Varies", "grand-turk-private-tours.html"),
    ]
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-turk-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-turk-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Grand Turk Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your Grand Turk Cruise Center port day to beach time, Gibbs Cay stingrays, snorkelling, island sightseeing or a private custom route — all timed for typical cruise schedules.</p>
  <div class="overflow-x-auto rounded-3xl border border-turk-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Activity Level</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-turk-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="6–9 hours (typical)",
        best_for="Cruise Center beach, Gibbs Cay, snorkelling, island tours",
        activity_level="Varies — see comparison",
        family="Excellent with age-appropriate picks",
        return_ship="Operators usually allow 60–90 min buffer",
        popular="Beach breaks, Gibbs Cay stingrays, snorkelling, island tours",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def _content_excursion_page(
    intro: str,
    bullets: list[str],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-cyan-300 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Grand Turk Cruise Center · Turks &amp; Caicos</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Grand Turk Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Walk straight from your ship to turquoise water at the Cruise Center beach — or book Gibbs Cay stingrays, snorkelling, island tours and relaxed beach days timed for your port call.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-grand-turk-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="grand-turk-beach-breaks.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Cruise Center Beach</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Center Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Gibbs Cay Stingrays</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Snorkelling</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Turquoise Water</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Island Tours</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def _content_home() -> str:
    cards = _card_grid([
        (BEACH_BREAK_IMG, BEACH_BREAK_ALT, "Cruise Center Beach", "Step off the ship onto white sand and clear turquoise water — no transfer needed.", "grand-turk-beach-breaks.html", "Beach Breaks"),
        (GIBBS_IMG, GIBBS_ALT, "Gibbs Cay Stingrays", "Short boat ride to shallow sandbar where friendly stingrays swim at your feet.", "gibbs-cay-stingray-excursions.html", "Gibbs Cay"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling Tours", "Reef patches and crystal-clear water on guided snorkel trips from the port.", "grand-turk-snorkelling-tours.html", "Snorkelling"),
        (ISLAND_IMG, ISLAND_ALT, "Island Tours", "Cockburn Town, lighthouse views and Grand Turk highlights by van or tram.", "grand-turk-island-tours.html", "Island Tours"),
    ])
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Grand Turk Cruise Center</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Guests<br/><span class="text-ocean-600">Choose Grand Turk</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">Grand Turk is built for cruise passengers — the pier sits beside a swimmable beach with turquoise water. Gibbs Cay stingrays, snorkelling and island sightseeing fit a typical <strong>6–9 hour</strong> port call without long transfers.</p>
        <a href="best-grand-turk-shore-excursions.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Browse All Excursions</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top Grand Turk Experiences</h2></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Grand Turk Port Day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="grand-turk-cruise-port-guide.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="grand-turk-faq.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">FAQ</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid([
        (BEACH_BREAK_IMG, BEACH_BREAK_ALT, "Cruise Center Beach", "Walk-off beach day with loungers and turquoise swim.", "grand-turk-beach-breaks.html", "Beach Breaks"),
        (GIBBS_IMG, GIBBS_ALT, "Gibbs Cay Stingrays", "Shallow-water stingray encounters on a short boat trip.", "gibbs-cay-stingray-excursions.html", "Gibbs Cay"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling Tours", "Reef snorkelling in Grand Turk's famously clear water.", "grand-turk-snorkelling-tours.html", "Snorkelling"),
        (PRIVATE_IMG, PRIVATE_ALT, "Private Tours", "Custom island routes for your group.", "grand-turk-private-tours.html", "Private"),
    ])
    snap = _snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Grand Turk Shore Excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Operators meet at <strong>Grand Turk Cruise Center</strong> and plan returns with buffer before all aboard.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_port() -> str:
    snap = _snapshot_default(
        activity_level="Low at terminal; moderate on boat tours",
        popular="Walk-on beach, Gibbs Cay boats, island tours",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 leading-relaxed text-sm">Ships dock at <strong>Grand Turk Cruise Center</strong> — a purpose-built pier with beach, shops and excursion desks steps from the gangway on a typical <strong>6–9 hour</strong> call.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-turk-100"><h3 class="font-display font-bold text-lg mb-2">Grand Turk Cruise Center</h3><p class="text-gray-600">The pier connects directly to a swimmable beach, Margaritaville, shops and tour kiosks — many guests never leave the complex.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-turk-100"><h3 class="font-display font-bold text-lg mb-2">Beyond the Pier</h3><p class="text-gray-600">Gibbs Cay stingray boats, snorkel trips, golf cart rentals and island tours depart from the Cruise Center or nearby docks.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-3 gap-6 text-sm">
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">US dollar (USD) is the official currency. Cards and cash widely accepted at the port and on tours.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English is the official language. Guides and port staff speak clear English for cruise guests.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Walk the Cruise Center beach; taxis, golf carts and organised tours for Gibbs Cay, snorkelling and Cockburn Town.</p></div>
      </div>
      <p class="text-center mt-8"><a href="one-day-in-grand-turk.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(best_for="Cruise Center beach morning + Gibbs Cay or snorkel afternoon")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">Sample timeline for a <strong>6–9 hour</strong> Grand Turk call. Adjust for your ship's actual times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Grand Turk Port Day</h2>
      <ol class="space-y-4 text-sm">
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-turk-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Walk to the beach</strong><p class="text-gray-600 mt-1">Step off the pier onto Cruise Center sand — morning water is calm and clear.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-turk-100"><span class="font-bold text-ocean-600 shrink-0">10:00</span><div><strong>Gibbs Cay or snorkel trip</strong><p class="text-gray-600 mt-1">Book a mid-morning boat for stingrays at Gibbs Cay or a reef snorkel — both are cruise favourites.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-turk-100"><span class="font-bold text-ocean-600 shrink-0">13:00</span><div><strong>Cockburn Town or lighthouse</strong><p class="text-gray-600 mt-1">Short island tour to historic Cockburn Town or the Grand Turk Lighthouse viewpoint.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-turk-100"><span class="font-bold text-ocean-600 shrink-0">15:00</span><div><strong>Return to Cruise Center</strong><p class="text-gray-600 mt-1">Final swim, shops or a cold drink before heading back to the ship.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-turk-100"><span class="font-bold text-ocean-600 shrink-0">16:30</span><div><strong>Back at ship</strong><p class="text-gray-600 mt-1">Allow margin before published all-aboard.</p></div></li>
      </ol>
      <div class="mt-10">{_internal_links()}</div>
    </div></section>"""


def _content_gibbs() -> str:
    return _content_excursion_page(
        "Gibbs Cay is a tiny uninhabited sandbar a short boat ride from Grand Turk — shallow turquoise water where southern stingrays glide around your feet. It is the signature excursion for cruise passengers who want a memorable wildlife encounter without a long journey.",
        [
            "15–20 minute boat ride from Grand Turk Cruise Center.",
            "Shallow water suits most ages — guides help first-timers.",
            "Usually 2–3 hours total including boat time and beach stop.",
            "Pair with Cruise Center beach only on longer port calls.",
        ],
        dict(
            best_for="Wildlife lovers and first-time visitors",
            activity_level="Low to moderate — boat and wading",
            popular="Gibbs Cay stingray swim, stingray and snorkel combos",
        ),
        GIBBS_IMG,
        GIBBS_ALT,
    )


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "Grand Turk sits on a wall drop-off with famously clear turquoise water — snorkel tours visit reef patches teeming with tropical fish, often combined with Gibbs Cay or a beach stop. Gear and guides depart from the Cruise Center area.",
        [
            "Half-day trips fit most 6–9 hour port schedules.",
            "Beginners welcome — flotation aids often available.",
            "Use reef-safe sunscreen or a rash guard.",
            "Calm mornings offer the best visibility.",
        ],
        dict(
            best_for="Reef swimmers and clear-water fans",
            activity_level="Moderate — boat and snorkelling",
            popular="Reef snorkel tours, Gibbs Cay combo snorkel",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_beach_breaks() -> str:
    return _content_excursion_page(
        "Grand Turk Cruise Center was designed so passengers walk straight from ship to beach — white sand, turquoise water, loungers and beach bars without a taxi or transfer. Organised beach breaks add chair packages and cruise-timed peace of mind.",
        [
            "Zero transfer — beach is steps from the gangway.",
            "Loungers and umbrellas available for rent on site.",
            "Lowest-effort option for relaxed port days.",
            "Governor's Beach is a short taxi for a quieter stretch.",
        ],
        dict(
            best_for="Beach lovers who want minimal logistics",
            activity_level="Low — swimming and sun",
            popular="Cruise Center beach day, lounger packages",
        ),
        BEACH_BREAK_IMG,
        BEACH_BREAK_ALT,
    )


def _content_governors() -> str:
    return _content_excursion_page(
        "Governor's Beach sits south of the Cruise Center on Grand Turk's leeward coast — powdery white sand, shallow turquoise water and fewer crowds than the pier beach. Short taxi or organised transfers make it an easy upgrade for cruise guests.",
        [
            "5–10 minute taxi from Grand Turk Cruise Center.",
            "Calm water suits families and relaxed swimmers.",
            "Less commercial than the Cruise Center strip.",
            "Often paired with a lighthouse or town stop.",
        ],
        dict(
            best_for="Quieter beach seekers",
            activity_level="Low — swimming and walking",
            popular="Governor's Beach transfers, beach and island combos",
        ),
        GOVERNORS_IMG,
        GOVERNORS_ALT,
    )


def _content_island() -> str:
    return _content_excursion_page(
        "Island sightseeing tours cover Grand Turk's highlights in one loop — historic Cockburn Town, salt pond views, the Grand Turk Lighthouse and photo stops along the turquoise coast. Air-conditioned vans and open trams suit guests who want an overview on a first visit.",
        [
            "2–4 hour loops fit standard port calls.",
            "Cockburn Town offers colourful Bermudian-style architecture.",
            "Less physically demanding than snorkel or stingray trips.",
            "Private options let you prioritise town vs lighthouse.",
        ],
        dict(
            best_for="Sightseers and first-time visitors",
            activity_level="Low — van or tram touring",
            popular="Cockburn Town tours, island highlight drives",
        ),
        ISLAND_IMG,
        ISLAND_ALT,
    )


def _content_golf_cart() -> str:
    return _content_excursion_page(
        "Golf cart and tram tours let you explore Grand Turk's coastline and Cockburn Town at a relaxed pace — popular with guests who want fresh air and photo stops without a full coach tour. Rentals and guided cart routes depart near the Cruise Center.",
        [
            "1.5–3 hours depending on route and rental terms.",
            "Self-drive carts need a valid licence — guided options available.",
            "Coastal roads offer lighthouse and beach viewpoints.",
            "Ideal add-on after a morning beach swim.",
        ],
        dict(
            best_for="Independent explorers and photo stops",
            activity_level="Low — cart driving or riding",
            popular="Golf cart rentals, guided tram tours",
        ),
        GOLF_IMG,
        GOLF_ALT,
    )


def _content_lighthouse() -> str:
    return _content_excursion_page(
        "The Grand Turk Lighthouse stands on the island's northern tip — a historic cast-iron tower with Atlantic views and salt industry heritage nearby. Lighthouse tours combine the climb or viewpoint stop with Cockburn Town or coastal drives.",
        [
            "Often bundled with island sightseeing tours.",
            "Short walk from parking — moderate steps at the site.",
            "Best photo light in morning or late afternoon.",
            "Check if interior access is included on your tour.",
        ],
        dict(
            best_for="History buffs and viewpoint seekers",
            activity_level="Low to moderate — walking at site",
            popular="Lighthouse and town tours, northern coast drives",
        ),
        LIGHTHOUSE_IMG,
        LIGHTHOUSE_ALT,
    )


def _content_private() -> str:
    return _content_excursion_page(
        "Private SUVs, vans and boats let your group set the pace — Gibbs Cay first, snorkel reef, Governor's Beach and Cockburn Town in one custom loop. Drivers serving cruise guests understand all-aboard deadlines at Grand Turk Cruise Center.",
        [
            "Split cost across families to rival per-person coach pricing.",
            "Share priorities when booking — routes are flexible.",
            "Ideal for mixed mobility within one group.",
            "Confirm return time in writing before payment.",
        ],
        dict(
            best_for="Groups wanting custom pacing",
            activity_level="Low to moderate — varies by itinerary",
            popular="Private island tours, custom Gibbs Cay charters",
        ),
        PRIVATE_IMG,
        PRIVATE_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family excursions in Grand Turk favour the walk-off Cruise Center beach, gentle Gibbs Cay stingray encounters, supervised snorkel trips and relaxed island drives. Two well-paced stops beat three rushed attractions with children.",
        [
            "Cruise Center beach suits all ages with shade nearby.",
            "Gibbs Cay shallow water works for school-age kids.",
            "Private vans simplify nap timing and snack stops.",
            "Golf cart tours engage teens who want independence.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Excellent with age-appropriate tour choice",
            popular="Beach days, Gibbs Cay family trips, island tours",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_beaches() -> str:
    snap = _snapshot_default(
        best_for="Choosing Cruise Center vs Governor's Beach",
        popular="Cruise Center beach, Governor's Beach, Pillory Beach",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">Grand Turk beaches range from the pier-side Cruise Center strip to quieter coves — <strong>Cruise Center Beach</strong> for zero-transfer swim, <strong>Governor's Beach</strong> for powdery sand south of port, and <strong>Pillory Beach</strong> near Cockburn Town for a local feel.</p>
        <ul class="space-y-3 mb-6">
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Cruise Center Beach</strong> — steps from the ship, loungers, turquoise swim.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Governor's Beach</strong> — white sand, calm water, fewer crowds.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Pillory Beach</strong> — near Cockburn Town, good for island tour combos.</li>
        </ul>
        <a href="grand-turk-beach-breaks.html" class="text-ocean-600 font-semibold text-sm">Cruise Center beach breaks →</a>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Grand Turk?</summary>
        <p class="mt-4 text-sm text-gray-500">Most Grand Turk calls are 6 to 9 hours. A Cruise Center beach morning plus Gibbs Cay or snorkel trip fits comfortably with return buffer.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is there a beach at the cruise port?</summary>
        <p class="mt-4 text-sm text-gray-500">Yes — Grand Turk Cruise Center has a swimmable beach steps from the pier. You can walk straight from ship to turquoise water without a transfer.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is Gibbs Cay?</summary>
        <p class="mt-4 text-sm text-gray-500">Gibbs Cay is a small sandbar off Grand Turk where southern stingrays swim in shallow water. Short boat trips from the Cruise Center are the most popular organised excursion.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Beach day or Gibbs Cay for a port day?</summary>
        <p class="mt-4 text-sm text-gray-500">Stay at the Cruise Center beach for the easiest relaxed day; book Gibbs Cay for a signature stingray experience. Many guests do beach in the morning and a boat trip mid-day.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship tours guarantee the vessel waits if the operator is late. Reputable Grand Turk operators plan returns with buffer — confirm policies and read reviews before booking ashore.</p></details>
      {_internal_links()}
    </div></section>"""


def _faq_schema() -> dict:
    qa = [
        (
            "How long do cruise ships stay in Grand Turk?",
            "Most Grand Turk calls are 6 to 9 hours.",
        ),
        (
            "Is there a beach at the cruise port?",
            "Yes — Grand Turk Cruise Center has a swimmable beach steps from the pier.",
        ),
        (
            "What is Gibbs Cay?",
            "A small sandbar off Grand Turk with shallow-water southern stingray encounters.",
        ),
        (
            "Beach day or Gibbs Cay for a port day?",
            "Cruise Center beach for ease; Gibbs Cay for stingrays — many guests combine both.",
        ),
        (
            "Ship excursion or book independently?",
            "Ship tours guarantee wait-if-late; reputable locals plan buffer returns.",
        ),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def main() -> None:
    print("Building Grand Turk Shore Excursion site…")

    write(
        "partials/nav.html",
        f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-turk-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Grand Turk<br/><span class="text-[10px] font-body font-normal text-turk-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-grand-turk-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="grand-turk-beach-breaks.html" data-nav="beach" class="text-gray-600 hover:text-ocean-600 transition-colors">Beach</a>
        <a href="gibbs-cay-stingray-excursions.html" data-nav="gibbs" class="text-gray-600 hover:text-ocean-600 transition-colors">Gibbs Cay</a>
        <a href="grand-turk-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="grand-turk-island-tours.html" data-nav="island" class="text-gray-600 hover:text-ocean-600 transition-colors">Island Tours</a>
        <a href="grand-turk-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-grand-turk-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )

    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Grand Turk from the Cruise Center. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-grand-turk-shore-excursions.html" class="hover:text-white transition-colors">Best Excursions</a></li>
            <li><a href="grand-turk-beach-breaks.html" class="hover:text-white transition-colors">Beach Breaks</a></li>
            <li><a href="gibbs-cay-stingray-excursions.html" class="hover:text-white transition-colors">Gibbs Cay Stingrays</a></li>
            <li><a href="grand-turk-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="governors-beach-excursions.html" class="hover:text-white transition-colors">Governor's Beach</a></li>
            <li><a href="grand-turk-island-tours.html" class="hover:text-white transition-colors">Island Tours</a></li>
            <li><a href="grand-turk-golf-cart-tours.html" class="hover:text-white transition-colors">Golf Cart Tours</a></li>
            <li><a href="grand-turk-private-tours.html" class="hover:text-white transition-colors">Private Tours</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="grand-turk-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="one-day-in-grand-turk.html" class="hover:text-white transition-colors">One Day in Grand Turk</a></li>
            <li><a href="grand-turk-lighthouse-tours.html" class="hover:text-white transition-colors">Lighthouse Tours</a></li>
            <li><a href="best-beaches-in-grand-turk.html" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="grand-turk-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="grand-turk-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
""",
    )

    write(
        "partials/trust-strip.html",
        f"""<section class="trust-strip" aria-label="Grand Turk shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise Center Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Gibbs Cay Stingrays</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Turquoise Water</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>
""",
    )

    heroes = {
        "hero-home.html": _hero_home(),
        "hero-excursions.html": _hero_inner(
            "Grand Turk Cruise Center · Turks & Caicos",
            f"Best Grand Turk<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Cruise Center beach, Gibbs Cay stingrays, snorkelling, island tours, golf cart routes, lighthouse visits and private options for your ship schedule.",
            BEST_IMG,
            BEST_ALT,
            breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Grand Turk Cruise Center pier, walk-off beach, taxis, USD currency and how to plan shore time ashore.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Port Guide",
            cta=("best-grand-turk-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 Cruise Center", "🏖️ Pier Beach", "🐟 Gibbs Cay", "🤿 Snorkelling"],
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">Grand Turk</span>",
            "Hour-by-hour plan from gangway to departure — Cruise Center beach, Gibbs Cay or snorkel with return buffer.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="One Day in Grand Turk",
        ),
        "hero-gibbs.html": _hero_inner(
            "Gibbs Cay · Grand Turk",
            f"Gibbs Cay Stingray<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Shallow-water southern stingrays on a short boat ride from Grand Turk Cruise Center.",
            GIBBS_IMG,
            GIBBS_ALT,
            breadcrumb="Gibbs Cay Stingrays",
        ),
        "hero-snorkelling.html": _hero_inner(
            "Turquoise Reef · Grand Turk",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Snorkelling</span> Tours",
            "Reef patches and crystal-clear water — boat trips with gear from the Cruise Center.",
            SNORKEL_IMG,
            SNORKEL_ALT,
            breadcrumb="Snorkelling Tours",
        ),
        "hero-beach-breaks.html": _hero_inner(
            "Walk-Off Beach · Grand Turk",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Beach Breaks</span>",
            "Step from ship to white sand and turquoise water at Grand Turk Cruise Center.",
            BEACH_BREAK_IMG,
            BEACH_BREAK_ALT,
            breadcrumb="Beach Breaks",
        ),
        "hero-governors.html": _hero_inner(
            "South Coast · Grand Turk",
            f"Governor's Beach<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Powdery white sand and calm turquoise water a short ride from the Cruise Center.",
            GOVERNORS_IMG,
            GOVERNORS_ALT,
            breadcrumb="Governor's Beach",
        ),
        "hero-island.html": _hero_inner(
            "Sightseeing · Grand Turk",
            f"Grand Turk Island<br/><span class=\"{ACCENT}\">Tours</span>",
            "Cockburn Town, coastal viewpoints and salt pond heritage by van or tram.",
            ISLAND_IMG,
            ISLAND_ALT,
            breadcrumb="Island Tours",
        ),
        "hero-golf-cart.html": _hero_inner(
            "Explore at Your Pace",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Golf Cart</span> Tours",
            "Coastal roads, Cockburn Town and lighthouse viewpoints on cart and tram routes.",
            GOLF_IMG,
            GOLF_ALT,
            breadcrumb="Golf Cart Tours",
        ),
        "hero-lighthouse.html": _hero_inner(
            "Northern Tip · Grand Turk",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Lighthouse</span> Tours",
            "Historic cast-iron lighthouse with Atlantic views and island heritage stops.",
            LIGHTHOUSE_IMG,
            LIGHTHOUSE_ALT,
            breadcrumb="Lighthouse Tours",
        ),
        "hero-private.html": _hero_inner(
            "Custom Shore Trips",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Private Tours</span>",
            "Private vans and boats at your group's pace — Gibbs Cay, snorkel, beaches and custom routes.",
            PRIVATE_IMG,
            PRIVATE_ALT,
            breadcrumb="Private Tours",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Family</span> Excursions",
            "Walk-off beach, gentle Gibbs Cay stingrays and relaxed island drives for every generation.",
            FAMILY_IMG,
            FAMILY_ALT,
            breadcrumb="Family Excursions",
        ),
        "hero-beaches.html": _hero_inner(
            "Beach Guide · Grand Turk",
            f"Best Beaches<br/><span class=\"{ACCENT}\">in Grand Turk</span>",
            "Cruise Center Beach, Governor's Beach and Pillory Beach — choose the right sand for your port day.",
            BEACHES_IMG,
            BEACHES_ALT,
            breadcrumb="Best Beaches",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Cruise Center port hours, Gibbs Cay stingrays, beach vs boat tours and independent vs ship booking.",
            FAQ_IMG,
            FAQ_ALT,
            breadcrumb="FAQ",
        ),
    }
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = {
        "home.html": _content_home(),
        "best-grand-turk-shore-excursions.html": _content_best(),
        "grand-turk-cruise-port-guide.html": _content_port(),
        "one-day-in-grand-turk.html": _content_one_day(),
        "gibbs-cay-stingray-excursions.html": _content_gibbs(),
        "grand-turk-snorkelling-tours.html": _content_snorkelling(),
        "grand-turk-beach-breaks.html": _content_beach_breaks(),
        "governors-beach-excursions.html": _content_governors(),
        "grand-turk-island-tours.html": _content_island(),
        "grand-turk-golf-cart-tours.html": _content_golf_cart(),
        "grand-turk-lighthouse-tours.html": _content_lighthouse(),
        "grand-turk-private-tours.html": _content_private(),
        "grand-turk-family-excursions.html": _content_family(),
        "best-beaches-in-grand-turk.html": _content_beaches(),
        "grand-turk-faq.html": _content_faq(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Cruise Center Beach, Gibbs Cay &amp; Snorkelling Tours",
            description="Plan Grand Turk shore excursions for cruise passengers — Cruise Center beach, Gibbs Cay stingrays, snorkelling, island tours, golf cart routes and private trips from Grand Turk Cruise Center.",
            keywords="Grand Turk shore excursions, Grand Turk cruise excursions, Gibbs Cay stingray tour, Grand Turk Cruise Center beach, Turks and Caicos cruise port tours",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for Grand Turk cruise shore excursions from the Cruise Center",
            },
        ),
        dict(
            file="best-grand-turk-shore-excursions.html",
            title="Best Grand Turk Shore Excursions | Compare Cruise Center Tours",
            description="Compare the best Grand Turk shore excursions — Cruise Center beach, Gibbs Cay stingrays, snorkelling, island tours, golf cart routes, lighthouse visits and private options with cruise timing.",
            keywords="best Grand Turk shore excursions, Grand Turk cruise port tours, compare Grand Turk excursions, Gibbs Cay cruise tour",
            path="best-grand-turk-shore-excursions.html",
            data_page="excursions",
            hero="partials/hero-excursions.html",
            content="best-grand-turk-shore-excursions.html",
            preload=BEST_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": "Best Grand Turk Shore Excursions",
                "url": f"{DOMAIN}/best-grand-turk-shore-excursions.html",
            },
        ),
        dict(
            file="grand-turk-cruise-port-guide.html",
            title="Grand Turk Cruise Port Guide | Cruise Center for Passengers",
            description="Grand Turk cruise port guide — Cruise Center pier, walk-off beach, taxis, USD currency and top shore excursions timed for your ship's schedule.",
            keywords="Grand Turk cruise port guide, Grand Turk Cruise Center, Grand Turk port day, cruise passenger guide Turks and Caicos",
            path="grand-turk-cruise-port-guide.html",
            data_page="port",
            hero="partials/hero-port-guide.html",
            content="grand-turk-cruise-port-guide.html",
            preload=PORT_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": "Grand Turk Cruise Port Guide",
                "url": f"{DOMAIN}/grand-turk-cruise-port-guide.html",
            },
        ),
        dict(
            file="one-day-in-grand-turk.html",
            title="One Day in Grand Turk from a Cruise Ship | Port Itinerary",
            description="How to spend one day in Grand Turk on a cruise stop — Cruise Center beach, Gibbs Cay and snorkel sample timeline with return-to-ship buffer.",
            keywords="one day in Grand Turk cruise, Grand Turk port day itinerary, Cruise Center cruise stop planning",
            path="one-day-in-grand-turk.html",
            data_page="port",
            hero="partials/hero-one-day.html",
            content="one-day-in-grand-turk.html",
            preload=ONE_DAY_IMG,
        ),
        dict(
            file="gibbs-cay-stingray-excursions.html",
            title="Gibbs Cay Stingray Excursions | Grand Turk Cruise Shore Tours",
            description="Gibbs Cay stingray excursions from Grand Turk Cruise Center — shallow-water southern stingrays on short boat trips with cruise-friendly returns.",
            keywords="Gibbs Cay stingray excursion Grand Turk, stingray swim cruise port, Gibbs Cay shore excursion Turks and Caicos",
            path="gibbs-cay-stingray-excursions.html",
            data_page="gibbs",
            hero="partials/hero-gibbs.html",
            content="gibbs-cay-stingray-excursions.html",
            preload=GIBBS_IMG,
        ),
        dict(
            file="grand-turk-snorkelling-tours.html",
            title="Grand Turk Snorkelling Tours | Reef Cruise Excursions",
            description="Grand Turk snorkelling tours from the Cruise Center — reef patches, tropical fish and crystal-clear turquoise water with cruise-friendly returns.",
            keywords="Grand Turk snorkelling tour cruise, reef snorkel Grand Turk, snorkel shore excursion Turks and Caicos",
            path="grand-turk-snorkelling-tours.html",
            data_page="snorkelling",
            hero="partials/hero-snorkelling.html",
            content="grand-turk-snorkelling-tours.html",
            preload=SNORKEL_IMG,
        ),
        dict(
            file="grand-turk-beach-breaks.html",
            title="Grand Turk Beach Breaks | Cruise Center Shore Excursions",
            description="Grand Turk beach breaks at the Cruise Center — walk from ship to white sand, turquoise water, loungers and cruise-timed returns.",
            keywords="Grand Turk beach break cruise, Cruise Center beach excursion, walk off beach Grand Turk shore excursion",
            path="grand-turk-beach-breaks.html",
            data_page="beach",
            hero="partials/hero-beach-breaks.html",
            content="grand-turk-beach-breaks.html",
            preload=BEACH_BREAK_IMG,
        ),
        dict(
            file="governors-beach-excursions.html",
            title="Governor's Beach Excursions | Grand Turk Cruise Shore Tours",
            description="Governor's Beach excursions from Grand Turk Cruise Center — white sand, calm turquoise water and quieter beach time with organised transfers.",
            keywords="Governor's Beach excursion Grand Turk, Governor Beach cruise tour, Grand Turk beach shore excursion",
            path="governors-beach-excursions.html",
            data_page="beach",
            hero="partials/hero-governors.html",
            content="governors-beach-excursions.html",
            preload=GOVERNORS_IMG,
        ),
        dict(
            file="grand-turk-island-tours.html",
            title="Grand Turk Island Tours | Cockburn Town &amp; Sightseeing",
            description="Grand Turk island tours for cruise passengers — Cockburn Town, coastal viewpoints and salt pond heritage with cruise-friendly returns.",
            keywords="Grand Turk island tour cruise, Cockburn Town excursion, sightseeing Grand Turk shore excursion",
            path="grand-turk-island-tours.html",
            data_page="island",
            hero="partials/hero-island.html",
            content="grand-turk-island-tours.html",
            preload=ISLAND_IMG,
        ),
        dict(
            file="grand-turk-golf-cart-tours.html",
            title="Grand Turk Golf Cart Tours | Cruise Port Exploration",
            description="Grand Turk golf cart and tram tours from the Cruise Center — coastal roads, Cockburn Town and lighthouse viewpoints at a relaxed pace.",
            keywords="Grand Turk golf cart tour cruise, tram tour Grand Turk, golf cart rental shore excursion",
            path="grand-turk-golf-cart-tours.html",
            data_page="island",
            hero="partials/hero-golf-cart.html",
            content="grand-turk-golf-cart-tours.html",
            preload=GOLF_IMG,
        ),
        dict(
            file="grand-turk-lighthouse-tours.html",
            title="Grand Turk Lighthouse Tours | Historic Island Excursions",
            description="Grand Turk Lighthouse tours for cruise passengers — historic tower, Atlantic views and heritage stops combined with island sightseeing.",
            keywords="Grand Turk Lighthouse tour cruise, lighthouse excursion Grand Turk, northern coast tour Turks and Caicos",
            path="grand-turk-lighthouse-tours.html",
            data_page="island",
            hero="partials/hero-lighthouse.html",
            content="grand-turk-lighthouse-tours.html",
            preload=LIGHTHOUSE_IMG,
        ),
        dict(
            file="grand-turk-private-tours.html",
            title="Grand Turk Private Tours | Custom Cruise Shore Excursions",
            description="Private Grand Turk tours for cruise passengers — custom vans and boats with flexible Gibbs Cay, snorkel and island itineraries.",
            keywords="Grand Turk private tours cruise, private shore excursion Grand Turk, custom Cruise Center tour",
            path="grand-turk-private-tours.html",
            data_page="private",
            hero="partials/hero-private.html",
            content="grand-turk-private-tours.html",
            preload=PRIVATE_IMG,
        ),
        dict(
            file="grand-turk-family-excursions.html",
            title="Grand Turk Family Excursions | Kid-Friendly Cruise Tours",
            description="Family-friendly Grand Turk excursions — Cruise Center beach, Gibbs Cay stingrays, snorkelling and relaxed island tours for cruise guests with children.",
            keywords="Grand Turk family excursions, kid friendly Grand Turk cruise tours, family shore excursion Turks and Caicos",
            path="grand-turk-family-excursions.html",
            data_page="family",
            hero="partials/hero-family.html",
            content="grand-turk-family-excursions.html",
            preload=FAMILY_IMG,
        ),
        dict(
            file="best-beaches-in-grand-turk.html",
            title="Best Beaches in Grand Turk | Cruise Center &amp; Governor's Beach",
            description="Best beaches in Grand Turk for cruise visitors — Cruise Center Beach, Governor's Beach and Pillory Beach on a port day.",
            keywords="best beaches Grand Turk cruise, Cruise Center beach Governor's Beach, beach guide Grand Turk port day",
            path="best-beaches-in-grand-turk.html",
            data_page="beaches",
            hero="partials/hero-beaches.html",
            content="best-beaches-in-grand-turk.html",
            preload=BEACHES_IMG,
        ),
        dict(
            file="grand-turk-faq.html",
            title="Grand Turk Shore Excursions FAQ | Cruise Center Planning",
            description="FAQ for Grand Turk shore excursions — Cruise Center port hours, Gibbs Cay stingrays, beach vs boat tours and independent vs ship booking.",
            keywords="Grand Turk shore excursions FAQ, Grand Turk cruise port questions, Gibbs Cay FAQ cruise",
            path="grand-turk-faq.html",
            data_page="port",
            hero="partials/hero-faq.html",
            content="grand-turk-faq.html",
            preload=FAQ_IMG,
            schema=_faq_schema(),
        ),
    ]

    for p in pages:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-grand-turk-shore-excursions.html", "0.9", "monthly"),
        ("grand-turk-cruise-port-guide.html", "0.8", "monthly"),
        ("one-day-in-grand-turk.html", "0.8", "monthly"),
        ("gibbs-cay-stingray-excursions.html", "0.9", "monthly"),
        ("grand-turk-snorkelling-tours.html", "0.9", "monthly"),
        ("grand-turk-beach-breaks.html", "0.9", "monthly"),
        ("governors-beach-excursions.html", "0.8", "monthly"),
        ("grand-turk-island-tours.html", "0.8", "monthly"),
        ("grand-turk-golf-cart-tours.html", "0.8", "monthly"),
        ("grand-turk-lighthouse-tours.html", "0.8", "monthly"),
        ("grand-turk-private-tours.html", "0.8", "monthly"),
        ("grand-turk-family-excursions.html", "0.8", "monthly"),
        ("best-beaches-in-grand-turk.html", "0.8", "monthly"),
        ("grand-turk-faq.html", "0.7", "monthly"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in urls:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write(
        "package.json",
        """{
  "name": "grand-turk-shore-excursion",
  "private": true,
  "scripts": {
    "build": "python3 scripts/build-grand-turk-site.py",
    "images": "python3 scripts/fetch-grand-turk-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8911"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""",
    )

    write(
        "wrangler.jsonc",
        """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "grand-turk-shore-excursion",
  "compatibility_date": "2026-06-06",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "grandturkshoreexcursion.com",
      "custom_domain": true
    }
  ]
}
""",
    )

    write(
        "deploy.sh",
        f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""",
    )

    (ROOT / "deploy.sh").chmod(0o755)

    write(
        "images/ATTRIBUTION.md",
        """# Image attribution

Hero and content images may be sourced from Unsplash (Unsplash License) via `npm run images`.

Replace placeholder images with your own Grand Turk photography where noted in `scripts/fetch-grand-turk-images.py` (`CUSTOM_IMAGES`).
""",
    )

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    placeholders = [
        HOME_HERO,
        BEST_IMG,
        PORT_IMG,
        ONE_DAY_IMG,
        GIBBS_IMG,
        SNORKEL_IMG,
        BEACH_BREAK_IMG,
        GOVERNORS_IMG,
        ISLAND_IMG,
        GOLF_IMG,
        LIGHTHOUSE_IMG,
        PRIVATE_IMG,
        FAMILY_IMG,
        BEACHES_IMG,
        FAQ_IMG,
        INTRO_IMG,
    ]
    for img in placeholders:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        if not p.exists() or p.stat().st_size <= 5000:
            p.write_bytes(
                b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
                b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
                b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
                b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
            )

    print("Done.")


if __name__ == "__main__":
    main()
