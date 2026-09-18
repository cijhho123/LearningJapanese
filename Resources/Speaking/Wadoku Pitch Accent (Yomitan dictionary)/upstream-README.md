# Wadoku Pitch Accent Dictionary for Yomitan

A pitch accent dictionary for [Yomitan](https://yomitan.wiki) based on the XML-Dump from the Wadoku Jiten/和独辞典 (<https://www.wadoku.de>). Download prebuilt dictionaries from Releases.

## Source Data

Using the XML-Dump from [the Wadoku downloads page](https://www.wadoku.de/wiki/display/WAD/Downloads+und+Links), we extract the accent positions for entries with `<accent>` nodes, and devoice positions from `<hatsuon>` nodes, and format according to Yomitan's [term meta bank v3 schema](https://github.com/yomidevs/yomitan/blob/master/ext/data/schemas/dictionary-term-meta-bank-v3-schema.json).

## Usage

```text
usage: build_dictionary.py [-h] [-o OUTPUT_DIR] xml_path minor_revision

Convert Wadoku XML pitch accent data to a Yomitan dictionary zip.

positional arguments:
  xml_path              Path to the wadoku XML file.
  minor_revision        The minor version for the dictionary, e.g. 01

options:
  -h, --help            show this help message and exit
  -o, --output-dir OUTPUT_DIR
                        Output directory (default: ./dist).
```

## Licensing

- Use and distribution of the produced dictionary must follow the terms of the **WaDoku-Datei-LIZENZ** (see the LICENSE file).
- The build_dictionary.py script and this README are released under **CC0 1.0 Universal** (see the LICENSE.CC0 file).
