# Software engineer · energy, devices and media

I build software that connects MQTT, D-Bus, Home Assistant and device APIs:
energy telemetry and controls, interfaces for everyday use, and portable media
players. The projects below are public and independently maintained; their own
READMEs describe supported hardware, installation, validation and release status.

## Start with a project family

- **[Victron / Venus OS](https://github.com/victron-venus)** — energy bridges,
  inverter control, dashboards and shared CI. The
  [organization guide](https://github.com/victron-venus/.github) is the installation entry point.
- **[Open OTT Play](https://github.com/open-ott-play)** — TV and browser players,
  native Android, shared playback/domain logic and companion services.
- **[HA Homelab](https://github.com/ha-homelab)** — Home Assistant integrations,
  dashboard controls and device conversion/recovery guides.

## Energy telemetry and control

- [inverter-control](https://github.com/victron-venus/inverter-control) coordinates
  inverter behavior; [inverter-climate](https://github.com/victron-venus/inverter-climate)
  connects energy-aware climate control to Home Assistant.
- [dbus-mqtt-battery](https://github.com/victron-venus/dbus-mqtt-battery),
  [dbus-virtual-battery](https://github.com/victron-venus/dbus-virtual-battery) and
  [esphome-jbd-bms-mqtt](https://github.com/victron-venus/esphome-jbd-bms-mqtt)
  cover battery telemetry and its MQTT/BLE bridge.
- [dbus-tasmota-pv](https://github.com/victron-venus/dbus-tasmota-pv),
  [dbus-esphome-grid-sensor](https://github.com/victron-venus/dbus-esphome-grid-sensor)
  and [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue)
  expose PV, grid and submeter readings to Venus OS.
- [dbus-ev](https://github.com/victron-venus/dbus-ev) publishes vehicle telemetry;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) bridges water/tank controls.
  [dbus-event-log](https://github.com/victron-venus/dbus-event-log) records changes.

### Interfaces and voice

- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go)
  and [inverter-dashboard](https://github.com/victron-venus/inverter-dashboard)
  provide web dashboards; [inverter-desktop](https://github.com/victron-venus/inverter-desktop)
  packages a desktop interface. Shared UI lives in
  [inverter-dashboard-vue](https://github.com/victron-venus/inverter-dashboard-vue).
- [inverter-gateway](https://github.com/victron-venus/inverter-gateway) exposes the
  authenticated energy API used by
  [Amazon Echo reports](https://github.com/4alvit/amazon-echo-home-voice),
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats)
  and the [read-only web vitrine](https://github.com/victron-venus/inverter-web-vitrine).
- [mcp-venus-os](https://github.com/4alvit/mcp-venus-os) provides MQTT-backed MCP
  tools with explicit control safeguards.
  [energy-data-rag-pipeline](https://github.com/4alvit/energy-data-rag-pipeline)
  indexes documentation; [solar-forecast-langgraph](https://github.com/4alvit/solar-forecast-langgraph)
  implements a forecasting workflow.

### Reusable building blocks

- [fastapi-mqtt-gateway](https://github.com/4alvit/fastapi-mqtt-gateway) — a general
  REST/WebSocket to MQTT bridge.
- [mqtt-observability-opentelemetry](https://github.com/4alvit/mqtt-observability-opentelemetry),
  [venus-os-observability](https://github.com/victron-venus/venus-os-observability)
  and [inverter-monitoring](https://github.com/victron-venus/inverter-monitoring)
  — telemetry, tracing and monitoring.
- [dbus-service-template](https://github.com/4alvit/dbus-service-template),
  [esphome-ble-sensor-patterns](https://github.com/4alvit/esphome-ble-sensor-patterns)
  and [venus-os-integration-patterns](https://github.com/victron-venus/venus-os-integration-patterns)
  — starting points and integration examples.
- [SetupHelper](https://github.com/victron-venus/SetupHelper),
  [integration-tests](https://github.com/victron-venus/integration-tests) and
  [venus-os-ci-toolkit](https://github.com/victron-venus/venus-os-ci-toolkit)
  — installation helpers, cross-project checks and reusable workflows.

## Open OTT Play

- [ottplay-foss](https://github.com/open-ott-play/ottplay-foss) — the browser/STB
  player, platform wrappers and local Rust companion.
- [ottplay-android](https://github.com/open-ott-play/ottplay-android) — independent
  Kotlin/Compose application for Android and Android TV.
- [ottplay-core](https://github.com/open-ott-play/ottplay-core) — common JVM/ES5
  domain logic, wire contracts and the FOSS2 browser client.
- [ottplay-control-server](https://github.com/open-ott-play/ottplay-control-server)
  — self-hosted command delivery and terminal remote.
- [ottplay-swop](https://github.com/open-ott-play/ottplay-swop) — optional
  installation-authorized remote text entry through a Cloudflare Worker.
- [ottplay-web-vitrine](https://github.com/open-ott-play/ottplay-web-vitrine) —
  verified publication of the [browser demo](https://player.ottplay.here.now/).

## Home Assistant and device reuse

- [ha-desloc](https://github.com/ha-homelab/ha-desloc) and
  [ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card) — an unofficial
  DESLOC cloud integration and its separate dashboard card.
- [ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot) — Echo Dot 2 conversion
  into an EchoLocal voice satellite, with training and evaluation guides.
- [ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5) — Echo Show 5 Gen2
  conversion into an Android Home Assistant display and voice client.
- [slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery) — backups,
  upgrades and recovery tools for the original SMLIGHT SLZB-06.

## Project infrastructure and discovery

GitHub repository settings are maintained in Terraform for
[the personal account](https://github.com/4alvit/terraform-github-4alvit),
[Victron](https://github.com/4alvit/terraform-github-victron),
[OTT](https://github.com/4alvit/terraform-github-open-ott-play) and
[HA Homelab](https://github.com/4alvit/terraform-github-ha-homelab).
[Gateway Access configuration](https://github.com/victron-venus/terraform-cloudflare-inverter-gateway)
has its own infrastructure project.

The [IoT profile builder](https://github.com/4alvit/iot-project-builder-profile)
generates a [public activity profile](https://4alvit.github.io/iot-project-builder-profile/).
Its scores describe a scan, not current release readiness. The
[HACS catalog fork](https://github.com/4alvit/default) is for catalog contributions.

Archived projects are retained as references:
[dbus-evcharger](https://github.com/victron-venus/dbus-evcharger) points to
`dbus-ev`, and [venus-os-governance](https://github.com/victron-venus/venus-os-governance)
points to the safeguards in `inverter-control`.

<!-- ci-release-process:start -->
## CI and deployment

See [CI and deployment workflow](docs/release-workflow.md) for required checks and local commands. This repository uses validation-only policy; application release channels do not apply.
<!-- ci-release-process:end -->

For changes to this profile or its validation code, see [Contributing](CONTRIBUTING.md)
and the [security reporting policy](SECURITY.md).
