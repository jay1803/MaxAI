# Public content policy

Everything in this repository will be public and is meant for other people to
copy. Content must describe a method, not a private setup.

## Never include

- The owner's or anyone else's name, handle, email, phone, location, photo or
  employer.
- Employer, product, customer, partner or vendor names; prices, revenue,
  metrics, roadmaps, launch dates or decisions from real work.
- Real workspace names, channel names, user IDs, issue keys, project names,
  database or page IDs, template IDs, internal URLs or hostnames.
- Credentials, tokens, signed URLs, local paths, machine names.
- Quotes from private conversations or tickets.
- Names that only make sense inside the private setup (personal nicknames for
  agents, private app names). Use the role instead: "the local agent", "the
  cloud assistant", "the relay".

## Allowed

- Public tool and product names used as examples of a category (Linear,
  Slack, Gmail, Notion, GitHub, Claude Code, ChatGPT).
- Generic numbers that describe the method (for example "3 working days",
  "at most 2 questions").
- Lessons learned, written as a rule plus a neutral example.

## How to generalize a real rule

1. Keep the rule and the reason.
2. Replace every proper noun with its role or a placeholder.
3. Remove dates and ticket references that point to the original event.
4. Check that a reader with a different employer and different tools can
   apply it.

`scripts/check_public.py` enforces part of this. Passing the check does not
prove a page is clean; the writer still reviews each line.
