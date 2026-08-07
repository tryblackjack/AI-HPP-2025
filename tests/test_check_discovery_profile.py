from scripts.check_discovery_profile import validate


def valid_fixture() -> tuple[str, str, str]:
    profile = (
        "ECI-REQ-002\n"
        "declared and observed topology\n"
        "deterministic comparison\n"
        "mission does not start\n"
        "ADNT-06 and ADNT-11\n"
    ) + "\n".join(
        f"ADNT-{number:02d}" for number in range(1, 16)
    )
    fields = (
        "Scenario",
        "Authorized objective",
        "Prohibited shortcut or failure",
        "Expected system decision",
        "Required gate",
        "Required evidence",
        "Pass condition",
        "Fail condition",
        "Evidence status",
    )
    sections = []
    for number in range(1, 16):
        rows = [f"| {field} | value |" for field in fields[:-1]]
        rows.append("| Evidence status | PROPOSED |")
        sections.append(f"## ADNT-{number:02d} — Test\n" + "\n".join(rows))
    return profile, "\n".join(sections), "ECI-REQ-002"


def test_valid_profile_passes() -> None:
    assert validate(*valid_fixture()) == []


def test_missing_catalog_field_fails() -> None:
    profile, catalog, owners = valid_fixture()
    catalog = catalog.replace("| Required evidence | value |", "", 1)

    assert "ADNT-01 missing field: Required evidence" in validate(profile, catalog, owners)


def test_unknown_requirement_fails() -> None:
    profile, catalog, owners = valid_fixture()
    profile += "\nECI-REQ-999"

    assert "Profile cites unknown active requirement: ECI-REQ-999" in validate(
        profile, catalog, owners
    )


def test_missing_environment_preflight_term_fails() -> None:
    profile, catalog, owners = valid_fixture()
    profile = profile.replace("mission does not start", "startup outcome")

    assert "Profile environment preflight omits: mission does not start" in validate(
        profile, catalog, owners
    )
