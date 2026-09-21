import json
import sys
from pathlib import Path


def load_events(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def filter_critical(events):
    return [e for e in events if e["severity"] == "critical"]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "events.json"
    events = load_events(path)
    critical = filter_critical(events)
    for e in critical:
        print(f"critical: {e['event']}")
    print(f"критичных {len(critical)}")


if __name__ == "__main__":
    main()
