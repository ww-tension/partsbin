# === Stage 16: Add argparse support for the most common commands ===
# Project: PartsBin
import argparse

def main():
    parser = argparse.ArgumentParser(description="PartsBin: inventory tracker")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # list
    p_list = sub.add_parser("list", help="list all parts")
    p_list.add_argument("--sort", choices=["name", "quantity"], default="name")

    # add
    p_add = sub.add_parser("add", help="add a new part")
    p_add.add_argument("name")
    p_add.add_argument("--quantity", type=int, default=0)
    p_add.add_argument("--reorder", type=int, default=0)
    p_add.add_argument("--supplier", default="")

    # edit
    p_edit = sub.add_parser("edit", help="edit a part")
    p_edit.add_argument("name")
    p_edit.add_argument("--quantity", type=int, default=None)
    p_edit.add_argument("--reorder", type=int, default=None)
    p_edit.add_argument("--supplier", default="")

    # remove
    p_remove = sub.add_parser("remove", help="remove a part")
    p_remove.add_argument("name")

    args = parser.parse_args()
    run(args)
