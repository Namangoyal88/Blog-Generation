# Blog-Generation

An agentic blog content generation system built with **LangGraph** and **FastAPI**. It uses graph-based workflows to generate blog content on a given topic, with optional automatic translation into a target language, powered by pluggable LLM backends.

## Features

- **Agentic workflow orchestration** — Content generation is modeled as a LangGraph state graph, with conditional routing based on the input request.
- **Topic-based generation** — Generate a blog post from a topic alone.
- **Language translation** — Optionally translate the generated blog into a specified language via an extended graph workflow.
- **Multi-LLM support** — Swap between LLM providers at runtime:
  - Groq
  - Google Gemini
  - Nemotron
- **REST API** — Exposes a simple FastAPI endpoint for integration with other services or frontends.

## Tech Stack

- Python
- FastAPI
- LangGraph / LangChain
- Groq, Google Gemini, Nemotron (LLM providers)
- Uvicorn

## Project Structure

```
Blog-Generation/
├── app.py                 # FastAPI application and API endpoint
├── main.py                # Entry point
├── src/
│   ├── graphs/             # LangGraph graph builder and workflow logic
│   └── llms/                # LLM provider wrappers (Groq, Gemini, Nemotron)
├── langgraph.json          # LangGraph configuration
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

## Getting Started

### Prerequisites

- Python 3.10+
- API keys for your chosen LLM provider(s) (Groq / Google / Nemotron) and LangChain

### Installation

```bash
git clone https://github.com/Namangoyal88/Blog-Generation.git
cd Blog-Generation
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

### Running the App

```bash
python app.py
```

The server starts at `http://0.0.0.0:8000`.

## API Usage

### `POST /blog`

Generates a blog post, optionally translated into a target language.

**Request body:**

```json
{
  "topic": "The Future of Artificial Intelligence",
  "language": "hindi"
}
```

- `topic` (required) — The subject to generate the blog about.
- `language` (optional) — If provided, the generated blog is translated into this language. If omitted, the blog is returned in its original generated form.

**Response:**

```json
{
  "data": {
    "topic": "...",
    "content": "...",
    "translated_content": "..."
  }
}
```

## How It Works

1. A request hits the `/blog` endpoint with a `topic` (and optionally a `language`).
2. A `GraphBuilder` constructs a LangGraph workflow — either a `topic` graph or a `topic + language` graph, depending on the request.
3. The graph is invoked with the input state, running through generation (and translation, if applicable) nodes.
4. The final state, containing the generated content, is returned as the API response.

## License

This project currently has no license specified.
