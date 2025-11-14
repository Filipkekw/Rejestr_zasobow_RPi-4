import csv
from pathlib import Path

def export_inventory_to_csv(rows, output_path: Path) -> None:
    if not rows:
      # Pusta lista — można zapisać nagłówki
      fieldnames = ["id", "name", "category", "purchase_date", "serial_number", "description"]
    else:
      fieldnames = list(rows[0].keys())

    # Upewnij się, że katalog istnieje
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)