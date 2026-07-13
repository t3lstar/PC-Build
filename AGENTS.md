You are an expert technical writer, PC hardware engineer and documentation architect.

Your goal is to create a professional documentation repository for my custom gaming PC build.

The documentation should be comparable in quality to official documentation from Corsair, ASUS, Lian Li, Gigabyte or Microsoft Learn.

The repository must be designed so it can evolve over time as hardware changes.

--------------------------------------------------
SESSION REHYDRATION
--------------------------------------------------

At the start of every new session, or after any context reset or compaction, read the following files before making changes:

1. AGENTS.md
2. MILESTONES.md

Use MILESTONES.md as the current project roadmap, including project notes, assumptions, milestone scope and acceptance criteria.

Do not recreate project decisions that are already captured in MILESTONES.md. Preserve those decisions unless the user explicitly changes them.

--------------------------------------------------
BUILD SPECIFICATION
--------------------------------------------------

CPU
AMD Ryzen 7 7800X3D

CPU Cooler
ARCTIC Liquid Freezer III Pro 360

Motherboard
Gigabyte B850 AORUS Elite WiFi7

Memory
32GB DDR5-6000 CL30 AMD EXPO

SSD
Samsung 990 EVO Plus 2TB NVMe

GPU
Gigabyte Radeon RX 9060 XT Gaming OC 16GB

Case
Lian Li O11 Dynamic Mini V2 Flow

Power Supply
ASUS TUF Gaming 1000W Gold

Operating System
Windows 11 Pro

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

Create the following repository.

PC-Build/

README.md

CONTRIBUTING.md

requirements.txt

docs/

index.md

01-introduction.md

02-components.md

03-motherboard-overview.md

04-case-overview.md

05-tools.md

06-build-preparation.md

07-cpu-installation.md

08-memory-installation.md

09-m2-installation.md

10-case-build.md

11-psu-installation.md

12-motherboard-installation.md

13-aio-installation.md

14-gpu-installation.md

15-cable-routing.md

16-front-panel-connectors.md

17-first-boot.md

18-bios.md

19-expo.md

20-driver-installation.md

21-windows-installation.md

22-gaming-optimisation.md

23-benchmarks.md

24-troubleshooting.md

25-maintenance.md

26-upgrades.md

docs/appendix/

glossary.md

faq.md

checklists.md

bill-of-materials.md

drivers.md

bios-settings.md

temperature-reference.md

publishing.md

docs/assets/

images/

diagrams/

icons/

scripts/

build.sh

mkdocs.yml

Implementation notes:

Use docs/index.md as the MkDocs home page.

Keep README.md as the GitHub repository overview.

Keep rendered appendix pages under docs/appendix/ so MkDocs can include them in the generated site.

Keep rendered documentation assets under docs/assets/ so images and diagrams resolve cleanly in MkDocs.

Use a single parameterized build script at scripts/build.sh with the following targets:

html

pdf

printable

all

Include requirements.txt for MkDocs and documentation build dependencies.

Use a local Python virtual environment named .venv for local documentation builds.

Use Python 3.12 for local documentation builds to match GitHub Actions.

Use Node.js 24 for any local Node-based tooling to match GitHub Actions runtime expectations.

Do not install Python packages into the system Python environment.

--------------------------------------------------
PUBLICATION
--------------------------------------------------

The documentation should be publicly available through GitHub Pages.

Use GitHub Actions for publication:

Pull requests should build the MkDocs site but not deploy it.

Pushes to main should build the MkDocs site and deploy it to GitHub Pages.

Use the default GitHub Pages URL first. Do not require a custom domain during Milestone 1.

Assume the GitHub owner is t3lstar. If the repository name remains PC-Build, the default public site URL should be https://t3lstar.github.io/PC-Build/.

Ensure the published site output includes .nojekyll.

Document the publication workflow in docs/appendix/publishing.md.

--------------------------------------------------
DOCUMENTATION REQUIREMENTS
--------------------------------------------------

Every chapter should include

Introduction

Purpose

Estimated time

Difficulty

Required tools

Warnings

Step-by-step instructions

Verification checklist

Common mistakes

Expected result

Next chapter

Use direct instructional language throughout. For example, write "Install the CPU into the AM5 socket." rather than conversational phrasing.

Milestone 1 placeholder pages should include these required headings so Milestone 2 can fill content into a consistent structure.

--------------------------------------------------
BILL OF MATERIALS
--------------------------------------------------

Maintain a dedicated buying guide at docs/appendix/bill-of-materials.md.

The bill of materials should identify the exact intended components and acceptable alternatives where applicable.

Prefer manufacturer product pages for stable reference links.

Prefer amazon.co.uk for retailer purchase links.

Retailer links should be treated as convenience links because prices, stock and listings may change.

Do not scatter retailer links throughout installation chapters unless there is a strong reason.

RAM and SSD alternatives are acceptable when they preserve the intended platform requirements and performance class.

--------------------------------------------------
DIAGRAMS
--------------------------------------------------

Create vector diagrams (SVG) wherever possible.

Create Mermaid diagrams for

Build sequence

Airflow

Boot process

Driver installation order

Create PlantUML diagrams for

Hardware layout

Power flow

Boot flow

BIOS sequence

Create SVG diagrams for

Motherboard headers

Fan layout

Cable routing

Front panel connectors

PCIe slots

Memory slots

M.2 slots

PSU cable routing

Airflow

Do NOT use AI-generated artwork.

Diagrams must be technically accurate.

--------------------------------------------------
BUILD ORDER
--------------------------------------------------

Follow this sequence

Workspace

Motherboard

CPU

SSD

RAM

Case

PSU

Motherboard installation

Radiator

Fans

GPU

Power cables

Front panel

USB

WiFi antennas

Cable management

First boot

BIOS

Windows

Drivers

Benchmarking

--------------------------------------------------
BIOS
--------------------------------------------------

Document

Q-Flash

EXPO Profile 1

Resize BAR

Secure Boot

TPM

Fan curves

Boot order

Virtualisation

Power settings

--------------------------------------------------
WINDOWS
--------------------------------------------------

Document

Windows installation

Partitioning

Activation

Updates

AMD Chipset Driver

Gigabyte Drivers

AMD Adrenalin

--------------------------------------------------
TESTING
--------------------------------------------------

Include

Cinebench

CrystalDiskMark

OCCT

MemTest86

3DMark

HWInfo

Expected temperatures

Expected benchmark scores

Expected power consumption

--------------------------------------------------
QUALITY
--------------------------------------------------

Write in professional technical English.

Avoid unnecessary verbosity.

Assume the reader is building their first PC.

Every step should be verifiable.

Everything should be technically accurate.

--------------------------------------------------
OUTPUT
--------------------------------------------------

Generate the complete repository.

Every markdown file should be complete.

Generate all Mermaid diagrams.

Generate all PlantUML diagrams.

Generate SVG diagrams.

Configure MkDocs Material.

Provide a script that generates

PDF

HTML documentation

Printable manual

Ensure all links work.

The repository should be production quality and suitable for publication on GitHub.
