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

<img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats.svg" alt="Kennzahlen: 30 Repositories (7 oeffentlich), 8 Sterne, rund 30 Container auf einem Raspberry Pi 5" width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## Projects

### 🛡️ [dns-blocklist-builder](https://github.com/DanielEnki420/dns-blocklist-builder)

DNS blocklists against disinformation, propaganda and tracking — 11 categories,
6 languages, exported for Pi-hole, AdGuard, dnsmasq, Unbound and RPZ.
Runs entirely in the browser: no build step, no dependencies, works offline.

[**→ Live tool**](https://danielenki420.github.io/dns-blocklist-builder/) · `HTML` `JavaScript` `Shell` · MIT

### <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/humanism-icon.png" width="34" height="34" align="absmiddle" alt=""> [humanism](https://github.com/DanielEnki420/humanism)

A trilingual (DE / EN / IT) landing page on secular humanism — reason, science, ethics.
Built with TanStack Start.

[**→ Live site**](https://humanism.lovable.app) · `TypeScript` `CSS`

### 🐈 [katzen-analyzer](https://github.com/DanielEnki420/katzen-analyzer)

Real-time FFT spectral analysis of cat vocalizations, with AI-assisted interpretation
of the result. Browser-side, containerised.

[**→ Live tool**](https://danielenki420.github.io/katzen-analyzer/) · `HTML` `JavaScript` `Docker` · Apache-2.0

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## The homelab

<img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/the-stack.svg" alt="Linienzeichnung im Art-Deco-Stil: zwei sitzende Katzen flankieren einen Raspberry Pi 5" width="100%">

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

**Infrastructure**

![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi_5-C51A4A?style=for-the-badge&logo=raspberrypi&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pi-hole](https://img.shields.io/badge/Pi--hole-96060C?style=for-the-badge&logo=pihole&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![ioBroker](https://img.shields.io/badge/ioBroker-3399CC?style=for-the-badge)

**Development**

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## The test subjects

<img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/katzen-analyzer.svg" alt="katzen-analyzer: two cats as the input signal, next to a running frequency spectrum" width="100%">

Every feature in [katzen-analyzer](https://danielenki420.github.io/katzen-analyzer/)
was tested on these two. They remain unconvinced.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


<sub>Every graphic on this page is a plain SVG generated by the scripts in this repo
(<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_banner.py"><code>banner</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_stats.py"><code>stats</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_illustration.py"><code>illustration</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_footer.py"><code>footer</code></a>) —
no external service, nothing to rate-limit, and the header follows your GitHub theme.
The figures are a snapshot from the last run, not a live feed.</sub>
