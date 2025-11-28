from fastapi import APIRouter, Depends
from .auth import get_current_user

router = APIRouter()

@router.get("/")
async def get_stats(current_user: str = Depends(get_current_user)):
    # In production, fetch from main DevHQ backend and aggregate
    return {
        "platform_overview": {
            "total_users": 1250,
            "active_users_last_30_days": 890,
            "total_projects_created": 3450,
            "active_projects": 1200,
            "platform_revenue_mrr": 45000,
            "total_transactions": 5600
        },
        "user_analytics": {
            "user_growth_chart": [],  # Mock data
            "user_retention_rate": 0.75,
            "user_segmentation": {
                "oauth_users": 600,
                "email_password_users": 650
            },
            "user_churn_rate": 0.05,
            "geographic_distribution": {},  # Mock
            "average_projects_per_user": 2.8
        },
        "subscription_revenue": {
            "subscription_breakdown": {
                "free": 400,
                "pro": 600,
                "enterprise": 150,
                "trial": 100
            },
            "revenue_metrics": {
                "total_mrr": 45000,
                "arr": 540000,
                "arpu": 36,
                "ltv": 180
            },
            "conversion_funnel": {
                "free_to_pro": 0.15,
                "pro_to_enterprise": 0.08,
                "trial_to_paid": 0.25
            }
        },
        "platform_usage": {
            "projects_created_trend": [],  # Mock
            "contracts_generated": 1200,
            "contract_signature_rate": 0.85,
            "time_entries_logged": 15000,
            "git_commits_processed": 25000,
            "client_portals_created": 800,
            "deliverables_completed": 2200,
            "invoices_generated": 950,
            "cli_downloads": 3000,
            "cli_active_installations": 1800
        },
        # Add more sections as per plan
        "system_health": {
            "api_response_time": 0.2,
            "error_rate": 0.01,
            "database_records": 50000
        }
    }