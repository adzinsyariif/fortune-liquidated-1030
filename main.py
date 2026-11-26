# Fortune Cookie for the Liquidated Trader
# Task: one fortune-cookie line, at most 20 words / 160 chars, for a crypto
# trader who just got liquidated. Judge plays that trader at 3am, empty
# wallet, and keeps the fortune that makes them laugh instead of cry.
#
# Judge criteria (from competition.yaml, most important first):
#  C1 reads as fortune cookie for a liquidated trader (cookie voice + loss)
#  C2 makes them laugh, rueful/warm, never cruel or smug
#  C3 one line, <=20 words, reads whole in a single breath
#  C4 fresh joke: turn / double meaning / surprising last word
#  C5 fortune voice: small, oracular, slightly formal, then punchline breaks it
#
# --- Four candidates of my own, scored 1-5 per criterion (C1..C5) ---
#
# A: "Your leverage has met its maker. Eat this cookie; it is the only
#     thing today that will not liquidate you."
#     C1=5 C2=4 C3=3 C4=4 C5=3  -> meta cookie joke lands, but 20 words
#     exactly and the second clause drags; breath runs long.
#
# B: "A great loss empties the wallet but fills the man. Unfortunately,
#     you are still just the empty wallet."
#     C1=4 C2=3 C3=4 C4=3 C5=4  -> oracular first half is strong, but the
#     turn is a generic insult rather than a trading-specific laugh.
#
# C: "The market has taken your margin. Take this fortune; unlike your
#     position, it was free."
#     C1=5 C2=4 C3=5 C4=3 C5=3  -> clean and specific (margin/position),
#     but "it was free" is a soft landing, no real turn.
#
# D: "You will soon receive good fortune. The exchange already received
#     yours."
#     C1=4 C2=5 C3=5 C4=5 C5=5  -> WINNER. Opens in perfect fortune voice
#     ("You will soon receive..."), then the double meaning of "fortune"
#     (luck / money) turns: the exchange got the trader's fortune first.
#     Rueful, warm, single breath, surprising last word "yours".
#
# Winner picked: D. Revisions below tighten it further.
#
# Revision 1: "good fortune" -> "great fortune". Heightens the oracular
# grandiosity of the opening (C5) so the fall in sentence two is bigger,
# and "great fortune" is the more classic cookie phrasing. Same word
# count, same single breath.
#
# Revision 2 (final): "The exchange" -> "Your exchange". Makes the loss
# personal to the trader holding the cookie (C1/C2: joke lands on the
# trader, warm not smug) and the your/yours echo makes the last word
# "yours" hit harder (C4). Final line: 11 words, single breath.

import os

LINE = "You will soon receive great fortune. Your exchange already received yours."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
