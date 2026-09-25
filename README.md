<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-light.svg">
  <img alt="Daniel — self-hosting, home automation, network privacy" src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/banner-light.svg">
</picture>

> **Esse quam videri** — to be, rather than to seem.

I build small, self-contained tools and run them myself. Most of it lives on a
Raspberry Pi 5 in my living room — 36 containers, no cloud, backed up off-site.
What I publish is the part that is useful to someone other than me.

## Reason & evidence

Three tools with one thread — make it a little harder for something to pass as
what it is not.

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-faktenchecker-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-faktenchecker-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/faktenchecker">faktenchecker</a></h3>
  <p>An AI-assisted fact-checker that fits in a single HTML file — no backend, no build step, no account. German and English.</p>
  <p><a href="https://danielenki420.github.io/faktenchecker/"><b>&rarr; Live tool</b></a> · <code>HTML</code> · MIT</p>
</td>
</tr>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-correctness-checks-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-correctness-checks-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/correctness-checks">correctness-checks</a></h3>
  <p>Monitoring templates that ask whether a service still does its job, not
  whether it answers. A routine audit found three of mine dead for months behind
  green dashboards: Samba refusing every login, backups that were valid archives
  without the database, Portainer serving HTTP 200 with no Docker connection.
  Every check reports to a push monitor that turns red on its own when the report
  stops arriving.</p>
  <p><code>Shell</code> · MIT</p>
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
  <p>A trilingual (DE / EN / IT) landing page on secular humanism — reason, science, ethics. Built with TanStack Start.</p>
  <p><a href="https://humanism.lovable.app"><b>&rarr; Live site</b></a> · <code>TypeScript</code> <code>CSS</code></p>
</td>
</tr>
</table>

## Growing

Two nutrient calculators — one for deep water culture, one for soil and coco.
Each is a single HTML file that works offline; grow data stays in the browser, and
the optional AI assistant runs on your own Gemini key. In September 2026 I checked
every feeding plan in both against the manufacturer's own schedule and corrected
what did not match. Every plan now names its source, and a test in each repo
spot-checks the numbers against the charts.

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
  <p>Deep water culture. Doses in ml for your reservoir, week by week, for 13 nutrient brands — each from the maker's DWC or hydro schedule. Biobizz is listed but locked: its maker says the mixed solution must not stand for more than a day.</p>
  <p>Warnings for pH, EC, temperature and ORP, an EC top-up calculator, water-change reminder, harvest countdown and grow diary. Six languages.</p>
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
  <p>Soil, coco or a mix of both. 21 manufacturers in 31 plans — soil and coco kept apart wherever the maker publishes separate charts.</p>
  <p>pH and EC targets that follow the substrate, runoff tracking for salt build-up, feeding reminders for every first, second or third watering, charts and a grow diary. Four languages.</p>
  <p><a href="https://danielenki420.github.io/soil-coco-grower-edition/"><b>&rarr; Live tool</b></a> ·
  <a href="https://github.com/DanielEnki420/soil-coco-grower-edition/blob/main/tests/coco-belege.js">dose check</a> · <code>HTML</code> · MIT</p>
</td>
</tr>
</table>

## For the Mac

<table>
<tr>
<td width="104" align="center" valign="middle">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-apple-notes-dark.svg">
    <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/icon-apple-notes-light.svg" width="72" alt="">
  </picture>
</td>
<td valign="top">
  <h3><a href="https://github.com/DanielEnki420/apple-notes-to-pages">apple-notes-to-pages</a></h3>
  <p>Merges all your Apple Notes into one Pages document — clickable table of contents, formatting and images kept. One command, strictly read-only: only macOS built-ins and the Python standard library, nothing to install, no network access.</p>
  <p><code>Python</code> · MIT</p>
</td>
</tr>
</table>

## Olivera — built, running, for sale

My largest piece of work: a platform for leasing olive trees and selling the oil
directly. It is deployed and technically complete, and it has never been put into
operation — no paying customers, no revenue, Stripe in test mode and PayPal
implemented but currently disabled, the trees shown are sample data. I am not going
to run it; I am selling it. A buyer
switches the payment keys to live and takes over a finished system.

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
  <p><b>Frontend</b> — three Next.js 16 apps on the App Router (customer, admin,
  farmer portal), React 19, TypeScript in strict mode, Tailwind and shadcn/ui,
  Zustand and TanStack Query, five languages via next-intl.</p>
  <p><b>Backend</b> — four Hono services (API, oracle, notifications, indexer) on
  Node 20, PostgreSQL 16 with Drizzle ORM, Redis with BullMQ for queues.</p>
  <p><b>Payments and mail</b> — Stripe (test mode) and PayPal (implemented, currently
  disabled), Resend, Sentry.</p>
  <p><b>Certificates</b> — each lease gets an Ed25519 signature, publicly
  verifiable at <code>/verify</code> without a blockchain.</p>
  <p><b>Operations</b> — Vercel for the frontends, self-hosted Coolify on a
  Hetzner box for the services, nightly off-site backups, CI on every pull request.</p>
  <p>~86,500 lines of TypeScript across a pnpm/Turborepo monorepo.</p>
  <p><a href="https://www.oli-vera.eu"><b>&rarr; Live platform</b></a> ·
  <a href="https://app.littleexits.com/project/olivera-olive-tree-leasing-platform"><b>&rarr; For sale on Little Exits</b></a> ·
  <a href="https://www.prerevmarket.com/production/olivera"><b>&rarr; For sale on PreRevMarket</b></a></p>
  <p><code>TypeScript</code> <code>Next.js</code> <code>Hono</code>
  <code>PostgreSQL</code> · private repo</p>
</td>
</tr>
</table>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


## The homelab

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/homelab-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/homelab-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/homelab-light.svg" alt="Homelab on one Raspberry Pi 5: Art Deco line drawing of two cats flanking the board, with services grouped by function" width="100%">
</picture>

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
  <p>Real-time FFT spectral analysis of cat vocalizations, with AI-assisted interpretation of the result. Browser-side, containerised. An entertainment and learning project, and it says so up front: the classification is simple heuristics, not validated bioacoustics.</p>
  <p><a href="https://danielenki420.github.io/katzen-analyzer/"><b>&rarr; Live tool</b></a> · <code>HTML</code> <code>JavaScript</code> <code>Docker</code> · Apache-2.0</p>
</td>
</tr>
</table>

Every feature was tested on these two. They remain unconvinced.

## By the numbers

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/stats-light.svg" alt="Figures: 32 repositories (8 public), 4 stars, 36 containers on one Raspberry Pi 5" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg">
  <img src="https://raw.githubusercontent.com/DanielEnki420/DanielEnki420/main/assets/divider-light.svg" alt="" width="100%" height="24">
</picture>


<sub>Every graphic on this page is a plain SVG generated by the scripts in this repo
(<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_banner.py"><code>banner</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_stats.py"><code>stats</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_stack.py"><code>stack</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_icons.py"><code>icons</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_homelab.py"><code>homelab</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_footer.py"><code>footer</code></a>,
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/generate_divider.py"><code>divider</code></a>),
each in a light and a dark variant from one shared palette in
<a href="https://github.com/DanielEnki420/DanielEnki420/blob/main/theme.py"><code>theme.py</code></a>.
Nothing is loaded from a third party, so there is nothing to rate-limit and the whole
page follows your GitHub theme. The figures are a snapshot from the last run, not a live feed.</sub>
