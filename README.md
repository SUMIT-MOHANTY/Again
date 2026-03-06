# Placeholder Credentials & Mock Services

## Why placeholders exist
The repository is designed to run out‑of‑the‑box without requiring external services.  Placeholder values for PostgreSQL and Azure OpenAI allow developers to start the API immediately, using in‑memory mocks instead of real connections.

## Replacing placeholders with real values
1. Copy `.env.example` to `.env`.
2. Replace `POSTGRES_URI` with your PostgreSQL connection string.
3. Replace `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` with the credentials from your Azure OpenAI resource.
4. Restart the application - the mocks will be disabled and real services will be used.

## Automatic fallback to mocks
If any of the three environment variables contain the placeholder strings (`postgres://user:password@localhost/db`, `your-key-here`, `https://your-openai-instance.openai.azure.com/`), the `settings.use_mock` flag becomes `True`.  The code paths in `services/azure_openai.py` and `db/session.py` will instantiate the mock classes, preventing real network or database calls.

## Troubleshooting

- **Application still tries to connect to the real DB**: Ensure *all* three variables are either unset or contain the exact placeholder values.  Even a single correct value disables the mock.
- **Environment variables not loading**: Verify that the `.env` file is present at the project root and that you have installed `python-dotenv` (or that your deployment platform loads env vars correctly).
- **Unexpected errors from mock services**: The mocks are very lightweight; they only implement the methods used in the current code base.  Extending them may be required for new features.

