# DevHQ Dashboard Plan

## Overview

The DevHQ Dashboard is a separate admin application for managing users, sending emails, and viewing app statistics. It consists of:

- **Frontend**: Next.js application
- **Backend**: FastAPI application
- **Database**: PostgreSQL (separate from main app, but can access main app data via API)

## Architecture

```
[Dashboard Frontend (Next.js)] <--> [Dashboard Backend (FastAPI)] <--> [Main DevHQ Backend (FastAPI)]
                                      |
                                      v
                                 [PostgreSQL DB]
```

- Dashboard backend communicates with main DevHQ backend via API calls for user data, stats, etc.
- Dashboard has its own database for admin-specific data (e.g., admin users, email logs).

## Features

### Platform Overview (Hero Metrics)
- Total Users - Total registered users on the platform
- Active Users (Last 30 Days) - Users who logged in recently
- Total Projects Created - Lifetime project count across all users
- Active Projects - Currently in-progress projects platform-wide
- Platform Revenue (MRR) - Monthly Recurring Revenue from subscriptions
- Total Transactions - Payment volume processed through Paystack

### User Analytics
- User Growth Chart - New signups over time (daily/weekly/monthly)
- User Retention Rate - % of users who return after signup
- User Segmentation: OAuth vs Email/Password users, Users by provider (Google, GitHub, GitLab, Bitbucket), Active vs Inactive Users
- User Churn Rate - Users who stopped using the platform
- Geographic Distribution - Users by timezone/location
- Average Projects per User - Engagement depth metric

### Subscription & Revenue Analytics
- Subscription Breakdown: Free tier, Pro tier, Enterprise tier, Trial users
- Subscription Status Distribution (Active, Cancelled, Expired)
- Revenue Metrics: Total MRR, ARR, ARPU, LTV
- Conversion Funnel: Free → Pro, Pro → Enterprise, Trial → Paid conversion rates
- Churn Analysis: Subscription cancellations, reasons, revenue churn rate
- Payment Method Distribution (Paystack vs Manual)
- Paystack Fee Waived Stats - Revenue impact of waived fees for paid users

### Platform Usage Metrics
- Projects Created - Daily/weekly/monthly trends
- Contracts Generated - Total contracts sent to clients
- Contract Signature Rate - % of contracts signed
- Time Entries Logged - Total hours tracked platform-wide
- Git Commits Processed - Automation usage metrics
- Client Portals Created - Portal generation frequency
- Deliverables Completed - Platform-wide deliverable completion
- Invoices Generated - Total invoicing activity
- CLI Downloads - CLI adoption rate
- CLI Active Installations - Users actively using CLI

### Feature Adoption
- Git Integration Usage: Users with GitHub/GitLab/Bitbucket connected, repositories tracked, commits processed
- Time Tracker Integration: Toggl, Harvest integrations
- Automation Features: Auto-verified deliverables, auto-pause events, auto-replenish usage
- Client Portal Engagement: Active sessions, views, session duration

### Financial Dashboard
- Platform Revenue Breakdown: Subscription revenue, transaction fees, Paystack fees
- Payment Processing: Total volume, successful/failed transactions, average value
- Invoice Analytics: Total created, paid/unpaid, average value, pending verification
- Revenue by Plan Type - Pie chart

### System Health & Performance
- API Performance: Response time, error rate, most used endpoints
- Database Metrics: Total records, size, query performance
- NATS/WebSocket Activity: Active connections, events published, latency
- CLI Version Distribution
- Failed Webhooks
- Background Job Status

### User Behavior Insights
- Most Active Users - Top users by project count, hours logged
- Power Users - Users with most integrations, deliverables
- Feature Usage Heatmap
- User Journey Analytics: Time from signup to first project, etc.
- Drop-off Points

### Content & Templates
- Template Usage: Popular templates, system vs custom
- Contract Templates: Most used, custom vs default
- Integration Popularity

### Support & Issues
- Error Logs
- Failed Payments
- Subscription Issues
- User Feedback
- Support Tickets

### Growth Metrics
- Viral Coefficient
- Activation Rate
- Engagement Score
- Feature Adoption Timeline
- Cohort Analysis

### Alerts & Monitoring
- Critical Alerts: Payment gateway downtime, DB issues, high errors, payment failures
- Business Alerts: Churn spike, revenue drop, traffic increase
- Security Alerts: Failed logins, suspicious usage, OAuth failures

### Admin Actions Panel
- User Management: View/edit accounts, adjust subscriptions, impersonate, ban/suspend
- Subscription Management: Override limits, grant trials, waive fees
- System Configuration: Feature flags, maintenance mode, rate limits
- Data Export: User data, revenue reports, usage analytics

### Real-time Activity Feed
- New signups, subscription changes, large payments, high-value projects, errors, CLI updates

### Legacy Features (from initial plan)
1. **User Management** (enhanced with above)
2. **Email Sending**:
   - Send emails to individual users or groups
   - Email templates
   - Email history/logs
3. **Authentication**:
   - Admin login/logout
   - JWT-based auth

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: Next.js, React, Tailwind CSS (assuming)
- **Email**: Brevo API
- **Auth**: JWT

## API Endpoints (Dashboard Backend)

- `GET /users` - List users (proxy to main backend)
- `POST /users` - Create user (proxy)
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user
- `POST /emails/send` - Send email
- `GET /stats` - Get stats (aggregate from main backend)
- `POST /auth/login` - Admin login

## Database Models

- AdminUser: id, username, password_hash, role
- EmailLog: id, recipient, subject, sent_at, status

## Frontend Pages

- `/login` - Admin login
- `/dashboard` - Main dashboard with stats
- `/users` - User management
- `/emails` - Send emails, view history

## Security Considerations

- Secure API communication with main backend (API keys, JWT)
- Admin authentication
- Input validation
- CORS settings

## Deployment

- Separate deployment from main app
- Environment variables for configs (DB URL, main backend URL, email API key)

## Next Steps

- Create starter files for backend and frontend
- Implement basic authentication
- Set up database
- Integrate with main backend APIs
