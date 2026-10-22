import psycopg
from datetime import datetime

conn = psycopg.connect(
    "dbname=bluevivo user=app_user password=secret host=localhost port=5432"
)

with conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO engagement_memory (
                project_code,
                client_name,
                account_owner,
                compliance_profile,
                summary,
                created_at
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                "BV-2042",
                "Northwind Health",
                "M. Singh",
                "HIPAA-sensitive",
                "Client requires role-based AI knowledge access, audit logging, and regional data controls.",
                datetime.utcnow(),
            ),
        )
