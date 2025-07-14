#!/usr/bin/python3

# SPDX-License-Identifier: LicenseRef-OQL-1.2
#
# This project is licensed under the Opinionated Queer License v1.2 (OQL-1.2)
#
# ## Full License Text
#
# # 🏳️‍🌈 Opinionated Queer License v1.2
#
# © Copyright [NamelessNanashi](<https://git.NamelessNanashi.dev/>)
#
# ## Permissions
#
# The creators of this Work (“The Licensor”) grant permission
# to any person, group or legal entity that doesn't violate the prohibitions below (“The User”),
# to do everything with this Work that would otherwise infringe their copyright or any patent claims,
# subject to the following conditions:
#
# ## Obligations
#
# The User must give appropriate credit to the Licensor,
# provide a copy of this license or a (clickable, if the medium allows) link to
# [oql.avris.it/license/v1.2](<https://oql.avris.it/license/v1.2>),
# and indicate whether and what kind of changes were made.
# The User may do so in any reasonable manner,
# but not in any way that suggests the Licensor endorses the User or their use.
#
# ## Prohibitions
#
# No one may use this Work for prejudiced or bigoted purposes, including but not limited to:
# racism, xenophobia, queerphobia, queer exclusionism, homophobia, transphobia, enbyphobia, misogyny.
#
# No one may use this Work to inflict or facilitate violence or abuse of human rights,
# as defined in either of the following documents:
# [Universal Declaration of Human Rights](<https://www.un.org/en/about-us/universal-declaration-of-human-right>),
# [European Convention on Human Rights](<https://prd-echr.coe.int/web/echr/european-convention-on-human-rights>)
# along with the rulings of the [European Court of Human Rights](<https://www.echr.coe.int/>).
#
# No law enforcement, carceral institutions, immigration enforcement entities, military entities or military contractors
# may use the Work for any reason. This also applies to any individuals employed by those entities.
#
# No business entity where the ratio of pay (salaried, freelance, stocks, or other benefits)
# between the highest and lowest individual in the entity is greater than 50 : 1
# may use the Work for any reason.
#
# No private business run for profit with more than a thousand employees
# may use the Work for any reason.
#
# Unless the User has made substantial changes to the Work,
# or uses it only as a part of a new work (eg. as a library, as a part of an anthology, etc.),
# they are prohibited from selling the Work.
# That prohibition includes processing the Work with machine learning models.
#
# ## Sanctions
#
# If the Licensor notifies the User that they have not complied with the rules of the license,
# they can keep their license by complying within 30 days after the notice.
# If they do not do so, their license ends immediately.
#
# ## Warranty
#
# This Work is provided “as is”, without warranty of any kind, express or implied.
# The Licensor will not be liable to anyone for any damages related to the Work or this license,
# under any kind of legal claim as far as the law allows.

import argparse


def calculate_tolerance(expected, measured):
    tolerances = {}
    for axis, e, m in zip(["X", "Y", "Z"], expected, measured):
        if e == 0:
            raise ValueError(f"Expected value for {axis}-axis cannot be zero.")
        if e < 0:
            raise ValueError(f"Expected value for {axis}-axis cannot be negative.")
        signed = ((m - e) / e) * 100
        absolute = abs(signed)
        tolerances[axis] = {"signed": signed, "absolute": absolute}
    return tolerances


def prompt_for_dimensions(label):
    print(f"\nEnter {label} dimensions (in mm):")
    x = float(input(" X: "))
    y = float(input(" Y: "))
    z = float(input(" Z: "))
    return (x, y, z)


def main():
    parser = argparse.ArgumentParser(
        description="PrintTolCalc CLI STANDALONE - Calculate 3D print dimensional tolerance.",
        epilog="""
Examples:
  PrintTolCalc
    → Interactive mode, will prompt for expected/measured dimensions.

  PrintTolCalc --expected 20 20 20 --measured 19.99 19.95 20.10
    → Command-line mode, pass dimensions directly.

All dimensions must be in millimeters (mm).
""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--version", action="version", version="PrintTolCalc.Standalone.py STANDALONE"
    )
    parser.add_argument(
        "--expected",
        type=float,
        nargs=3,
        metavar=("X", "Y", "Z"),
        help="Expected dimensions in mm (e.g. --expected 20 20 20)",
    )
    parser.add_argument(
        "--measured",
        type=float,
        nargs=3,
        metavar=("X", "Y", "Z"),
        help="Measured dimensions in mm (e.g. --measured 19.99 19.95 20.10)",
    )

    args = parser.parse_args()

    expected = args.expected if args.expected else prompt_for_dimensions("expected")
    measured = args.measured if args.measured else prompt_for_dimensions("measured")

    tolerances = calculate_tolerance(expected, measured)

    print("\n3D Print Tolerance Report:")
    print(f"Ideal X dimension (mm): {expected[0]:.2f}")
    print(f"Ideal Y dimension (mm): {expected[1]:.2f}")
    print(f"Ideal Z dimension (mm): {expected[2]:.2f}")
    print(f"Measured X dimension (mm): {measured[0]:.2f}")
    print(f"Measured Y dimension (mm): {measured[1]:.2f}")
    print(f"Measured Z dimension (mm): {measured[2]:.2f}")
    print("\nTolerance Results:")
    for axis in ["X", "Y", "Z"]:
        signed = tolerances[axis]["signed"]
        absolute = tolerances[axis]["absolute"]
        sign_prefix = "+" if signed > 0 else ""
        print(
            f"{axis}-axis: Signed = {sign_prefix}{signed:.3f}%, Absolute = {absolute:.3f}%"
        )


if __name__ == "__main__":
    main()
