from gwc.cli import build_parser


def test_status_summary_parses():
    parser = build_parser()
    args = parser.parse_args(["status-summary"])
    assert args.command == "status-summary"


def test_branch_name_parses():
    parser = build_parser()
    args = parser.parse_args(["branch-name", "42", "add-login"])
    assert args.command == "branch-name"
    assert args.issue_number == 42
    assert args.slug == "add-login"


def test_clean_merged_dry_run_default():
    parser = build_parser()
    args = parser.parse_args(["clean-merged"])
    assert args.apply is False
