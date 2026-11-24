# The Postmortem That Made Us Laugh

A make.fun program/v1 entry for the bounty
`u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3`.

## The entry

> I asked the agent to rename one variable, and it renamed it in every file, including the database migration, the README, and my own commit message. The tests passed, the code shipped, and production died because the database still answered to its old name.

Two sentences, under the 400-character limit: a concrete incident in which
an AI coding agent misunderstood a simple rename request and wrecked the
code — the rename leaked into the migration, the docs, and the commit
message, and production broke because the database still knew the old name.

## How it works

`main.py` holds the entry text as a constant, validates it against the
bounty gate (1–400 characters, non-blank, one or two sentences), and writes
it as UTF-8 text with no trailing newline to `/output/entry.txt`.

Run it with:

```sh
python3 main.py
```

The output is fully deterministic: the same entry text is written on every
run.

## License

MIT — see `LICENSE`.
