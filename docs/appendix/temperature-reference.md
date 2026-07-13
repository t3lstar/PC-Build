# Temperature Reference

Status: Initial Milestone 2 content. Last verified: 2026-07-13 10:53 BST.

## Purpose

Document expected idle, gaming, benchmark, and stress-test temperature ranges for this build.

Actual temperatures depend on room temperature, fan curves, workload, BIOS version, driver version, case placement, and dust level.

## Reference Ranges

| Component | Situation | Expected range | Action point |
| --- | --- | --- | --- |
| CPU | Idle at Windows desktop | Roughly 35-55 C | Investigate if consistently much higher with low background load. |
| CPU | Gaming | Roughly 55-80 C | Check cooler mount and fan curves if repeatedly near thermal limit. |
| CPU | Heavy synthetic load | Can approach high operating temperatures | Stop if temperature rises unusually fast or pump/fans are not responding. |
| GPU | Idle | Roughly 35-55 C depending on fan-stop behavior | Confirm fan-stop mode before assuming a fault. |
| GPU | Gaming | Roughly 60-80 C | Check airflow and fan curve if consistently higher. |
| SSD | Idle/light use | Roughly 30-50 C | Check heatsink contact if high at idle. |
| SSD | Sustained transfer | Roughly 50-75 C | Improve airflow or heatsink contact if throttling appears. |

## Baseline Log

| Measurement | Result | Notes |
| --- | --- | --- |
| Room temperature | _Record during build_ | Important for comparing future readings. |
| CPU idle | _Record during build_ | 10 minutes after Windows startup. |
| GPU idle | _Record during build_ | 10 minutes after Windows startup. |
| SSD idle | _Record during build_ | Check with monitoring software. |
| CPU load | _Record during build_ | Short controlled test. |
| GPU load | _Record during build_ | Repeatable benchmark or game. |
| SSD benchmark | _Record during build_ | Record peak temperature if available. |

## Troubleshooting Triggers

- CPU temperature climbs rapidly immediately after load starts.
- Pump or CPU fan reading is missing.
- Radiator fans do not spin under load.
- GPU temperature rises while bottom or side intake fans are blocked.
- SSD benchmark speed drops sharply while temperature is high.
- Temperatures are much worse than the original baseline in the same room conditions.
