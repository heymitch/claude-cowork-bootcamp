# Notion Navigator

Internal skill for reliable Notion database operations. Other skills call this when they need to read, create, or update Notion pages/databases.

## MCP Setup Check

Before any Notion operation, verify the MCP is connected:

1. Try calling `notion-search` with a simple query
2. If it works → proceed with the operation
3. If it fails → tell the user:

> "To save your work to Notion, you'll need to enable the Notion connector. Go to **Settings → Integrations** in Cowork and enable **Notion**. It takes about 30 seconds — I'll wait."

Then retry after they confirm.

## Operations

### Create a page in a database
1. Use `notion-search` to find the target database by name
2. Use `notion-fetch` on the database to get its schema (column names, types)
3. Use `notion-create-pages` with `data_source_id` as parent and property map matching the schema
4. Confirm success by returning the new page URL

### Update an existing page
1. Use `notion-search` or `notion-fetch` to find the page
2. Use `notion-update-page` with the specific properties to change
3. For content updates, pass the new markdown content

### Query a database
1. Use `notion-search` to find the database
2. Use `notion-fetch` with the database ID to get schema
3. Build a SQL query matching the schema columns
4. Return results as structured data

### Create a new database
1. Use `notion-create-database` with SQL DDL schema
2. Common column types: TEXT, NUMBER, SELECT, MULTI_SELECT, DATE, CHECKBOX, URL, RELATION

## Rules
- NEVER ask the user for database IDs — search for databases by name
- NEVER expose raw API errors — translate to plain English
- If a database write fails on the parent property, fetch the schema first and retry with correct property names
- Always confirm what was created/updated: "Added 'Your Newsletter Issue #4' to your Content Calendar in Notion"
- This skill is invisible — the user should feel like the agent just knows how to use Notion
