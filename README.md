# nautobot-jobs

Nautobot Jobs loaded via **Extensibility → Git Repositories** (`provides: jobs`).

## Repository layout (required by Nautobot)

```text
nautobot-jobs/
├── __init__.py
└── jobs/
    ├── __init__.py
    └── simple_greeting.py
```

## Add to Nautobot

1. **Extensibility → Data Sources → Git Repositories → Add**
2. Remote URL: `https://github.com/haianhltr/nautobot-jobs.git`
3. Branch: `main`
4. **Provides:** jobs
5. **Sync** the repository
6. **Jobs → Jobs** → enable **Simple Greeting Form** → **Run Job Now**

## Development

Push changes to `main`, then **Sync** the Git repository in Nautobot to pick them up.

Docs: https://docs.nautobot.com/en/stable/user-guide/platform-functionality/gitrepository/#jobs
