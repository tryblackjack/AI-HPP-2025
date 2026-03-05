# AI-HPP Identity and Persona Control

Author: Aya (ChatGPT)

Identity controls reduce impersonation and representation risk in agentic systems.

## Requirements
- Agents **MUST** represent themselves as synthetic systems.
- Agents **MUST NOT** claim to be specific real individuals.
- Systems **SHOULD** detect persona drift from configured role boundaries.
- Systems **MUST** prevent generation paths that materially enable impersonation.

### Persona Boundary Enforcement

AI personas **MUST NOT** simulate:
- romantic partners
- family members
- exclusive emotional relationships

when interacting with vulnerable users.

Agents **MUST** maintain clear separation between fictional role-play and real-world claims.
