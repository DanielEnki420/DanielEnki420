<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-light.svg">
  <img alt="Daniel Enki — self-hosting, tools that prove they work" src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-light.svg">
</picture>

I build tools that **prove they work instead of just looking healthy** — and run
them myself, on a Raspberry Pi 5 in my living room: 35 containers, no cloud,
backed up off-site. What I publish is the part that is useful to someone else.

## Decolab — my homelab, for your Pi

<p align="center"><a href="https://github.com/DanielEnki420/decolab"><img src="https://raw.githubusercontent.com/DanielEnki420/decolab/main/docs/images/dashboard.png" alt="The Decolab dashboard: apps, CPU, RAM, disk, temperatures, monitoring, network and fan of a Raspberry Pi 5" width="80%"></a><br>
<sub>The Decolab dashboard on a Raspberry Pi 5.</sub></p>

The setup from my living room as a project anyone can install. Backups are
restored automatically and checked, monitors ask whether each service does its
job, the defaults are hardened and every release tag is signed. Pi-hole with
Unbound, Prometheus, [Perses](https://perses.dev), Uptime Kuma, Portainer and a
Samba NAS, optionally Immich and Vaultwarden — all from one plain `KEY=VALUE`
file. Shell and the Python standard library, no build step, only open projects
under neutral governance.

<a href="https://github.com/DanielEnki420/decolab"><b>&rarr; Repository</b></a> ·
<a href="https://github.com/DanielEnki420/decolab/blob/main/INSTALL.md"><b>&rarr; Install guide</b></a> ·
<code>Shell</code> <code>Python</code> · MIT or Apache-2.0 · v0.3.0, signed releases

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-correctness-checks-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-correctness-checks-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/correctness-checks">correctness-checks</a></h3>
  <p>The idea behind Decolab, as templates for any setup. A routine audit found
  three of my services dead for months behind green dashboards: Samba refusing
  every login, backups that were valid archives without the database, Portainer
  serving HTTP 200 with no Docker connection. These checks ask whether a service
  still does its job, not whether it answers — and report to a push monitor that
  turns red on its own when the report stops arriving.</p>
  <p><code>Shell</code> · MIT</p>
</td>
</tr>
</table>

## Growing

Two nutrient calculators, each a single HTML file that works offline; grow data
stays in the browser. Every feeding plan was checked against the manufacturer's
own schedule, names its source, and a test spot-checks the numbers against the
charts.

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-dwc-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-dwc-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/dwc-grower-edition">dwc-grower-edition</a></h3>
  <p>Deep water culture. Doses in ml for your reservoir, week by week, for 13 nutrient brands. Warnings for pH, EC, temperature and ORP, EC top-up calculator, water-change reminder and grow diary. Six languages.</p>
  <p><a href="https://danielenki420.github.io/dwc-grower-edition/"><b>&rarr; Live tool</b></a> ·
  <a href="https://github.com/DanielEnki420/dwc-grower-edition/blob/main/tests/brands-belege.js">dose check</a> · <code>HTML</code> · MIT</p>
</td>
</tr>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-soil-coco-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-soil-coco-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/soil-coco-grower-edition">soil-coco-grower-edition</a></h3>
  <p>Soil, coco or a mix. 21 manufacturers in 31 plans, pH and EC targets that follow the substrate, runoff tracking for salt build-up and a grow diary. Four languages.</p>
  <p><a href="https://danielenki420.github.io/soil-coco-grower-edition/"><b>&rarr; Live tool</b></a> ·
  <a href="https://github.com/DanielEnki420/soil-coco-grower-edition/blob/main/tests/coco-belege.js">dose check</a> · <code>HTML</code> · MIT</p>
</td>
</tr>
</table>

## Smaller tools

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-dns-blocklist-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-dns-blocklist-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/dns-blocklist-builder">dns-blocklist-builder</a></h3>
  <p>Builds DNS blocklists against disinformation, propaganda and tracking — 11 categories, 400+ domains, for Pi-hole, AdGuard, dnsmasq and Unbound. Runs in the browser, offline, no dependencies.</p>
  <p><a href="https://danielenki420.github.io/dns-blocklist-builder/"><b>&rarr; Live tool</b></a> · <code>HTML</code> · MIT</p>
</td>
</tr>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-atmotube-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-atmotube-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/atmotube-prometheus">atmotube-prometheus</a></h3>
  <p>Reads an Atmotube PRO air sensor over Bluetooth LE and hands particulate matter, VOC, temperature, humidity and pressure to Prometheus. When BlueZ drops half of a split reading, it fetches the gap over a short GATT connection. One Python file, no cloud, no Home Assistant.</p>
  <p><code>Python</code> · MIT</p>
</td>
</tr>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-faktenchecker-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-faktenchecker-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/faktenchecker">faktenchecker</a></h3>
  <p>An AI-assisted fact-checker in a single HTML file — no backend, no build step, no account. German and English.</p>
  <p><a href="https://danielenki420.github.io/faktenchecker/"><b>&rarr; Live tool</b></a> · <code>HTML</code> · MIT</p>
</td>
</tr>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-apple-notes-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-apple-notes-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/apple-notes-to-pages">apple-notes-to-pages</a></h3>
  <p>Merges all your Apple Notes into one Pages document with a clickable table of contents. Strictly read-only, macOS built-ins and the Python standard library only.</p>
  <p><code>Python</code> · MIT</p>
</td>
</tr>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-humanism-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-humanism-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/humanism">humanism</a></h3>
  <p>A trilingual (DE / EN / IT) landing page on secular humanism — reason, science, ethics.</p>
  <p><a href="https://humanism.lovable.app"><b>&rarr; Live site</b></a> · <code>TypeScript</code></p>
</td>
</tr>
</table>

## Olivera — built, running, for sale

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-olivera-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-olivera-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3>olivera</h3>
  <p>A platform for leasing olive trees and selling the oil directly: three Next.js apps, four Hono services, PostgreSQL, Stripe, signed lease certificates — ~86,500 lines of TypeScript. Deployed and technically complete, never put into operation (no customers, no revenue). I am selling it; a buyer switches the payment keys to live.</p>
  <p><a href="https://www.oli-vera.eu"><b>&rarr; Live platform</b></a> ·
  <a href="https://app.littleexits.com/project/olivera-olive-tree-leasing-platform"><b>&rarr; Little Exits</b></a> ·
  <a href="https://www.prerevmarket.com/production/olivera"><b>&rarr; PreRevMarket</b></a> · private repo</p>
</td>
</tr>
</table>

## The test subjects

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-katzen-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-katzen-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/katzen-analyzer">katzen-analyzer</a></h3>
  <p>Real-time FFT analysis of cat vocalizations, with AI-assisted interpretation. An entertainment project, and it says so: simple heuristics, not validated bioacoustics.</p>
  <p><a href="https://danielenki420.github.io/katzen-analyzer/"><b>&rarr; Live tool</b></a> · <code>JavaScript</code> · Apache-2.0</p>
</td>
</tr>
</table>

Every feature was tested on my two cats. They remain unconvinced.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>

<sub>Apart from the Decolab screenshot, every graphic on this page is a plain SVG generated by the scripts in this repo
(<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_banner.py"><code>banner</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_icons.py"><code>icons</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_divider.py"><code>divider</code></a>),
each in a light and a dark variant from one shared palette in
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/theme.py"><code>theme.py</code></a>.
Nothing is loaded from a third party, so the whole page follows your GitHub theme.</sub>
