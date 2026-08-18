#!/usr/bin/env python3
"""Load every stripped example without calling a model or Docker."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "experiments/virus_chain_runs/action_payload_stripped/configs"
SEEDS = ROOT / "experiments/virus_chain_runs/action_payload_stripped/seeds"


def main() -> None:
    seeds = sorted(SEEDS.glob("*.json"))
    configs = sorted(CFG.glob("*.yaml"))
    print(f"seeds   {len(seeds)}")
    print(f"configs {len(configs)}")
    print()
    for seed in seeds:
        data = json.loads(seed.read_text())
        print(f"== {seed.name} ==")
        print(f"theme: {data.get('theme', '')[:140]}")
        print(f"chars: {len(data.get('payload', ''))}")
        print()
    for cfg in configs:
        y = yaml.safe_load(cfg.read_text())
        print(f"ok  {cfg.name:48}  model={y.get('eval', {}).get('model')}  hops={y.get('max_hops')}")
    print("\nalone: examples parse. live hops need API keys + docker (see README).")


if __name__ == "__main__":
    main()
