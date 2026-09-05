#!/usr/bin/env python3
"""Generate Grand Turk Shore Excursion World 2.0 static site (inlined HTML)."""
from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://grandturkshoreexcursion.com"
SITE = "Grand Turk Shore Excursion"
DATE = "2026-09-05"
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
BEST_ALT = "Grand Turk shore excursion planning — beaches, boat trips and island sightseeing"
PORT_IMG = "images/grand-turk-cruise-port.png"
PORT_ALT = "Coastal view near Grand Turk cruise port area in Turks and Caicos"
ONE_DAY_IMG = "images/one-day-grand-turk.png"
ONE_DAY_ALT = "Turquoise Caribbean water for a Grand Turk cruise port day"
GIBBS_IMG = "images/gibbs-cay-stingray.png"
GIBBS_ALT = "Shallow turquoise water at Gibbs Cay near Grand Turk"
SNORKEL_IMG = "images/grand-turk-snorkelling.png"
SNORKEL_ALT = "Clear Caribbean water suitable for snorkelling near Grand Turk"
BEACH_BREAK_IMG = "images/grand-turk-beach-breaks.png"
BEACH_BREAK_ALT = "Grand Turk Cruise Center beach with GRAND TURK sign and palm trees"
GOVERNORS_IMG = "images/governors-beach.png"
GOVERNORS_ALT = "Quiet white-sand Caribbean beach similar to Governor's Beach, Grand Turk"
ISLAND_IMG = "images/grand-turk-island-tours.png"
ISLAND_ALT = "Grand Turk coastline and turquoise water on an island sightseeing day"
GOLF_IMG = "images/grand-turk-golf-cart.png"
GOLF_ALT = "Open-air exploration suited to Grand Turk golf cart style touring"
LIGHTHOUSE_IMG = "images/grand-turk-lighthouse.png"
LIGHTHOUSE_ALT = "Grand Turk Lighthouse on the northern tip of the island"
PRIVATE_IMG = "images/grand-turk-private-tours.png"
PRIVATE_ALT = "Flexible private touring scenery for a Grand Turk cruise stop"
FAMILY_IMG = "images/grand-turk-family.png"
FAMILY_ALT = "Relaxed beach day suited to families on a Grand Turk port call"
BEACHES_IMG = "images/grand-turk-beaches.png"
BEACHES_ALT = "Grand Turk Cruise Center beach with GRAND TURK sign on white wall and palm trees"
FAQ_IMG = "images/grand-turk-faq.png"
FAQ_IMG_ALT = "Cruise passengers exploring a Caribbean cruise centre"
INTRO_IMG = "images/grand-turk-intro.png"
INTRO_ALT = "Aerial view of Grand Turk coastline with turquoise water and boats"


def href(path: str) -> str:
    if not path or path == "index.html" or path == "/":
        return "/"
    p = path.removesuffix(".html").lstrip("/")
    return f"/{p}"


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(**kwargs: str) -> str:
    fields = [
        ("Typical Time In Port", kwargs.get("time_in_port", "Often around 6–9 hours — confirm your ship")),
        ("Best For", kwargs["best_for"]),
        ("Activity Level", kwargs["activity_level"]),
        ("Family Friendly", kwargs["family"]),
        ("Return Planning", kwargs["return_ship"]),
        ("Popular Excursion Types", kwargs["popular"]),
    ]
    items = "".join(
        f'<div class="cruise-snapshot__item"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in fields
    )
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">{items}</dl>
</aside>"""


def _hero_wave() -> str:
    return (
        '<div class="absolute bottom-0 left-0 right-0">'
        '<svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" '
        'class="site-hero__wave" aria-hidden="true">'
        '<path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'
    )


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
        <a href="/" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = (
            f'<a href="{href(cta[0])}" class="btn-ocean inline-flex items-center justify-center '
            f'gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
        )
    tags_html = ""
    if tags:
        tags_html = (
            '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">'
            + "".join(
                f'<span class="inline-flex items-center bg-white/10 border border-white/25 '
                f'rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
                for t in tags
            )
            + "</div>"
        )
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-cyan-300"></span>
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
    links = [
        ("grand-turk-cruise-port-guide", "Port Guide"),
        ("best-grand-turk-shore-excursions", "Best Excursions"),
        ("best-beaches-in-grand-turk", "Best Beaches"),
        ("gibbs-cay-stingray-excursions", "Gibbs Cay"),
        ("grand-turk-snorkelling-tours", "Snorkelling"),
        ("grand-turk-beach-breaks", "Beach Breaks"),
        ("governors-beach-excursions", "Governor's Beach"),
        ("one-day-in-grand-turk", "One Day"),
        ("grand-turk-faq", "FAQ"),
    ]
    parts = []
    for i, (path, label) in enumerate(links):
        if i:
            parts.append('<span class="text-gray-300">·</span>')
        parts.append(
            f'<a href="{href(path)}" class="text-ocean-600 hover:text-ocean-800 font-medium">{label}</a>'
        )
    return f"""<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Grand Turk guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">{"".join(parts)}</div>
</nav>"""


def _snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="Often around 6–9 hours — confirm your ship",
        best_for="Cruise Center beach, Gibbs Cay, snorkelling, island tours",
        activity_level="Varies — see comparison",
        family="Often suitable with age-appropriate choices",
        return_ship="Plan a conservative buffer before all-aboard; confirm with your operator",
        popular="Beach time, Gibbs Cay boat trips, snorkelling, island tours",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(
            f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-turk-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{href(link)}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>"""
        )
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _comparison_section() -> str:
    rows = [
        ("Cruise Center Beach", "Flexible", "Walk-off beach day", "Low — swim &amp; relax", "grand-turk-beach-breaks"),
        ("Gibbs Cay", "Often ~2–3 hrs", "Boat trip + sandbar stop", "Low to moderate", "gibbs-cay-stingray-excursions"),
        ("Snorkelling", "Often ~2–3 hrs", "Reef &amp; clear water", "Moderate — swim", "grand-turk-snorkelling-tours"),
        ("Island Tour", "Often ~2–4 hrs", "Cockburn Town &amp; viewpoints", "Low — van touring", "grand-turk-island-tours"),
        ("Golf Cart Tour", "Often ~1.5–3 hrs", "Coastline &amp; town at your pace", "Low — self-drive/ride", "grand-turk-golf-cart-tours"),
        ("Lighthouse Visit", "Often ~2–3 hrs", "Historic lighthouse &amp; views", "Low to moderate", "grand-turk-lighthouse-tours"),
        ("Private Tour", "Flexible", "Custom pacing for groups", "Varies", "grand-turk-private-tours"),
    ]
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-turk-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{href(link)}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{href(link)}" class="text-turk-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Grand Turk Excursion Fits Your Call?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match beach time, Gibbs Cay, snorkelling or island sightseeing to the shore time your ship actually gives you. Durations below are typical planning ranges — not guarantees.</p>
  <div class="overflow-x-auto rounded-3xl border border-turk-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Option</th>
          <th class="py-4 px-3 font-semibold">Typical duration</th>
          <th class="py-4 px-3 font-semibold">Best for</th>
          <th class="py-4 px-3 font-semibold">Activity</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _content_excursion_page(intro: str, bullets: list[str], snapshot_kwargs: dict, img: str, alt: str, extra: str = "") -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
        {extra}
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


# ----- Content pages -----


def _content_home() -> str:
    cards = _card_grid(
        [
            (BEACH_BREAK_IMG, BEACH_BREAK_ALT, "Cruise Center Beach", "Step off the ship onto white sand and clear turquoise water — often with no transfer.", "grand-turk-beach-breaks", "Beach Breaks"),
            (GIBBS_IMG, GIBBS_ALT, "Gibbs Cay", "Short boat ride to a sandbar known for shallow-water stingray encounters — wildlife not guaranteed.", "gibbs-cay-stingray-excursions", "Explore Gibbs Cay"),
            (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling Tours", "Reef patches and clear water on guided snorkel trips from the port area.", "grand-turk-snorkelling-tours", "See snorkelling"),
            (ISLAND_IMG, ISLAND_ALT, "Island Tours", "Cockburn Town, lighthouse views and Grand Turk highlights by van or tram.", "grand-turk-island-tours", "Plan an island day"),
        ]
    )
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Grand Turk Cruise Center</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why cruise guests<br/><span class="text-ocean-600">plan carefully here</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">Grand Turk’s pier sits beside a swimmable beach. Many guests stay at the Cruise Center; others take a boat to Gibbs Cay or a short island loop. Shore time depends on your ship — confirm arrival and all-aboard before you commit to anything far from the pier.</p>
        <div class="flex flex-wrap gap-3">
          <a href="{href('best-grand-turk-shore-excursions')}" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Compare excursions</a>
          <a href="{href('best-beaches-in-grand-turk')}" class="btn-outline-ocean inline-flex items-center gap-2 font-semibold px-7 py-3.5 rounded-full text-sm">Best beaches</a>
        </div>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Popular Grand Turk experiences</h2>
      <p class="text-gray-600 text-sm mt-3 max-w-2xl mx-auto">Editorial guides only in this phase — we do not take bookings or payments on this site.</p></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan your Grand Turk port day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="{href('grand-turk-cruise-port-guide')}" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="{href('one-day-in-grand-turk')}" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">One Day</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid(
        [
            (BEACH_BREAK_IMG, BEACH_BREAK_ALT, "Cruise Center Beach", "Walk-off beach day with loungers and turquoise swim.", "grand-turk-beach-breaks", "Compare beaches"),
            (GIBBS_IMG, GIBBS_ALT, "Gibbs Cay", "Signature boat trip — stingrays sometimes present, never guaranteed.", "gibbs-cay-stingray-excursions", "Explore Gibbs Cay"),
            (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling Tours", "Reef snorkelling in clear water from the port area.", "grand-turk-snorkelling-tours", "See snorkelling"),
            (PRIVATE_IMG, PRIVATE_ALT, "Private Tours", "Custom island routes when you want flexible pacing.", "grand-turk-private-tours", "Read the guide"),
        ]
    )
    snap = _snapshot_default(best_for="Comparing excursion types before you book elsewhere", popular="See comparison table")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Grand Turk shore excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Use this hub to compare styles of day — beach, boat, snorkel or sightseeing — then read the individual guides. This site does not sell tickets or show live availability.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_beaches() -> str:
    snap = _snapshot_default(
        best_for="Choosing Cruise Center vs Governor's Beach vs a Gibbs Cay boat day",
        popular="Cruise Center Beach, Governor's Beach, Pillory Beach context",
        return_ship="Stay close to the pier on short calls; allow extra time for taxis or boats",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6">
      <p class="text-gray-600 leading-relaxed mb-6">Grand Turk’s beach story for cruise passengers is simple: the pier-side <strong>Cruise Center Beach</strong> is the easy default; <a href="{href('governors-beach-excursions')}" class="text-ocean-600 font-semibold">Governor’s Beach</a> is a quieter stretch a short ride south; <strong>Pillory Beach</strong> sits nearer Cockburn Town and suits island-tour combos more than a pure walk-off swim. <a href="{href('gibbs-cay-stingray-excursions')}" class="text-ocean-600 font-semibold">Gibbs Cay</a> is a boat excursion to a sandbar — valuable, but not “just another beach day”.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
      <div>{snap}</div>
    </div></div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 space-y-8">
      <article class="bg-white rounded-3xl p-6 border border-turk-100">
        <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Cruise Center Beach</h2>
        <p class="text-gray-600 text-sm leading-relaxed mb-3"><strong>Best for:</strong> lowest logistics, short calls, families who want shade and shops nearby.</p>
        <p class="text-gray-600 text-sm leading-relaxed mb-3">You can walk from the ship to sand and turquoise water. Facilities and atmosphere are more commercial than quieter island beaches. You do not need to buy a tour merely to use the public walk-off beach area — organised chair packages are optional extras some guests prefer.</p>
        <p class="text-sm"><a href="{href('grand-turk-beach-breaks')}" class="text-ocean-600 font-semibold">Beach breaks guide →</a></p>
      </article>
      <article class="bg-white rounded-3xl p-6 border border-turk-100">
        <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Governor’s Beach</h2>
        <p class="text-gray-600 text-sm leading-relaxed mb-3"><strong>Best for:</strong> a calmer swim with fewer pier crowds, when you have time for a short transfer.</p>
        <p class="text-gray-600 text-sm leading-relaxed mb-3">South of the Cruise Center on the leeward coast — powdery sand and shallow water. A short taxi or organised transfer is typical; exact fares vary, so ask on the day. Still editorial here — not a bookable product page.</p>
        <p class="text-sm"><a href="{href('governors-beach-excursions')}" class="text-ocean-600 font-semibold">Governor’s Beach guide →</a></p>
      </article>
      <article class="bg-white rounded-3xl p-6 border border-turk-100">
        <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Pillory Beach</h2>
        <p class="text-gray-600 text-sm leading-relaxed mb-3"><strong>Best for:</strong> combining a beach stop with Cockburn Town on an island loop.</p>
        <p class="text-gray-600 text-sm leading-relaxed">Nearer town than the Cruise Center strip. Useful context on sightseeing days; not always the simplest choice if your only goal is maximum swim time beside the ship.</p>
      </article>
      <article class="bg-white rounded-3xl p-6 border border-turk-100">
        <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Gibbs Cay — adjacent excursion, not a standard beach day</h2>
        <p class="text-gray-600 text-sm leading-relaxed mb-3">Gibbs Cay is a small sandbar reached by boat. It is famous for shallow-water stingray encounters, but wildlife sightings and interactions cannot be guaranteed. Treat it as a signature outing, not a substitute for a pier beach lounge.</p>
        <p class="text-sm"><a href="{href('gibbs-cay-stingray-excursions')}" class="text-ocean-600 font-semibold">Gibbs Cay guide →</a>
        · <a href="{href('grand-turk-cruise-port-guide')}" class="text-ocean-600 font-semibold">Port guide →</a>
        · <a href="{href('one-day-in-grand-turk')}" class="text-ocean-600 font-semibold">One day plans →</a>
        · <a href="{href('best-grand-turk-shore-excursions')}" class="text-ocean-600 font-semibold">Excursion hub →</a></p>
      </article>
    </div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _content_governors() -> str:
    extra = f"""<p class="text-sm text-gray-500 mb-4">This page is editorial planning guidance. We do not sell Governor’s Beach transfers or packages here.</p>
        <p class="text-sm"><a href="{href('best-beaches-in-grand-turk')}" class="text-ocean-600 font-semibold">← Back to Best Beaches</a>
        · <a href="{href('grand-turk-beach-breaks')}" class="text-ocean-600 font-semibold">Cruise Center beach breaks</a>
        · <a href="{href('grand-turk-cruise-port-guide')}" class="text-ocean-600 font-semibold">Port guide</a>
        · <a href="{href('one-day-in-grand-turk')}" class="text-ocean-600 font-semibold">One day</a></p>"""
    return _content_excursion_page(
        "Governor’s Beach sits south of the Cruise Center — a quieter white-sand stretch with calm, shallow water compared with the pier beach. It suits guests who want a less commercial swim and have time for a short taxi or organised transfer. Despite “excursions” in the URL, treat this as a beach-planning guide, not a checkout page.",
        [
            "Short ride from Grand Turk Cruise Center (often described as a few minutes by taxi — confirm on the day).",
            "Calmer atmosphere than the Cruise Center strip for many visitors.",
            "Good comparison point when choosing between walk-off convenience and quieter sand.",
            "Pair with a lighthouse or Cockburn Town stop only if your ship’s shore time allows.",
        ],
        dict(
            best_for="Quieter beach seekers with transfer time",
            activity_level="Low — swimming and walking",
            popular="Governor’s Beach as a quieter alternative to the pier beach",
            family="Often suitable for relaxed swimming with children",
            return_ship="Factor taxi or transfer time both ways before all-aboard",
        ),
        GOVERNORS_IMG,
        GOVERNORS_ALT,
        extra=extra,
    )


def _content_gibbs() -> str:
    extra = f"""<div class="bg-sand-50 border border-turk-100 rounded-2xl p-4 text-sm text-gray-600 mb-4">
          <p class="font-semibold text-gray-900 mb-1">Wildlife honesty</p>
          <p>Southern stingrays are the draw at Gibbs Cay, but animals move with tides, weather and crowding. Do not plan the day as if rays will definitely be present or interact on cue.</p>
        </div>
        <p class="text-sm mb-2"><a href="{href('best-grand-turk-shore-excursions')}" class="text-ocean-600 font-semibold">Compare shore excursions →</a>
        · <a href="{href('best-beaches-in-grand-turk')}" class="text-ocean-600 font-semibold">Best beaches →</a>
        · <a href="{href('grand-turk-cruise-port-guide')}" class="text-ocean-600 font-semibold">Port planning →</a></p>
        <p class="text-xs text-gray-500">Editorial only — no prices, suppliers or live checkout on this site in this phase.</p>"""
    return _content_excursion_page(
        "Gibbs Cay is a tiny uninhabited sandbar a short boat ride from Grand Turk. It is the island’s signature cruise outing: shallow turquoise water, a beach stop, and a chance — not a promise — to see southern stingrays in the shallows. It is an excursion experience, not a substitute for a simple walk-off beach day at the Cruise Center.",
        [
            "Boat transfer from the Cruise Center area (often described as a short ride).",
            "Shallow water suits many ages when conditions are calm — listen to guides on site.",
            "Typical outing length is often in the 2–3 hour range including boat time; confirm with your operator.",
            "Combine with pier beach time only when your ship’s call is long enough.",
            "Bring reef-safe habits, water shoes if you like, and a conservative return buffer.",
        ],
        dict(
            best_for="Guests wanting a signature boat outing",
            activity_level="Low to moderate — boat and wading",
            popular="Gibbs Cay sandbar trips (wildlife not guaranteed)",
            family="Often workable for school-age children when conditions allow",
            return_ship="Boat schedules must leave clear margin before all-aboard",
        ),
        GIBBS_IMG,
        GIBBS_ALT,
        extra=extra,
    )


def _content_beach_breaks() -> str:
    extra = f"""<p class="text-sm text-gray-600 mb-4">Walk-off beach access at the Cruise Center is the low-friction option. Organised beach packages (chairs, hosts, timed returns) are a different product — useful for some guests, unnecessary if you only want sand and a swim. We do not list package prices here.</p>
        <p class="text-sm"><a href="{href('best-beaches-in-grand-turk')}" class="text-ocean-600 font-semibold">Best beaches hub →</a>
        · <a href="{href('governors-beach-excursions')}" class="text-ocean-600 font-semibold">Governor’s Beach →</a></p>"""
    return _content_excursion_page(
        "Grand Turk Cruise Center was designed so passengers can walk from ship to beach — white sand, turquoise water, and port amenities without a taxi. That free/walk-off access is different from an organised beach-break package. Choose based on how much structure you want, not on the idea that you must buy a tour to use the pier beach.",
        [
            "Beach is steps from the gangway for many ships.",
            "Loungers and umbrellas may be available to rent on site — ask locally; prices change.",
            "Lowest-effort option for short or relaxed port days.",
            "Governor’s Beach is a short transfer if you want a quieter stretch.",
        ],
        dict(
            best_for="Beach lovers who want minimal logistics",
            activity_level="Low — swimming and sun",
            popular="Walk-off Cruise Center beach; optional chair packages",
            family="Often one of the simplest family choices",
            return_ship="Easy when you stay at the Cruise Center complex",
        ),
        BEACH_BREAK_IMG,
        BEACH_BREAK_ALT,
        extra=extra,
    )


def _content_port() -> str:
    snap = _snapshot_default(
        activity_level="Low at terminal; moderate on boat tours",
        popular="Walk-on beach, Gibbs Cay boats, island tours",
        best_for="Understanding the pier before you leave it",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
      <p class="text-gray-600 leading-relaxed text-sm mb-4">Ships call at <strong>Grand Turk Cruise Center</strong> — a purpose-built pier with beach, shops and excursion meeting points close to the gangway. Many guests never leave the complex; others use it as the launch point for Gibbs Cay boats, snorkel trips, taxis and golf carts.</p>
      <p class="text-gray-600 leading-relaxed text-sm">Shore time varies by ship. Treat any sample timeline as a planning sketch and verify your own arrival, departure and all-aboard times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where ships arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-turk-100"><h3 class="font-display font-bold text-lg mb-2">Grand Turk Cruise Center</h3><p class="text-gray-600">Pier, swimmable beach, shops and tour desks in one compact area. Useful if you want a low-transfer day.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-turk-100"><h3 class="font-display font-bold text-lg mb-2">Beyond the pier</h3><p class="text-gray-600">Gibbs Cay boats, snorkel trips, golf carts, taxis toward Cockburn Town, Governor’s Beach and the lighthouse. Build return time into every plan.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">US dollar (USD) is widely used. Cards and cash are commonly accepted at the port and on tours — still carry a small cash buffer.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English is the official language. Port staff and guides are used to cruise guests.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Getting around</strong><p class="mt-2 text-gray-600">Walk the Cruise Center beach; use taxis, golf carts or organised tours for further stops. Do not invent fixed fares from this page — ask on the day.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Beach choices</strong><p class="mt-2 text-gray-600">Start with <a href="{href('best-beaches-in-grand-turk')}" class="text-ocean-600 font-semibold">Best Beaches</a> for Cruise Center vs Governor’s vs Pillory context.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Gibbs Cay</strong><p class="mt-2 text-gray-600">Boat departures are organised from the port area. Read the <a href="{href('gibbs-cay-stingray-excursions')}" class="text-ocean-600 font-semibold">Gibbs Cay guide</a> before you treat it as guaranteed wildlife.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Return planning</strong><p class="mt-2 text-gray-600">Keep a conservative buffer. Your cruise line’s all-aboard time is the deadline that matters.</p></div>
      </div>
      <p class="text-center mt-8 space-x-4 text-sm">
        <a href="{href('one-day-in-grand-turk')}" class="text-ocean-600 font-semibold">One-day scenarios →</a>
        <a href="{href('best-grand-turk-shore-excursions')}" class="text-ocean-600 font-semibold">Excursion hub →</a>
      </p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(
        best_for="Choosing a realistic scenario for your ship’s shore time",
        time_in_port="Depends on your ship — sample plans assume a typical longer call",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">These scenarios are planning sketches. Actual available shore time depends on your ship’s call. Always leave a conservative buffer before all-aboard.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4 space-y-6">
      <article class="bg-white rounded-2xl p-5 border border-turk-100">
        <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Easy walk-off beach day</h2>
        <p class="text-sm text-gray-600">Stay at Cruise Center Beach: swim, shade, shops. Lowest risk on shorter calls. See <a href="{href('grand-turk-beach-breaks')}" class="text-ocean-600 font-semibold">beach breaks</a>.</p>
      </article>
      <article class="bg-white rounded-2xl p-5 border border-turk-100">
        <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Beach + light sightseeing</h2>
        <p class="text-sm text-gray-600">Morning pier beach, then a compact island loop toward Cockburn Town or the lighthouse if time remains. See <a href="{href('grand-turk-island-tours')}" class="text-ocean-600 font-semibold">island tours</a>.</p>
      </article>
      <article class="bg-white rounded-2xl p-5 border border-turk-100">
        <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Gibbs Cay excursion day</h2>
        <p class="text-sm text-gray-600">Prioritise the boat trip, then a short pier beach cool-down if the schedule allows. Wildlife is not guaranteed. See <a href="{href('gibbs-cay-stingray-excursions')}" class="text-ocean-600 font-semibold">Gibbs Cay</a>.</p>
      </article>
      <article class="bg-white rounded-2xl p-5 border border-turk-100">
        <h2 class="font-display font-bold text-lg text-gray-900 mb-2">Shorter relaxed port day</h2>
        <p class="text-sm text-gray-600">If your call is tight, skip distant transfers. Pier beach + lunch at the complex beats a rushed taxi loop.</p>
      </article>
      <div class="mt-6">{_internal_links()}</div>
    </div></section>"""


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "Grand Turk is known for clear turquoise water and nearby reef structure. Snorkel trips from the Cruise Center area visit reef patches and are sometimes combined with other stops. Conditions, sites and inclusions vary by operator — confirm details before you book elsewhere.",
        [
            "Half-day style trips often fit longer port calls.",
            "Beginners are commonly welcome; ask about flotation aids.",
            "Use reef-safe habits and listen to briefings.",
            "Calm mornings often offer better visibility — not guaranteed.",
        ],
        dict(
            best_for="Reef swimmers and clear-water fans",
            activity_level="Moderate — boat and snorkelling",
            popular="Reef snorkel tours; occasional Gibbs Cay combos",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_island() -> str:
    return _content_excursion_page(
        "Island sightseeing loops typically cover Cockburn Town’s Bermudian-style streets, coastal viewpoints and often the Grand Turk Lighthouse area. Vans and open trams suit guests who want an overview without a long transfer day.",
        [
            "Often a 2–4 hour style loop on standard calls — confirm locally.",
            "Cockburn Town is the historic capital stretch.",
            "Less physically demanding than snorkel or boat trips for many guests.",
            "Private options let you prioritise town vs lighthouse.",
        ],
        dict(
            best_for="Sightseers and first-time visitors",
            activity_level="Low — van or tram touring",
            popular="Cockburn Town and coastal highlight drives",
        ),
        ISLAND_IMG,
        ISLAND_ALT,
    )


def _content_golf_cart() -> str:
    return _content_excursion_page(
        "Golf cart and tram-style touring lets you see coastline and town at a slower pace. Self-drive carts usually need a valid licence; guided options exist. Treat rental rules and return times as operator-specific.",
        [
            "Often 1.5–3 hours depending on route and rental terms.",
            "Self-drive vs guided — choose based on comfort.",
            "Useful after a morning swim if shore time allows.",
            "Keep fuel, phone signal and return buffer in mind.",
        ],
        dict(
            best_for="Independent explorers and photo stops",
            activity_level="Low — cart driving or riding",
            popular="Golf cart rentals and guided tram-style tours",
        ),
        GOLF_IMG,
        GOLF_ALT,
    )


def _content_lighthouse() -> str:
    return _content_excursion_page(
        "The Grand Turk Lighthouse stands on the island’s northern tip — a historic cast-iron tower with Atlantic views and salt-industry heritage nearby. It is commonly bundled into island sightseeing rather than sold as a long standalone outing.",
        [
            "Often combined with Cockburn Town or coastal drives.",
            "Short walk from parking; expect some steps at the site.",
            "Interior access depends on the day and operator — ask ahead.",
            "Photo light is often nicer earlier or later in the day.",
        ],
        dict(
            best_for="History buffs and viewpoint seekers",
            activity_level="Low to moderate — walking at site",
            popular="Lighthouse plus town sightseeing",
        ),
        LIGHTHOUSE_IMG,
        LIGHTHOUSE_ALT,
    )


def _content_private() -> str:
    return _content_excursion_page(
        "Private vans, SUVs or boats let a group set the pace — beach, Gibbs Cay, snorkel or town in one custom loop. This page is editorial only: we do not broker private drivers or take payment here.",
        [
            "Useful when mobility or ages differ within one group.",
            "Agree return time clearly before you pay an operator elsewhere.",
            "Share priorities: wildlife boat vs beach vs sightseeing.",
            "Still plan a conservative buffer to the ship.",
        ],
        dict(
            best_for="Groups wanting custom pacing",
            activity_level="Low to moderate — varies by itinerary",
            popular="Private island loops and custom boat charters",
        ),
        PRIVATE_IMG,
        PRIVATE_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family days in Grand Turk usually favour the walk-off Cruise Center beach, carefully chosen boat trips, gentle snorkels and relaxed island drives. Two well-paced stops beat three rushed ones with children.",
        [
            "Cruise Center beach keeps logistics simple.",
            "Gibbs Cay can work for school-age kids when conditions allow — wildlife still not guaranteed.",
            "Private vans help with naps and snack stops.",
            "Skip distant transfers on short calls.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Often workable with age-appropriate choices",
            popular="Beach days, carefully timed boat trips, island tours",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Grand Turk?</summary>
        <p class="mt-4 text-sm text-gray-500">Many calls are often in the 6–9 hour range, but your ship may differ. Always use the times on your daily programme.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is there a beach at the cruise port?</summary>
        <p class="mt-4 text-sm text-gray-500">Yes — Grand Turk Cruise Center has a swimmable beach close to the pier. You can often walk from ship to sand without a transfer.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is Gibbs Cay?</summary>
        <p class="mt-4 text-sm text-gray-500">A small sandbar off Grand Turk reached by boat, known for shallow-water southern stingray encounters. Sightings and interactions are not guaranteed.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Beach day or Gibbs Cay?</summary>
        <p class="mt-4 text-sm text-gray-500">Stay at the Cruise Center beach for the easiest relaxed day; choose Gibbs Cay for a signature boat outing. Many guests only combine both on longer calls.</p></details>
      <details class="faq-item rounded-2xl border border-turk-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or independent?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship tours may include wait-if-late policies. Independent operators can be excellent — confirm return policies, meeting points and reviews before you pay.</p></details>
      {_internal_links()}
    </div></section>"""


def _content_about() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">About Grand Turk Shore Excursion</h1>
  <p class="text-gray-600 leading-relaxed mb-4">This site is an independent planning guide for cruise passengers calling at Grand Turk in the Turks and Caicos Islands. We help you compare beaches, Gibbs Cay boat trips, snorkelling and island sightseeing against a realistic port day from Grand Turk Cruise Center.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We do not operate tours, sell tickets or take payment on this website in this phase. If you book, you book with operators you choose separately. We are not affiliated with any cruise line.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We do not claim a physical Grand Turk office, local staff desk or first-hand operator relationships on this site.</p>
  <p class="text-gray-600 leading-relaxed">See our <a href="{href('methodology')}" class="text-ocean-600 underline">methodology</a> and <a href="{href('contact')}" class="text-ocean-600 underline">contact</a> pages.</p>
</section>"""


def _content_contact() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Contact</h1>
  <p class="text-gray-600 leading-relaxed mb-4">This site is an independent Grand Turk cruise planning guide. We do not take bookings or payments here.</p>
  <p class="text-gray-600 leading-relaxed mb-4">A public inbox for this domain is being prepared. Email routing for <span class="font-medium text-gray-800">hello@grandturkshoreexcursion.com</span> has not yet been verified as live, so please do not rely on that address until routing is confirmed.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Meanwhile, use the planning pages:</p>
  <ul class="list-disc pl-5 text-gray-600 space-y-2 mb-6">
    <li><a href="{href('one-day-in-grand-turk')}" class="text-ocean-600 underline">One day in Grand Turk</a></li>
    <li><a href="{href('best-beaches-in-grand-turk')}" class="text-ocean-600 underline">Best beaches</a></li>
    <li><a href="{href('grand-turk-cruise-port-guide')}" class="text-ocean-600 underline">Cruise port guide</a></li>
    <li><a href="{href('best-grand-turk-shore-excursions')}" class="text-ocean-600 underline">Best shore excursions</a></li>
  </ul>
  <p class="text-sm text-gray-500 leading-relaxed">When email routing is verified, this page will be updated with a working contact address.</p>
</section>"""


def _content_privacy() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Privacy</h1>
  <p class="text-gray-600 leading-relaxed mb-4">Grand Turk Shore Excursion is an editorial planning website. In this phase we do not operate an online booking or payment system on this domain.</p>
  <p class="text-gray-600 leading-relaxed mb-4">If you contact us once a verified public email is published, we will use your message only to respond to your enquiry. We do not sell personal information.</p>
  <p class="text-gray-600 leading-relaxed mb-4">This site may use standard hosting and analytics logs typical of websites served through Cloudflare. Those logs can include IP address, user agent and requested URLs.</p>
  <p class="text-gray-600 leading-relaxed">For questions about this policy, use the <a href="{href('contact')}" class="text-ocean-600 underline">contact</a> page once a working inbox is confirmed.</p>
</section>"""


def _content_terms() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Terms of use</h1>
  <p class="text-gray-600 leading-relaxed mb-4">Content on Grand Turk Shore Excursion is provided for general cruise-planning information only. It is not a booking contract, travel insurance policy or guarantee of shore time.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Operators, cruise lines, beach facilities, transport and weather change. Always verify final details with your cruise line and any operator you choose before travel.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We are not affiliated with cruise lines or third-party marketplaces. Wildlife sightings are never guaranteed.</p>
  <p class="text-gray-600 leading-relaxed">To the fullest extent permitted by law, we are not liable for decisions made solely on the basis of this editorial guidance. Plan a conservative return buffer to your ship.</p>
</section>"""


def _content_methodology() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Methodology</h1>
  <p class="text-gray-600 leading-relaxed mb-4">This site is editorial. Recommendations are independent planning guidance for Grand Turk cruise passengers, not paid placements or live inventory.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We do not invent star ratings, review counts, bestsellers or fabricated availability. Operator inclusions, prices, meeting points and timings can change — confirm details before travel.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Where exact taxi fares or chair prices cannot be verified, we avoid inventing numbers.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Wildlife sightings, including stingrays at Gibbs Cay, are never guaranteed.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Ship schedule pages are deferred in this phase. Confirm arrival, departure and all-aboard times with your cruise line.</p>
  <p class="text-gray-600 leading-relaxed">See <a href="{href('about')}" class="text-ocean-600 underline">About</a> and <a href="{href('contact')}" class="text-ocean-600 underline">Contact</a>.</p>
</section>"""


def _content_404() -> str:
    return f"""<section class="py-24 max-w-3xl mx-auto px-4 text-center">
  <h1 class="font-display text-4xl font-bold text-gray-900 mb-4">Page not found</h1>
  <p class="text-gray-600 mb-8">That URL is not part of this Grand Turk planning site.</p>
  <div class="flex flex-col sm:flex-row gap-3 justify-center text-sm">
    <a href="/" class="btn-ocean text-white font-semibold px-6 py-3 rounded-full">Home</a>
    <a href="{href('best-beaches-in-grand-turk')}" class="btn-outline-ocean font-semibold px-6 py-3 rounded-full">Best Beaches</a>
    <a href="{href('best-grand-turk-shore-excursions')}" class="btn-outline-ocean font-semibold px-6 py-3 rounded-full">Excursions</a>
  </div>
</section>"""


def _faq_schema() -> dict:
    qa = [
        ("How long do cruise ships stay in Grand Turk?", "Many calls are often in the 6–9 hour range, but always confirm your ship’s times."),
        ("Is there a beach at the cruise port?", "Yes — Grand Turk Cruise Center has a swimmable beach close to the pier."),
        ("What is Gibbs Cay?", "A small sandbar off Grand Turk reached by boat, known for shallow-water stingray encounters that cannot be guaranteed."),
        ("Beach day or Gibbs Cay?", "Cruise Center beach for ease; Gibbs Cay for a signature boat outing — combine only when shore time allows."),
        ("Ship excursion or independent?", "Ship tours may include wait-if-late policies; independent operators require you to confirm return policies yourself."),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def _nav() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-turk-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="/" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Grand Turk<br/><span class="text-[10px] font-body font-normal text-turk-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="{href('best-grand-turk-shore-excursions')}" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Shore Excursions</a>
        <a href="{href('best-beaches-in-grand-turk')}" data-nav="beaches" class="text-gray-600 hover:text-ocean-600 transition-colors">Best Beaches</a>
        <a href="{href('gibbs-cay-stingray-excursions')}" data-nav="gibbs" class="text-gray-600 hover:text-ocean-600 transition-colors">Gibbs Cay</a>
        <a href="{href('grand-turk-cruise-port-guide')}" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
        <a href="{href('one-day-in-grand-turk')}" data-nav="oneday" class="text-gray-600 hover:text-ocean-600 transition-colors">One Day</a>
      </div>
      <a href="{href('best-grand-turk-shore-excursions')}" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">Compare Tours</a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu" aria-expanded="false">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
"""


def _footer() -> str:
    return f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="/" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise visitors to Grand Turk. Not affiliated with any cruise line. We do not take bookings on this site in this phase.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="{href('best-grand-turk-shore-excursions')}" class="hover:text-white transition-colors">Best Excursions</a></li>
            <li><a href="{href('best-beaches-in-grand-turk')}" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="{href('gibbs-cay-stingray-excursions')}" class="hover:text-white transition-colors">Gibbs Cay</a></li>
            <li><a href="{href('grand-turk-beach-breaks')}" class="hover:text-white transition-colors">Beach Breaks</a></li>
            <li><a href="{href('governors-beach-excursions')}" class="hover:text-white transition-colors">Governor's Beach</a></li>
            <li><a href="{href('grand-turk-snorkelling-tours')}" class="hover:text-white transition-colors">Snorkelling</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="{href('grand-turk-cruise-port-guide')}" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="{href('one-day-in-grand-turk')}" class="hover:text-white transition-colors">One Day</a></li>
            <li><a href="{href('grand-turk-faq')}" class="hover:text-white transition-colors">FAQ</a></li>
            <li><a href="{href('about')}" class="hover:text-white transition-colors">About</a></li>
            <li><a href="{href('contact')}" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="{href('methodology')}" class="hover:text-white transition-colors">Methodology</a></li>
            <li><a href="{href('privacy')}" class="hover:text-white transition-colors">Privacy</a></li>
            <li><a href="{href('terms')}" class="hover:text-white transition-colors">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking. Wildlife sightings are not guaranteed.</p>
      </div>
    </div>
  </footer>
"""


def _trust() -> str:
    return """<section class="trust-strip" aria-label="Grand Turk planning highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise Center Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Gibbs Cay Guides</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Honest Wildlife Notes</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Independent Planning</li>
    </ul>
  </div>
</section>
"""


def page_shell(
    *,
    title: str,
    description: str,
    canonical_path: str,
    data_page: str,
    hero_html: str,
    content_html: str,
    preload: str = HOME_HERO,
    schema: dict | list | None = None,
    trust: bool = True,
    main_pad: bool = False,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path or canonical_path == "/" else f"{DOMAIN}/{canonical_path.lstrip('/')}"
    graph: list = [
        {
            "@type": "WebSite",
            "name": SITE,
            "url": f"{DOMAIN}/",
            "description": "Independent planning guide for Grand Turk cruise shore excursions",
            "inLanguage": "en-GB",
        },
        {
            "@type": "WebPage",
            "name": title.replace("&amp;", "&"),
            "url": canon,
            "description": description,
            "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{DOMAIN}/"},
            "inLanguage": "en-GB",
        },
    ]
    if schema:
        if isinstance(schema, list):
            graph.extend(schema)
        elif schema.get("@type") == "FAQPage":
            graph.append({k: v for k, v in schema.items() if k != "@context"})
        else:
            graph.append(schema)
    schema_block = (
        '  <script type="application/ld+json">\n'
        + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2)
        + "\n  </script>\n"
    )
    hero_block = (
        f'  <div id="page-hero" data-inlined="true">\n{hero_html}\n  </div>\n' if hero_html else ""
    )
    trust_block = (
        f'  <div id="page-trust-strip" data-inlined="true">\n{_trust()}\n  </div>\n' if trust else ""
    )
    main_class = ' class="pt-16"' if main_pad else ""
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta property="og:locale" content="en_GB" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{DOMAIN}/{preload}" />
{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body class="bg-white text-gray-800 antialiased" data-page="{data_page}" data-base="">
  <div id="site-nav" data-inlined="true">
{_nav()}
  </div>
{hero_block}{trust_block}  <main id="page-content" data-inlined="true"{main_class}>
{content_html}
  </main>
  <div id="site-footer" data-inlined="true">
{_footer()}
  </div>
  <script src="/js/site.js"></script>
</body>
</html>
"""


def main() -> None:
    print("Building Grand Turk Shore Excursion World 2.0…")

    write("partials/nav.html", _nav())
    write("partials/footer.html", _footer())
    write("partials/trust-strip.html", _trust())

    heroes = {
        "hero-home.html": f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-cyan-300"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Grand Turk Cruise Center · Turks &amp; Caicos</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Grand Turk Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Walk from ship to turquoise water at the Cruise Center beach — or plan Gibbs Cay, snorkelling and island sightseeing around the shore time your ship actually gives you.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="{href('best-grand-turk-shore-excursions')}" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="{href('best-beaches-in-grand-turk')}" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Best Beaches</a>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>""",
        "hero-excursions.html": _hero_inner(
            "Grand Turk Cruise Center · Turks &amp; Caicos",
            f"Best Grand Turk<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Cruise Center beach, Gibbs Cay, snorkelling, island tours and private options for your ship schedule.",
            BEST_IMG, BEST_ALT, breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Grand Turk Cruise Center pier, walk-off beach, taxis and how to plan shore time ashore.",
            PORT_IMG, PORT_ALT, breadcrumb="Port Guide",
            cta=("best-grand-turk-shore-excursions", "View Shore Excursions →"),
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Scenarios",
            f"One Day in<br/><span class=\"{ACCENT}\">Grand Turk</span>",
            "Realistic cruise-day scenarios — walk-off beach, Gibbs Cay or sightseeing — adjusted to your ship’s call.",
            ONE_DAY_IMG, ONE_DAY_ALT, breadcrumb="One Day in Grand Turk",
        ),
        "hero-gibbs.html": _hero_inner(
            "Gibbs Cay · Grand Turk",
            f"Gibbs Cay Stingray<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Signature sandbar boat trip from Grand Turk Cruise Center — wildlife encounters possible, never promised.",
            GIBBS_IMG, GIBBS_ALT, breadcrumb="Gibbs Cay",
        ),
        "hero-snorkelling.html": _hero_inner(
            "Turquoise Reef · Grand Turk",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Snorkelling</span> Tours",
            "Reef patches and clear water — boat trips from the Cruise Center area.",
            SNORKEL_IMG, SNORKEL_ALT, breadcrumb="Snorkelling Tours",
        ),
        "hero-beach-breaks.html": _hero_inner(
            "Walk-Off Beach · Grand Turk",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Beach Breaks</span>",
            "Walk-off Cruise Center beach versus organised packages — choose what you actually need.",
            BEACH_BREAK_IMG, BEACH_BREAK_ALT, breadcrumb="Beach Breaks",
        ),
        "hero-governors.html": _hero_inner(
            "South Coast · Grand Turk",
            f"Governor's Beach<br/><span class=\"{ACCENT}\">Guide</span>",
            "Quieter white sand a short ride from the Cruise Center — editorial planning, not a booking desk.",
            GOVERNORS_IMG, GOVERNORS_ALT, breadcrumb="Governor's Beach",
        ),
        "hero-island.html": _hero_inner(
            "Sightseeing · Grand Turk",
            f"Grand Turk Island<br/><span class=\"{ACCENT}\">Tours</span>",
            "Cockburn Town, coastal viewpoints and lighthouse stops by van or tram.",
            ISLAND_IMG, ISLAND_ALT, breadcrumb="Island Tours",
        ),
        "hero-golf-cart.html": _hero_inner(
            "Explore at Your Pace",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Golf Cart</span> Tours",
            "Coastal roads, Cockburn Town and viewpoints on cart and tram-style routes.",
            GOLF_IMG, GOLF_ALT, breadcrumb="Golf Cart Tours",
        ),
        "hero-lighthouse.html": _hero_inner(
            "Northern Tip · Grand Turk",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Lighthouse</span> Tours",
            "Historic cast-iron lighthouse with Atlantic views and island heritage stops.",
            LIGHTHOUSE_IMG, LIGHTHOUSE_ALT, breadcrumb="Lighthouse Tours",
        ),
        "hero-private.html": _hero_inner(
            "Custom Shore Trips",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Private Tours</span>",
            "Editorial guide to private vans and boats at your group’s pace — no checkout on this site.",
            PRIVATE_IMG, PRIVATE_ALT, breadcrumb="Private Tours",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Family</span> Excursions",
            "Walk-off beach, carefully timed boat trips and relaxed island drives for mixed ages.",
            FAMILY_IMG, FAMILY_ALT, breadcrumb="Family Excursions",
        ),
        "hero-beaches.html": _hero_inner(
            "Beach Guide · Grand Turk",
            f"Best Beaches<br/><span class=\"{ACCENT}\">in Grand Turk</span>",
            "Cruise Center Beach, Governor’s Beach and Pillory context — plus why Gibbs Cay is a boat excursion, not a standard beach day.",
            BEACHES_IMG, BEACHES_ALT, breadcrumb="Best Beaches",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            f"Grand Turk<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Port hours, Gibbs Cay wildlife honesty, beach vs boat tours and independent vs ship booking.",
            FAQ_IMG, FAQ_IMG_ALT, breadcrumb="FAQ",
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
        "about.html": _content_about(),
        "contact.html": _content_contact(),
        "privacy.html": _content_privacy(),
        "terms.html": _content_terms(),
        "methodology.html": _content_methodology(),
        "404.html": _content_404(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(file="index.html", title=f"{SITE} | Cruise Center Beach, Gibbs Cay &amp; Port Planning", description="Plan Grand Turk shore time for cruise passengers — Cruise Center beach, Gibbs Cay, snorkelling and island tours from Grand Turk Cruise Center.", path="", data_page="home", hero="hero-home.html", content="home.html", schema={"@type": "TouristDestination", "name": "Grand Turk", "description": "Turks and Caicos cruise port with Cruise Center beach and Gibbs Cay boat trips", "touristType": "Cruise passengers"}),
        dict(file="best-grand-turk-shore-excursions.html", title="Best Grand Turk Shore Excursions | Compare Cruise Port Options", description="Compare Grand Turk shore excursion styles — Cruise Center beach, Gibbs Cay, snorkelling, island tours and private options with honest timing notes.", path="best-grand-turk-shore-excursions", data_page="excursions", hero="hero-excursions.html", content="best-grand-turk-shore-excursions.html", preload=BEST_IMG),
        dict(file="grand-turk-cruise-port-guide.html", title="Grand Turk Cruise Port Guide | Cruise Center for Passengers", description="Grand Turk cruise port guide — Cruise Center pier, walk-off beach, taxis, USD and how to plan shore time without invented fares.", path="grand-turk-cruise-port-guide", data_page="port", hero="hero-port-guide.html", content="grand-turk-cruise-port-guide.html", preload=PORT_IMG),
        dict(file="one-day-in-grand-turk.html", title="One Day in Grand Turk from a Cruise Ship | Port Scenarios", description="One day in Grand Turk cruise scenarios — walk-off beach, Gibbs Cay or sightseeing — adjusted to your ship’s actual shore time.", path="one-day-in-grand-turk", data_page="oneday", hero="hero-one-day.html", content="one-day-in-grand-turk.html", preload=ONE_DAY_IMG),
        dict(file="gibbs-cay-stingray-excursions.html", title="Gibbs Cay Stingray Excursions | Grand Turk Cruise Guide", description="Gibbs Cay from Grand Turk Cruise Center — sandbar boat trip, cruise-day fit and honest wildlife caveats. Editorial only; no booking.", path="gibbs-cay-stingray-excursions", data_page="gibbs", hero="hero-gibbs.html", content="gibbs-cay-stingray-excursions.html", preload=GIBBS_IMG),
        dict(file="grand-turk-snorkelling-tours.html", title="Grand Turk Snorkelling Tours | Reef Cruise Excursions", description="Grand Turk snorkelling tours from the Cruise Center area — reef patches, clear water and cruise-day planning notes.", path="grand-turk-snorkelling-tours", data_page="snorkelling", hero="hero-snorkelling.html", content="grand-turk-snorkelling-tours.html", preload=SNORKEL_IMG),
        dict(file="grand-turk-beach-breaks.html", title="Grand Turk Beach Breaks | Walk-Off vs Organised Packages", description="Grand Turk beach breaks at the Cruise Center — clarify free walk-off beach access versus optional organised packages.", path="grand-turk-beach-breaks", data_page="beach", hero="hero-beach-breaks.html", content="grand-turk-beach-breaks.html", preload=BEACH_BREAK_IMG),
        dict(file="governors-beach-excursions.html", title="Governor's Beach Grand Turk | Cruise Passenger Beach Guide", description="Governor’s Beach near Grand Turk Cruise Center — quieter sand, transfer context and links to the Best Beaches hub. Editorial only.", path="governors-beach-excursions", data_page="beaches", hero="hero-governors.html", content="governors-beach-excursions.html", preload=GOVERNORS_IMG),
        dict(file="grand-turk-island-tours.html", title="Grand Turk Island Tours | Cockburn Town &amp; Sightseeing", description="Grand Turk island tours for cruise passengers — Cockburn Town, coastal viewpoints and lighthouse stops.", path="grand-turk-island-tours", data_page="island", hero="hero-island.html", content="grand-turk-island-tours.html", preload=ISLAND_IMG),
        dict(file="grand-turk-golf-cart-tours.html", title="Grand Turk Golf Cart Tours | Cruise Port Exploration", description="Grand Turk golf cart and tram-style tours from the Cruise Center — coastal roads and town at a relaxed pace.", path="grand-turk-golf-cart-tours", data_page="island", hero="hero-golf-cart.html", content="grand-turk-golf-cart-tours.html", preload=GOLF_IMG),
        dict(file="grand-turk-lighthouse-tours.html", title="Grand Turk Lighthouse Tours | Historic Island Excursions", description="Grand Turk Lighthouse tours for cruise passengers — historic tower, Atlantic views and heritage stops.", path="grand-turk-lighthouse-tours", data_page="island", hero="hero-lighthouse.html", content="grand-turk-lighthouse-tours.html", preload=LIGHTHOUSE_IMG),
        dict(file="grand-turk-private-tours.html", title="Grand Turk Private Tours | Custom Cruise Shore Guidance", description="Private Grand Turk tour ideas for cruise passengers — custom pacing for beaches, boats and sightseeing. Editorial only.", path="grand-turk-private-tours", data_page="private", hero="hero-private.html", content="grand-turk-private-tours.html", preload=PRIVATE_IMG),
        dict(file="grand-turk-family-excursions.html", title="Grand Turk Family Excursions | Kid-Friendly Cruise Days", description="Family-friendly Grand Turk cruise ideas — Cruise Center beach, carefully timed boat trips and relaxed island drives.", path="grand-turk-family-excursions", data_page="family", hero="hero-family.html", content="grand-turk-family-excursions.html", preload=FAMILY_IMG),
        dict(file="best-beaches-in-grand-turk.html", title="Best Beaches in Grand Turk | Cruise Center &amp; Governor's Beach", description="Best beaches in Grand Turk for cruise visitors — Cruise Center Beach, Governor’s Beach, Pillory context and Gibbs Cay as a boat excursion.", path="best-beaches-in-grand-turk", data_page="beaches", hero="hero-beaches.html", content="best-beaches-in-grand-turk.html", preload=BEACHES_IMG),
        dict(file="grand-turk-faq.html", title="Grand Turk Shore Excursions FAQ | Cruise Center Planning", description="FAQ for Grand Turk shore excursions — port hours, Gibbs Cay wildlife honesty, beach vs boat tours and independent booking.", path="grand-turk-faq", data_page="port", hero="hero-faq.html", content="grand-turk-faq.html", preload=FAQ_IMG, schema=_faq_schema()),
        dict(file="about.html", title="About | Grand Turk Shore Excursion", description="About this independent Grand Turk cruise excursion and destination planning guide.", path="about", data_page="about", hero="", content="about.html", trust=False, main_pad=True),
        dict(file="contact.html", title="Contact | Grand Turk Shore Excursion", description="Contact Grand Turk Shore Excursion for independent cruise planning questions. Bookings are not taken on this site.", path="contact", data_page="contact", hero="", content="contact.html", trust=False, main_pad=True),
        dict(file="privacy.html", title="Privacy | Grand Turk Shore Excursion", description="Privacy policy for Grand Turk Shore Excursion, an editorial cruise planning website.", path="privacy", data_page="about", hero="", content="privacy.html", trust=False, main_pad=True),
        dict(file="terms.html", title="Terms of Use | Grand Turk Shore Excursion", description="Terms of use for Grand Turk Shore Excursion editorial cruise planning content.", path="terms", data_page="about", hero="", content="terms.html", trust=False, main_pad=True),
        dict(file="methodology.html", title="Methodology | Grand Turk Shore Excursion", description="How Grand Turk Shore Excursion frames editorial recommendations — no fake ratings, availability or wildlife guarantees.", path="methodology", data_page="about", hero="", content="methodology.html", trust=False, main_pad=True),
        dict(file="404.html", title="Page Not Found | Grand Turk Shore Excursion", description="The requested Grand Turk planning page was not found.", path="404", data_page="home", hero="", content="404.html", trust=False, main_pad=True),
    ]

    for p in pages:
        hero_file = p.get("hero") or ""
        hero_html = (ROOT / "partials" / hero_file).read_text(encoding="utf-8") if hero_file else ""
        content_html = (ROOT / "content" / p["content"]).read_text(encoding="utf-8")
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero_html=hero_html,
                content_html=content_html,
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
                trust=p.get("trust", True),
                main_pad=p.get("main_pad", False),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-beaches-in-grand-turk", "0.9", "monthly"),
        ("gibbs-cay-stingray-excursions", "0.9", "monthly"),
        ("governors-beach-excursions", "0.8", "monthly"),
        ("best-grand-turk-shore-excursions", "0.9", "monthly"),
        ("grand-turk-cruise-port-guide", "0.8", "monthly"),
        ("one-day-in-grand-turk", "0.8", "monthly"),
        ("grand-turk-beach-breaks", "0.8", "monthly"),
        ("grand-turk-snorkelling-tours", "0.8", "monthly"),
        ("grand-turk-island-tours", "0.7", "monthly"),
        ("grand-turk-golf-cart-tours", "0.7", "monthly"),
        ("grand-turk-lighthouse-tours", "0.7", "monthly"),
        ("grand-turk-private-tours", "0.7", "monthly"),
        ("grand-turk-family-excursions", "0.7", "monthly"),
        ("grand-turk-faq", "0.6", "monthly"),
        ("about", "0.4", "yearly"),
        ("contact", "0.4", "yearly"),
        ("privacy", "0.3", "yearly"),
        ("terms", "0.3", "yearly"),
        ("methodology", "0.4", "yearly"),
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

    print("Done.")


if __name__ == "__main__":
    main()
