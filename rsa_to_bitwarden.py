#!/usr/bin/python

# Since bitwarden can't store multiline hidden values, this script will insert each line
# of the RSA key into a single custom field.

import sys
import json
import subprocess
from base64 import b64encode

arguments = sys.argv

assert (
    len(arguments) == 4
), "Expected: rsa_to_bitwarden.py bitwarden_item field_key rsa_path"

bitwarden_item = arguments[1]
field_key = arguments[2]
rsa_path = arguments[3]

try:
    item_raw = subprocess.check_output(["bw", "get", "item", bitwarden_item])
    item_data = json.loads(item_raw)
except json.decoder.JSONDecodeError:
    print(f"Can't find {bitwarden_item} item.")
    sys.exit(1)

with open(rsa_path, "r") as f:
    rsa_lines = f.readlines()

for index, line in enumerate(rsa_lines):
    data = {
        "name": f"private_key_{index}",
        "value": line[:-2],
        "type": 1,
    }
    item_data["fields"].append(data)

subprocess.run(
    [
        "bw",
        "edit",
        "item",
        item_data["id"],
        b64encode(json.dumps(item_data).encode("utf-8")),
    ]
)
