import re

PROJECT_CODE_PATTERN = re.compile(r"^BV-\d{4}$")

def validate_get_engagement_status_args(args: dict) -> dict:
    project_code = args.get("project_code", "").strip()

    if not PROJECT_CODE_PATTERN.match(project_code):
        raise ValueError("Invalid project code format")

    return {"project_code": project_code}
