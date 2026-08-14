<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-light.svg">
  <img alt="Daniel — self-hosting, home automation, network privacy" src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-light.svg">
</picture>

> **Esse quam videri** — to be, rather than to seem.

I build small, self-contained tools and run them myself. Most of it lives on a
Raspberry Pi 5 in my living room — around 30 containers, no cloud, backed up off-site.
What I publish is the part that is useful to someone other than me.

## By the numbers

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats-light.svg" alt="Figures: 30 repositories (7 public), 8 stars, around 30 containers on one Raspberry Pi 5" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## Reason & evidence

Three tools with one thread — make it a little harder for noise to pass as fact.

### 🛡️ [dns-blocklist-builder](https://github.com/DanielEnki420/dns-blocklist-builder)

DNS blocklists against disinformation, propaganda and tracking — 11 categories,
6 languages, exported for Pi-hole, AdGuard, dnsmasq, Unbound and RPZ.
Runs entirely in the browser: no build step, no dependencies, works offline.

[**→ Live tool**](https://danielenki420.github.io/dns-blocklist-builder/) · `HTML` `JavaScript` `Shell` · MIT

### 🔍 [faktenchecker](https://github.com/DanielEnki420/faktenchecker)

An AI-assisted fact-checker that fits in a single HTML file — no backend, no build
step, no account. German and English.

[**→ Live tool**](https://danielenki420.github.io/faktenchecker/) · `HTML` · MIT

### <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/humanism-icon.png" width="34" height="34" align="absmiddle" alt=""> [humanism](https://github.com/DanielEnki420/humanism)

A trilingual (DE / EN / IT) landing page on secular humanism — reason, science, ethics.
Built with TanStack Start.

[**→ Live site**](https://humanism.lovable.app) · `TypeScript` `CSS`

## Growing

Two calculators, same idea, different medium. Nutrient schedules, pH/EC tracking and
a grow diary that never leaves the browser.

### 🌱 [dwc-grower-edition](https://github.com/DanielEnki420/dwc-grower-edition)

Deep-water-culture hydroponics: brand nutrient schedules, pH/EC/temperature/ORP
alerts, AI assistant, grow diary. Fully local — no cloud, no account.

[**→ Live tool**](https://danielenki420.github.io/dwc-grower-edition/) · `HTML` · MIT

### 🪴 [soil-coco-grower-edition](https://github.com/DanielEnki420/soil-coco-grower-edition)

The same for soil and coco — 25 brands, pH/EC tracking, grow diary, four languages.
Offline as well.

[**→ Live tool**](https://danielenki420.github.io/soil-coco-grower-edition/) · `HTML` · MIT

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## The homelab

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/the-stack-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/the-stack-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/the-stack-light.svg" alt="Art Deco line drawing: two seated cats flanking a Raspberry Pi 5" width="100%">
</picture>

<details>
<summary><b>~30 containers on one Raspberry Pi 5</b> — click to expand</summary>

<br>

| | |
|---|---|
| **Network & privacy** | Pi-hole · Unbound · Tailscale · CrowdSec · Fail2ban · Vaultwarden |
| **Home automation** | ioBroker (Tuya, Zigbee, Shelly) · custom Telegram alerting |
| **Observability** | Grafana · Prometheus · Uptime Kuma · Portainer · OLED status display |
| **Media & knowledge** | Immich · Calibre-Web · Kiwix |
| **Local AI** | Ollama · Open WebUI · LiteLLM |
| **Backup** | restic → off-site (Hetzner Storage Box), nightly |

Storage is NVMe, shared over Samba. Fan curve, watchdog and backup verification are
scripted — if something breaks at 3 a.m., the Pi tells me before I notice.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stack-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stack-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stack-light.svg" alt="Stack: Raspberry Pi 5, Linux, Docker, Pi-hole, Unbound, Grafana, Prometheus, ioBroker, Tailscale, restic; TypeScript, JavaScript, Node.js, Python, Bash" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## The test subjects

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/katzen-analyzer-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/katzen-analyzer-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/katzen-analyzer-light.svg" alt="katzen-analyzer: two cats as the input signal, next to a running frequency spectrum" width="100%">
</picture>

### 🐈 [katzen-analyzer](https://github.com/DanielEnki420/katzen-analyzer)

Real-time FFT spectral analysis of cat vocalizations, with AI-assisted interpretation
of the result. Browser-side, containerised.

[**→ Live tool**](https://danielenki420.github.io/katzen-analyzer/) · `HTML` `JavaScript` `Docker` · Apache-2.0

Every feature was tested on these two. They remain unconvinced.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


<sub>Every graphic on this page is a plain SVG generated by the scripts in this repo
(<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_banner.py"><code>banner</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_stats.py"><code>stats</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_illustration.py"><code>illustration</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_stack.py"><code>stack</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_footer.py"><code>footer</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_divider.py"><code>divider</code></a>),
each in a light and a dark variant from one shared palette in
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/theme.py"><code>theme.py</code></a>.
Nothing is loaded from a third party, so there is nothing to rate-limit and the whole
page follows your GitHub theme. The figures are a snapshot from the last run, not a live feed.</sub>
