# Security Policy

## Reporting a vulnerability
Please **do not** open public issues for suspected security problems.

Report privately to the maintainers with:
- affected file/path
- impact summary
- reproduction steps (if safe)
- suggested mitigation

If direct maintainer contact is not available, open a minimal issue requesting a private reporting channel without disclosing exploit details.

## Repository safety guidance
- Never commit credentials, tokens, private keys, or production data.
- Use local secret managers and environment variables outside Git.
- If accidental exposure is suspected, rotate credentials immediately and plan history purge.

## Disclosure process (high level)
1. Acknowledge report.
2. Triage severity and exposure scope.
3. Contain and patch.
4. Rotate impacted secrets.
5. Publish remediation notes when safe.

## AI-HPP Security Essentials (v4.1.1)

**1. Isolation**
Each agent runs separately.

**2. Minimum Permissions**
The agent receives only what it needs.

**3. Action Verification**
One agent confirms the other.

**4. No covert channels**
No secret messages between agents.

**5. Cryptography**
All important steps are signed.

The entire rule is on one line. Everyone understands it.
