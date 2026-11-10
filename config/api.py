from django.http import JsonResponse

from .db import get_db_connection


def health_check(request):
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                cursor.fetchone()

        return JsonResponse(
            {
                "success": True,
                "message": "Mani SaaS API is running",
                "database": "connected",
            }
        )

    except Exception as error:
        return JsonResponse(
            {
                "success": False,
                "message": "Database connection failed",
                "error": str(error),
            },
            status=500,
        )