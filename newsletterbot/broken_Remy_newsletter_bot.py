{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GUnquPUgUTex",
        "outputId": "fc35358a-8b07-43f3-a261-30129183fa72"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: google-genai in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (1.29.0)\n",
            "Collecting google-genai\n",
            "  Downloading google_genai-1.43.0-py3-none-any.whl.metadata (45 kB)\n",
            "Collecting arxiv\n",
            "  Downloading arxiv-2.2.0-py3-none-any.whl.metadata (6.3 kB)\n",
            "Requirement already satisfied: anyio<5.0.0,>=4.8.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (4.10.0)\n",
            "Requirement already satisfied: google-auth<3.0.0,>=2.14.1 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (2.40.3)\n",
            "Requirement already satisfied: httpx<1.0.0,>=0.28.1 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (0.28.1)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.0.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (2.11.7)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.28.1 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (2.32.4)\n",
            "Requirement already satisfied: tenacity<9.2.0,>=8.2.3 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (9.1.2)\n",
            "Requirement already satisfied: websockets<15.1.0,>=13.0.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (15.0.1)\n",
            "Requirement already satisfied: typing-extensions<5.0.0,>=4.11.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-genai) (4.14.1)\n",
            "Requirement already satisfied: idna>=2.8 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from anyio<5.0.0,>=4.8.0->google-genai) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from anyio<5.0.0,>=4.8.0->google-genai) (1.3.1)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (5.5.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (0.4.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (4.9.1)\n",
            "Requirement already satisfied: certifi in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from httpx<1.0.0,>=0.28.1->google-genai) (2025.8.3)\n",
            "Requirement already satisfied: httpcore==1.* in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from httpx<1.0.0,>=0.28.1->google-genai) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from httpcore==1.*->httpx<1.0.0,>=0.28.1->google-genai) (0.16.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (2.33.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (0.4.1)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from requests<3.0.0,>=2.28.1->google-genai) (3.4.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from requests<3.0.0,>=2.28.1->google-genai) (2.5.0)\n",
            "Requirement already satisfied: pyasn1>=0.1.3 in /Users/remyw/.pyenv/versions/agents/lib/python3.13/site-packages (from rsa<5,>=3.1.4->google-auth<3.0.0,>=2.14.1->google-genai) (0.6.1)\n",
            "Collecting feedparser~=6.0.10 (from arxiv)\n",
            "  Downloading feedparser-6.0.12-py3-none-any.whl.metadata (2.7 kB)\n",
            "Collecting sgmllib3k (from feedparser~=6.0.10->arxiv)\n",
            "  Downloading sgmllib3k-1.0.0.tar.gz (5.8 kB)\n",
            "  Installing build dependencies ... \u001b[?25ldone\n",
            "\u001b[?25h  Getting requirements to build wheel ... \u001b[?25ldone\n",
            "\u001b[?25h  Preparing metadata (pyproject.toml) ... \u001b[?25ldone\n",
            "\u001b[?25hDownloading google_genai-1.43.0-py3-none-any.whl (236 kB)\n",
            "Downloading arxiv-2.2.0-py3-none-any.whl (11 kB)\n",
            "Downloading feedparser-6.0.12-py3-none-any.whl (81 kB)\n",
            "Building wheels for collected packages: sgmllib3k\n",
            "  Building wheel for sgmllib3k (pyproject.toml) ... \u001b[?25ldone\n",
            "\u001b[?25h  Created wheel for sgmllib3k: filename=sgmllib3k-1.0.0-py3-none-any.whl size=6089 sha256=a3d491ed5b8e07f31601bed6f3151c18206745a6f43888d41c14bef5b06f598c\n",
            "  Stored in directory: /Users/remyw/Library/Caches/pip/wheels/3d/4d/ef/37cdccc18d6fd7e0dd7817dcdf9146d4d6789c32a227a28134\n",
            "Successfully built sgmllib3k\n",
            "Installing collected packages: sgmllib3k, feedparser, arxiv, google-genai\n",
            "\u001b[2K  Attempting uninstall: google-genai\n",
            "\u001b[2K    Found existing installation: google-genai 1.29.0\n",
            "\u001b[2K    Uninstalling google-genai-1.29.0:\n",
            "\u001b[2K      Successfully uninstalled google-genai-1.29.0\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4/4\u001b[0m [google-genai][0m [google-genai]\n",
            "\u001b[1A\u001b[2KSuccessfully installed arxiv-2.2.0 feedparser-6.0.12 google-genai-1.43.0 sgmllib3k-1.0.0\n",
            "\n",
            "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.1.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m25.2\u001b[0m\n",
            "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpip install --upgrade pip\u001b[0m\n"
          ]
        }
      ],
      "source": [
        "!pip install --upgrade google-genai google-api-python-client google-auth-httplib2 google-auth-oauthlib"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "E_Sca2oLyWi5"
      },
      "source": [
        "#Introduction: Building a Newsletter with a Team of AI Agents\n",
        "\n",
        "This notebook demonstrates how to build a simple but powerful autonomous agentic system. Think of it as assembling a team of specialized AI agents that collaborate to achieve a complex goal—in this case, researching and writing a newsletter from a single instruction.\n",
        "\n",
        "Here is the workflow:\n",
        "\n",
        "1.The Planner 🧠: You provide a high-level goal (e.g., \"Create a newsletter about AI memory techniques\"). The Planner agent then breaks this down into a detailed, step-by-step to-do list.\n",
        "\n",
        "2.The Specialists 🧑‍🔬: The system assigns each task to the right specialist. An agent_search handles general web research, while an agent_arxiv dives into academic papers to find scholarly sources.\n",
        "\n",
        "3.The Synthesizer ✍️: As the specialists complete their tasks, their findings are gathered. A final agent then synthesizes all this information into a single, well-structured newsletter.\n",
        "\n",
        "4.The Critic 🤔: To enable learning and improvement, a Critic agent reviews the entire process—from the initial plan to the final output—and provides feedback on how the system can perform better next time.\n",
        "\n",
        "By the end, you'll see a complete, end-to-end simulation of an autonomous system that can plan, execute, synthesize, and reflect to accomplish a creative task."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WJY-CMYBW1fp"
      },
      "source": [
        "#Helper functions to render the search output in markdown"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "twrrvkdh4GNi",
        "outputId": "1d38988c-6f7f-417d-a0ec-bdf069446f52"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;33mWARNING:\u001b[0m Your active project does not match the quota project in your local Application Default Credentials file. This might result in unexpected quota issues.\n",
            "\n",
            "To update your Application Default Credentials quota project, use the `gcloud auth application-default set-quota-project` command.\n",
            "Updated property [core/project].\n",
            "\n",
            "\n",
            "Updates are available for some Google Cloud CLI components.  To install them,\n",
            "please run:\n",
            "  $ gcloud components update\n",
            "\n",
            "\n",
            "\n",
            "To take a quick anonymous survey, run:\n",
            "  $ gcloud survey\n",
            "\n",
            "Your browser has been opened to visit:\n",
            "\n",
            "    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8085%2F&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fsqlservice.login&state=b0W8YIUtEoUir8NvyTmUjYKk0xNjYo&access_type=offline&code_challenge=NTAfAc0diKxJ6tFFfraSOQEAoHvGL3axb1KPtS2fiK0&code_challenge_method=S256\n",
            "\n",
            "\n",
            "Credentials saved to file: [/Users/remyw/.config/gcloud/application_default_credentials.json]\n",
            "\n",
            "These credentials will be used by any library that requests Application Default Credentials (ADC).\n",
            "\n",
            "Quota project \"remy-sandbox\" was added to ADC which can be used by Google client libraries for billing and quota. Note that some services may still bill the project owning the resource.\n"
          ]
        }
      ],
      "source": [
        "!export GOOGLE_CLOUD_PROJECT='remy-sandbox'\n",
        "!export GOOGLE_CLOUD_LOCATION=global\n",
        "!export GOOGLE_GENAI_USE_VERTEXAI=True\n",
        "\n",
        "!gcloud config set project remy-sandbox\n",
        "\n",
        "!gcloud auth application-default login --scopes=openid,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive.readonly"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "jbW3PA0S5fS0"
      },
      "outputs": [],
      "source": [
        "!export GOOGLE_CLOUD_PROJECT='remy-sandbox'\n",
        "!export GOOGLE_CLOUD_LOCATION=global\n",
        "!export GOOGLE_GENAI_USE_VERTEXAI=True\n",
        "\n",
        "\n",
        "client = genai.Client(vertexai=True, project='remy-sandbox', location='us-central1', http_options=HttpOptions(api_version=\"v1\"))\n",
        "MODEL_ID = \"gemini-2.5-flash\"\n",
        "\n",
        "def model_response(text,model_id):\n",
        "   response = client.models.generate_content(\n",
        "    model=genai.GenerativeModel(model_id),\n",
        "    contents = text\n",
        ")\n",
        "   return response.text"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {},
      "outputs": [],
      "source": [
        "!export GOOGLE_CLOUD_PROJECT='remy-sandbox'\n",
        "!export GOOGLE_CLOUD_LOCATION=global\n",
        "!export GOOGLE_GENAI_USE_VERTEXAI=True"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "id": "sDRH9UNcUZcm"
      },
      "outputs": [],
      "source": [
        "from google import genai\n",
        "import json\n",
        "from IPython.display import display, HTML, Markdown\n",
        "from google.genai.types import HttpOptions\n",
        "\n",
        "\n",
        "def show_json(obj):\n",
        "  print(json.dumps(obj.model_dump(exclude_none=True), indent=2))\n",
        "  return json.dumps(obj.model_dump(exclude_none=True), indent=2)\n",
        "\n",
        "def show_parts(r):\n",
        "  parts = r.candidates[0].content.parts\n",
        "  if parts is None:\n",
        "    finish_reason = r.candidates[0].finish_reason\n",
        "    print(f'{finish_reason=}')\n",
        "    return\n",
        "  for part in r.candidates[0].content.parts:\n",
        "    if part.text:\n",
        "      display(Markdown(part.text))\n",
        "      output = part.text\n",
        "    elif part.executable_code:\n",
        "      display(Markdown(f'```python\\n{part.executable_code.code}\\n```'))\n",
        "      output = part.executable_code\n",
        "    else:\n",
        "      show_json(part)\n",
        "\n",
        "  grounding_metadata = r.candidates[0].grounding_metadata\n",
        "  if grounding_metadata and grounding_metadata.search_entry_point:\n",
        "    display(HTML(grounding_metadata.search_entry_point.rendered_content))\n",
        "  return output\n",
        "\n",
        "!export GOOGLE_CLOUD_PROJECT='remy-sandbox'\n",
        "!export GOOGLE_CLOUD_LOCATION=global\n",
        "!export GOOGLE_GENAI_USE_VERTEXAI=True\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "#client = genai.Client(api_key=\"\")\n",
        "\n",
        "client = genai.Client(vertexai=True, project='remy-sandbox', location='us-central1', http_options=HttpOptions(api_version=\"v1\"))\n",
        "MODEL_ID = \"gemini-2.5-flash\"\n",
        "\n",
        "def model_response(text,model_id):\n",
        "   response = client.models.generate_content(\n",
        "    model=model_id,\n",
        "    contents = text\n",
        ")\n",
        "   return response.text\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HqPLD4ggyQ9H"
      },
      "source": [
        "##Creating the search agent"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "zC04YihLyQTy"
      },
      "outputs": [],
      "source": [
        "search_tool = {'google_search': {}}\n",
        "search_chat = client.chats.create(model=\"gemini-2.5-flash\", config={'tools': [search_tool]})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iULV58VxXRiO"
      },
      "source": [
        "#Create the Google Drive Agent"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "9VTKZ9n4Xq9q"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import json\n",
        "from dataclasses import dataclass, asdict\n",
        "from typing import List, Optional\n",
        "from datetime import datetime\n",
        "from dateutil import parser as dateparser\n",
        "\n",
        "from googleapiclient.discovery import build\n",
        "from google.auth import default\n",
        "from google.auth.transport.requests import Request\n",
        "from google.oauth2.credentials import Credentials"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e9QFlQT-tkP-",
        "outputId": "b5e173bf-01bc-4f45-c6ef-0f24c4877769"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "Warning: there are non-text parts in the response: ['thought_signature'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Here are the 5 most recent arXiv papers related to speculative decoding or streaming inference for LLMs in cs.LG or cs.CL categories, along with their summaries and PDF links:\n",
            "\n",
            "1.  **Title**: OWL: Overcoming Window Length-Dependence in Speculative Decoding for Long-Context Inputs\n",
            "    *   **Authors**: Jaeseong Lee, seung-won hwang, Aurick Qiao, Gabriele Oliaro, Ye Wang, Samyam Rajbhandari\n",
            "    *   **Summary**: Speculative decoding promises faster inference for large language models (LLMs), yet existing methods fail to generalize to real-world settings. Benchmarks typically assume short contexts (e.g., 2K tokens), whereas practical workloads involve long contexts. This paper finds current approaches degrade severely with long contexts, with some even slowing down generation speed. It addresses these limitations by releasing a new long-context benchmark (LongSpecBench) and introducing a novel model (OWL). OWL achieves about 5x higher acceptance length than EAGLE3 on long-context inputs through three innovations: (1) an LSTM-based drafter conditioned only on the last-token state, making it generalize to various lengths, (2) a special token [SPEC] in the verifier that produces richer repr.\n",
            "    *   **PDF Link**: http://arxiv.org/pdf/2510.07535v1\n",
            "\n",
            "2.  **Title**: Can Speech LLMs Think while Listening?\n",
            "    *   **Authors**: Yi-Jen Shih, Desh Raj, Chunyang Wu, Wei Zhou, SK Bong, Yashesh Gaur, Jay Mahadeokar, Ozlem Kalinli, Mike Seltzer\n",
            "    *   **Summary**: Recent advances in speech large language models (speech LLMs) have enabled seamless spoken interactions, but these systems still struggle with complex reasoning tasks. Previously, chain-of-thought (CoT) prompting or fine-tuning has been shown to significantly improve the reasoning abilities of text-based LLMs. This work investigates the effect of CoT fine-tuning for multi-stream speech LLMs, demonstrating that reasoning in text space improves the accuracy of speech LLMs by 2.4x, on average, over a suite of spoken reasoning tasks. Beyond accuracy, the latency of the spoken response is a crucial factor for interacting with voice-based agents. Inspired by the human behavior of \"thinking while listening,\" the paper proposes methods to reduce the additional latency from reasoning by allowing the model to think while listening.\n",
            "    *   **PDF Link**: http://arxiv.org/pdf/2510.07497v1\n",
            "\n",
            "3.  **Title**: RedTWIZ: Diverse LLM Red Teaming via Adaptive Attack Planning\n",
            "    *   **Authors**: Artur Horal, Daniel Pina, Henrique Paz, Iago Paulo, João Soares, Rafael Ferreira, Diogo Tavares, Diogo Glória-Silva, João Magalhães, David Semedo\n",
            "    *   **Summary**: This paper presents RedTWIZ: an adaptive and diverse multi-turn red teaming framework, to audit the robustness of Large Language Models (LLMs) in AI-assisted software development. The work is driven by three major research streams: (1) robust and systematic assessment of LLM conversational jailbreaks; (2) a diverse generative multi-turn attack suite, supporting compositional, realistic and goal-oriented jailbreak conversational strategies; and (3) a hierarchical attack planner, which adaptively plans, serializes, and triggers attacks tailored to specific LLM's vulnerabilities. Together, these contributions form a unified framework combining assessment, attack generation, and strategic planning to comprehensively evaluate LLMs.\n",
            "    *   **PDF Link**: http://arxiv.org/pdf/2510.06994v1\n",
            "\n",
            "4.  **Title**: SHANKS: Simultaneous Hearing and Thinking for Spoken Language Models\n",
            "    *   **Authors**: Cheng-Han Chiang, Xiaofei Wang, Linjie Li, Chung-Ching Lin, Kevin Lin, Shujie Liu, Zhendong Wang, Zhengyuan Yang, Hung-yi Lee, Lijuan Wang\n",
            "    *   **Summary**: Current large language models (LLMs) and spoken language models (SLMs) begin thinking and taking actions only after the user has finished their turn. This prevents the model from interacting during the user's turn and can lead to high response latency while it waits to think, which is not suitable for speech-to-speech interaction. This paper addresses this by noting that humans naturally \"think while listening.\" It proposes SHANKS, a general inference framework that enables SLMs to generate unspoken chain-of-thought reasoning while listening to the user input. SHANKS streams the input speech in fixed-duration chunks and, as soon as a chunk is received, generates unspoken reasoning.\n",
            "    *   **PDF Link**: http://arxiv.org/pdf/2510.06917v1\n",
            "\n",
            "5.  **Title**: Attention Sinks and Compression Valleys in LLMs are Two Sides of the Same Coin\n",
            "    *   **Authors**: Enrique Queipo-de-Llano, Álvaro Arroyo, Federico Barbero, Xiaowen Dong, Michael Bronstein, Yann LeCun, Ravid Shwartz-Ziv\n",
            "    *   **Summary**: Attention sinks and compression valleys have attracted significant attention as two puzzling phenomena in large language models, but have been studied in isolation. This work presents a surprising connection between attention sinks and compression valleys, tracing both to the formation of massive activations in the residual stream. It proves theoretically that massive activations necessarily produce representational compression and establishes bounds on the resulting entropy reduction. Through experiments across several models (410M-120B parameters), the paper confirms that when the beginning-of-sequence token develops extreme activation norms in the middle layers, both compression valleys and attention sinks emerge simultaneously. Targeted ablation studies validate the theoretical predictions.\n",
            "    *   **PDF Link**: http://arxiv.org/pdf/2510.06477v1\n",
            "\n",
            "Please note that I am providing the abstracts as summaries of contributions, as I do not have the capability to read and interpret the full PDF content to generate a novel summary.\n"
          ]
        }
      ],
      "source": [
        "# gemini_gdrive_tool.py\n",
        "\n",
        "from __future__ import annotations\n",
        "\n",
        "import json\n",
        "import os\n",
        "from typing import Any, Dict, List, Optional\n",
        "\n",
        "from google import genai\n",
        "from google.genai import types\n",
        "from google.auth import default\n",
        "from googleapiclient.discovery import build\n",
        "from google.genai.types import HttpOptions\n",
        "\n",
        "\n",
        "# --- Configure the Gemini client ---
",
        "client = genai.Client(vertexai=True, project='remy-sandbox', location='us-central1', http_options=HttpOptions(api_version=\"v1\"))\n",
        "MODEL_ID = \"gemini-2.5-flash\"\n",
        "\n",
        "\n",
        "# --- Tool Implementation: Google Drive search ---
",
        "def search_google_drive(\n",
        "    query: str,\n",
        "    max_results: int = 10,\n",
        ") -> Dict[str, Any]:\n",
        "    \"\"\"\n",
        "    Execute a Google Drive search and return a JSON-serializable payload.\n",
        "    Query string is used to search for file names.\n",
        "    \"\"\"\n",
        "    creds, _ = default()\n",
        "    drive_service = build('drive', 'v3', credentials=creds)\n",
        "\n",
        "    results = drive_service.files().list(\n",
        "        q=f\"name contains '{query}' and mimeType != 'application/vnd.google-apps.folder'\",\n",
        "        pageSize=max_results,\n",
        "        fields=\"nextPageToken, files(id, name, mimeType, webViewLink)\"\n",
        "    ).execute()\n",
        "\n",
        "    items = results.get('files', [])\n",
        "    \n",
        "    files_content = []\n",
        "    for item in items:\n",
        "        file_id = item['id']\n",
        "        file_name = item['name']\n",
        "        mime_type = item['mimeType']\n",
        "        \n",
        "        content = None\n",
        "        try:\n",
        "            if mime_type == 'application/vnd.google-apps.document': # Google Doc\n",
        "                request = drive_service.files().export_media(fileId=file_id, mimeType='text/plain')\n",
        "                content = request.execute().decode('utf-8')\n",
        "            elif mime_type.startswith('text/') or mime_type == 'application/json' or mime_type == 'application/rtf' or mime_type == 'application/pdf':\n",
        "                 if mime_type == 'application/pdf':\n",
        "                     # can't just read pdfs, would need a library. Skipping for now.\n",
        "                     continue\n",
        "                 request = drive_service.files().get_media(fileId=file_id)\n",
        "                 content = request.execute().decode('utf-8')\n",
        "        except Exception as e:\n",
        "            print(f'Error reading file {file_name}: {e}')
",
        "            content = f'Error reading file: {e}'",
        "\n",
        "        if content:\n",
        "            files_content.append({\n",
        "                "name": file_name,\n",
        "                "summary": content[:800], # Truncate for brevity\n",
        "                "link": item['webViewLink']\n",
        "            })\n",
        "\n",
        "    return {\n",
        "        "query": query,\n",
        "        "count": len(files_content),\n",
        "        "results": files_content,\n",
        "    }\n",
        "\n",
        "# --- Tool declaration (matches Gemini function-calling schema) ---
",
        "gdrive_tool = types.Tool(\n",
        "    function_declarations=[
",
        "        {
",
        "            "name": "search_google_drive",
",
        "            "description": (\n",
        "                "Search Google Drive for documents with a given query in their name. "\n",
        "                "Returns a JSON list of documents with metadata and content."
",
        "            ),
",
        "            "parameters": {
",
        "                "type": "object",
",
        "                "properties": {
",
        "                    "query": {
",
        "                        "type": "string",
",
        "                        "description": "Query string to search for in file names in Google Drive.",
",
        "                    },
",
        "                    "max_results": {
",
        "                        "type": "integer",
",
        "                        "minimum": 1,
",
        "                        "maximum": 50,
",
        "                        "default": 10,
",
        "                        "description": "Maximum number of files to return (cap at 50). ignited by users ask",
",
        "                    },
",
        "                },
",
        "                "required": ["query"],
",
        "            },
",
        "        }
",
        "    ]
",
        ")
",
        "\n",
        "# --- Dispatch: map function calls to Python implementations ---
",
        "def handle_tool_call(name: str, args: Dict[str, Any]) -> Dict[str, Any]:\n",
        "    if name == \"search_google_drive\":\n",
        "        return search_google_drive(**args)\n",
        "    raise ValueError(f\"Unknown tool: {name}\")\n",
        "\n",
        "config = types.GenerateContentConfig(tools=[gdrive_tool])\n",
        "# --- Conversation with function calling loop ---
",
        "def ask_gemini_with_gdrive(prompt: str, model: str = \"gemini-2.5-flash\") -> str:\n",
        "    contents = [\n",
        "        types.Content(role=\"user\", parts=[ types.Part(text=prompt) ])\n",
        "    ]\n",
        "\n",
        "    response = client.models.generate_content(\n",
        "        model=model,\n",
        "        contents=contents,\n",
        "        config=config,\n",
        "    )\n",
        "\n",
        "    tool_call = None\n",
        "    for cand in response.candidates or []:\n",
        "        for part in (cand.content.parts or []):\n",
        "            if getattr(part, \"function_call\", None):\n",
        "                tool_call = part.function_call\n",
        "                break\n",
        "        if tool_call:\n",
        "            break\n",
        "\n",
        "    if not tool_call:\n",
        "        return response.text\n",
        "\n",
        "    args = tool_call.args\n",
        "    tool_result = handle_tool_call(tool_call.name, args)\n",
        "\n",
        "    function_response_part = types.Part.from_function_response(\n",
        "        name=tool_call.name,\n",
        "        response={"result": tool_result},\n",
        "    )\n",
        "\n",
        "    contents.append(response.candidates[0].content)\n",
        "    contents.append(types.Content(role=\"user\", parts=[function_response_part]))\n",
        "\n",
        "    final = client.models.generate_content(\n",
        "        model=model,\n",
        "        contents=contents,\n",
        "        config=config,\n",
        "    )\n",
        "\n",
        "    return final.text\n",
        "\n",
        "# --- Example usage ---
",
        "if __name__ == \"__main__\":\n",
        "    demo_prompt = (\n",
        "        \"Find 5 documents in my Google Drive about 'speculative decoding' "\n",
        "        "or 'streaming' inference for LLMs. Summarize them.\"\n",
        "    )\n",
        "    print(ask_gemini_with_gdrive(demo_prompt))\n"
      ]
    }
```
```json
{
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VC105_paXsFj"
      },
      "source": [
        "#Build an autonomous system for generating newsletters"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "MmNjaAVSXgpr"
      },
      "outputs": [],
      "source": [
        "problem = \"\"\"You are the curator for the Agentville newsletter. Your task is to assemble the content for the centennial edition, covering the developments in autonomous agents. The newsletter should be in a witty format\n",
        "and should cover different dimensions of autonomous agents.\"\"\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "snVFjqW-X63s"
      },
      "source": [
        "##Planner in action"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "14fAzU1UypyI"
      },
      "outputs": [],
      "source": [
        "plan = model_response(f'''You are a planning agent inside an autonomous multi-agent system.\n",
        "Your job is to take a user's goal:{problem} and break it into a structured to-do list of clear steps.\n",
        "You have access to Search and Google Drive retrieval tools.\n",
        "\n",
        "Instructions:\n",
        "1. Understand the user’s goal.\n",
        "2. Break it down into the smallest actionable steps needed to achieve it. You are not supposed to come up with\n",
        "the final answer to the problem.\n",
        "3. Each step must be atomic (can be completed by a single specialized agent).\n",
        "4. Order the steps logically. Outline which agent among search and gdrive needs to be used to tackle each step.\n",
        "5.Format of the step: Tool name, step description. Available tool names are agent_search and agent_gdrive\n",
        "6.Separate each step with a --\n",
        "7. Include a final step to \"summarize the overall findings\" once all tasks are done.''',"gemini-2.5-pro")
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oKs3cErb0Ypp",
        "outputId": "cd9672ef-c728-4227-ca06-3c4643821f35"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\n",
            "--\n",
            "agent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\n",
            "--\n",
            "agent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\n",
            "--\n",
            "agent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\n",
            "--\n",
            "agent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\n",
            "--\n",
            "agent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\n",
            "--\n",
            "agent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\n",
            "--\n",
            "agent_arxiv, Investigate the future outlook and grand challenges in the field of autonomous agents, including topics like long-term planning and open-ended learning.\n",
            "--\n",
            "agent_search, Find articles and expert opinions on the ethical considerations, safety challenges, and societal impact of deploying advanced autonomous agents.\n",
            "--\n",
            "agent_search, Summarize the overall findings to synthesize the gathered information into a cohesive newsletter structure.\n"
          ]
        }
      ],
      "source": [
        "print (plan)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "6ZfB1PhUy0RB"
      },
      "outputs": [],
      "source": [
        "plan_steps = plan.split('--')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "392D_o2x0df5",
        "outputId": "bdd9da5c-2300-4705-8ada-4e96e9cb97e7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "10"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "len(plan_steps)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "0ua7oZkwI1Jl",
        "outputId": "a382369e-18df-4f84-a2d3-7670a474e31c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'\\nagent_search, Summarize the overall findings to synthesize the gathered information into a cohesive newsletter structure.'"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "plan_steps[-1]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lzMQ2uWiYT8U"
      },
      "source": [
        "## Helper functions to call Explorer and Scholar"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "id": "nFrdP-t65Ufc"
      },
      "outputs": [],
      "source": [
        "#TODO find stories from author corresponding to {step}\n",
        "\n",
        "async def handle_search(memory, step: str):\n",
        "    print(f\"[SEARCH] Handling search step: {step}\")\n",
        "    #\n",
        "    r = search_chat.send_message(f'''For the step: {step}, extract relevant context from memory: {memory} and execute the step.''')\n",
        "    response = show_parts(r)\n",
        "    # your search logic here\n",
        "    return response\n",
        "\n",
        "async def handle_gdrive(memory, step: str):\n",
        "    print(f\"[GDRIVE] Handling gdrive step: {step}\")\n",
        "    response = ask_gemini_with_gdrive(f'''Find out documents from google drive corresponding to the {step}. Use {memory} for context.''')\n",
        "    # your gdrive logic here\n",
        "    return response\n",
        "\n",
        "async def handle_default(memory, step: str):\n",
        "    print(f\"[DEFAULT] Handling generic step: {step}\")\n",
        "    response = model_response(f'''For the step: {step}, extract relevant context from memory: {memory} and execute the step.''',"gemini-2.5-flash")\n",
        "    # your fallback logic here\n",
        "    return response\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FQtIPoQNYjId"
      },
      "source": [
        "##Agent orchestration"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "bsLKePt5yW-8",
        "outputId": "2201a0dc-9987-4d35-d3eb-4ad26646bf61"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>}\n",
            "\n",
            "agent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>}\n",
            "\n",
            "agent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>}\n",
            "\n",
            "agent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>}\n",
            "\n",
            "agent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>}\n",
            "\n",
            "agent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>, '\\nagent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\\n': <coroutine object handle_search at 0x10eb4ca40>}\n",
            "\n",
            "agent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>, '\\nagent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\\n': <coroutine object handle_search at 0x10eb4ca40>, '\\nagent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\\n': <coroutine object handle_search at 0x10eb4cc40>}\n",
            "\n",
            "agent_arxiv, Investigate the future outlook and grand challenges in the field of autonomous agents, including topics like long-term planning and open-ended learning.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>, '\\nagent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\\n': <coroutine object handle_search at 0x10eb4ca40>, '\\nagent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\\n': <coroutine object handle_search at 0x10eb4cc40>, '\\nagent_arxiv, Investigate the future outlook and grand challenges in the field of autonomous agents, including topics like long-term planning and open-ended learning.\\n': <coroutine object handle_arxiv at 0x10eb35120>}\n",
            "\n",
            "agent_search, Find articles and expert opinions on the ethical considerations, safety challenges, and societal impact of deploying advanced autonomous agents.\n",
            "\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>, '\\nagent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\\n': <coroutine object handle_search at 0x10eb4ca40>, '\\nagent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\\n': <coroutine object handle_search at 0x10eb4cc40>, '\\nagent_arxiv, Investigate the future outlook and grand challenges in the field of autonomous agents, including topics like long-term planning and open-ended learning.\\n': <coroutine object handle_arxiv at 0x10eb35120>, '\\nagent_search, Find articles and expert opinions on the ethical considerations, safety challenges, and societal impact of deploying advanced autonomous agents.\\n': <coroutine object handle_search at 0x10eb4cb40>}\n",
            "\n",
            "agent_search, Summarize the overall findings to synthesize the gathered information into a cohesive newsletter structure.\n",
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>, '\\nagent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\\n': <coroutine object handle_search at 0x10eb4ca40>, '\\nagent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\\n': <coroutine object handle_search at 0x10eb4cc40>, '\\nagent_arxiv, Investigate the future outlook and grand challenges in the field of autonomous agents, including topics like long-term planning and open-ended learning.\\n': <coroutine object handle_arxiv at 0x10eb35120>, '\\nagent_search, Find articles and expert opinions on the ethical considerations, safety challenges, and societal impact of deploying advanced autonomous agents.\\n': <coroutine object handle_search at 0x10eb4cb40>, '\\nagent_search, Summarize the overall findings to synthesize the gathered information into a cohesive newsletter structure.': <coroutine object handle_search at 0x10eb4cd40>}\n"
          ]
        }
      ],
      "source": [
        "memory = {}\n",
        "for i in range(1,len(plan_steps)+1):\n",
        "  print (f\"{plan_steps[i-1]}\")\n",
        "  if \"agent_search\" in plan_steps[i-1]:\n",
        "        agent_response = handle_search(memory, plan_steps[i-1])\n",
        "  elif \"agent_gdrive\" in plan_steps[i-1]:\n",
        "        agent_response = handle_gdrive(memory, plan_steps[i-1])\n",
        "  else:\n",
        "        agent_response = handle_default(memory, plan_steps[i-1])\n",
        "  memory[plan_steps[i-1]] = agent_response\n",
        "  print (memory)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ikxWOmlONGeH",
        "outputId": "10b1f544-0099-48c7-a6a1-8ad317aee1da"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'agent_search, Find examples of witty and engaging technology newsletters or articles to establish a humorous and clever writing style for the content.\\n': <coroutine object handle_search at 0x10eb4c840>, '\\nagent_search, Research the key historical milestones and foundational concepts in the development of autonomous agents to create a \"look back\" section for the centennial edition.\\n': <coroutine object handle_search at 0x10eb4c640>, '\\nagent_arxiv, Find a highly-cited survey paper on recent advancements in autonomous agent architectures, focusing on the core components like planning, memory, and tool use.\\n': <coroutine object handle_arxiv at 0x10eb349a0>, '\\nagent_search, Identify recent (last 1-2 years) high-profile examples or breakthroughs of autonomous agents in action to showcase the current state-of-the-art.\\n': <coroutine object handle_search at 0x10eb4c940>, '\\nagent_arxiv, Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.\\n': <coroutine object handle_arxiv at 0x10eb35030>, '\\nagent_search, Find case studies and articles on the practical applications of autonomous agents in specific fields, such as software development, scientific research, or personal assistants.\\n': <coroutine object handle_search at 0x10eb4ca40>, '\\nagent_search, Research the concept of multi-agent systems and emergent collaboration, looking for accessible explanations and interesting examples.\\n': <coroutine object handle_search at 0x10eb4cc40>, '\\nagent_arxiv, Investigate the future outlook and grand challenges in the field of autonomous agents, including topics like long-term planning and open-ended learning.\\n': <coroutine object handle_arxiv at 0x10eb35120>, '\\nagent_search, Find articles and expert opinions on the ethical considerations, safety challenges, and societal impact of deploying advanced autonomous agents.\\n': <coroutine object handle_search at 0x10eb4cb40>, '\\nagent_search, Summarize the overall findings to synthesize the gathered information into a cohesive newsletter structure.': <coroutine object handle_search at 0x10eb4cd40>}\n"
          ]
        }
      ],
      "source": [
        "print (memory)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kuKyrTlCVs85",
        "outputId": "91f0dcfe-5ef5-4910-9642-33c5c872472e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Here is a detailed report summarizing the research tasks, categorized by the agent assigned:\n",
            "\n",
            "```markdown\n",
            "# Autonomous Agents Centennial Newsletter Research Plan\n",
            "\n",
            "This document outlines the research tasks to gather information for the centennial edition of a newsletter focused on autonomous agents. The tasks are categorized by the agent responsible for their execution.\n",
            "\n",
            "## Agent: `agent_search`\n",
            "\n",
            "This agent is tasked with conducting web searches to gather general information, examples, case studies, and expert opinions.\n",
            "\n",
            "*   **Find examples of witty and engaging technology newsletters or articles** to establish a humorous and clever writing style for the content.\n",
            "*   **Research the key historical milestones and foundational concepts** in the development of autonomous agents to create a \"look back\" section for the centennial edition.\n",
            "*   **Identify recent (last 1-2 years) high-profile examples or breakthroughs** of autonomous agents in action to showcase the current state-of-the-art.\n",
            "*   **Find case studies and articles on the practical applications of autonomous agents** in specific fields, such as software development, scientific research, or personal assistants.\n",
            "*   **Research the concept of multi-agent systems and emergent collaboration**, looking for accessible explanations and interesting examples.\n",
            "*   **Find articles and expert opinions on the ethical considerations, safety challenges, and societal impact** of deploying advanced autonomous agents.\n",
            "*   **Summarize the overall findings** to synthesize the gathered information into a cohesive newsletter structure.\n",
            "\n",
            "## Agent: `agent_arxiv`\n",
            "\n",
            "This agent is responsible for searching the arXiv pre-print repository, primarily for academic papers and surveys.\n",
            "\n",
            "*   **Find a highly-cited survey paper on recent advancements in autonomous agent architectures**, focusing on the core components like planning, memory, and tool use.\n",
            "*   **Research the role of Large Language Models (LLMs) as the reasoning engine or \"brain\" for modern autonomous agents.**\n",
            "*   **Investigate the future outlook and grand challenges in the field of autonomous agents**, including topics like long-term planning and open-ended learning.\n",
            "```\n"
          ]
        }
      ],
      "source": [
        "print (model_response(f'''Render the response:{memory} in the form of a detailed report in markdown format with proper indentation.\n",
        "Preserve the hyperlinks to the research papers and links cited.''','gemini-2.5-flash'))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OJXAQyVWOdV0"
      },
      "source": [
        "## Critic"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "id": "L4ypXXGZOKvr"
      },
      "outputs": [],
      "source": [
        "critic_response = model_response(f'''For the given problem:{problem}, a bunch of agents worked together to curate the response: {memory}. Your\n",
        "job is to analyze how well the original plan: {plan} was executed and suggest improvements for the overall system and individual agents involved.''',\"gemini-2.5-pro\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s8h3WF7rUdJ3",
        "outputId": "26b3fa95-6649-4fa6-ca50-6131b6a9e98f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Excellent. This is a fascinating look under the hood of a multi-agent system at work. My analysis will focus on the quality of the plan's execution, followed by actionable suggestions for improving the overall system and the individual agents.\n",
            "\n",
            "### Analysis of Plan Execution\n",
            "\n",
            "The provided output `{'agent_call': <coroutine object>}` indicates that the system successfully parsed the original plan and instantiated the necessary tasks for execution. This is a critical and successful first step.\n",
            "\n",
            "Here's a breakdown of how well the plan was executed, based on its structure and the tasks generated:\n",
            "\n",
            "**What Went Well:**\n",
            "\n",
            "*   **High Fidelity to the Plan:** The system executed the plan with 100% fidelity. Every single step from the original plan was translated into a corresponding agent call. There were no omissions, misinterpretations, or re-orderings.\n",
            "*   **Correct Agent Selection:** The division of labor between `agent_search` and `agent_arxiv` is logical and well-executed.\n",
            "    *   `agent_search` was correctly tasked with finding contemporary articles, opinions, case studies, and stylistic examples—content typically found on the broader web.\n",
            "    *   `agent_arxiv` was appropriately assigned to find deep, technical, and research-oriented content like survey papers and investigations into future challenges, which are its primary domain.\n",
            "*   **Clear & Actionable Prompts:** The prompts generated for each agent are specific and effective. For example, \"Find a highly-cited survey paper\" for `agent_arxiv` is much better than a vague \"find papers.\" Similarly, asking `agent_search` for \"recent (last 1-2 years) high-profile examples\" provides a clear temporal constraint.\n",
            "\n",
            "**Limitations and Points of Friction:**\n",
            "\n",
            "*   **Purely Sequential Execution:** The plan is a rigid, linear sequence. Steps 1 through 9 are all independent data-gathering tasks. They do not rely on each other's outputs. Executing them one after another is highly inefficient. The entire data-gathering phase could have been run in parallel, drastically reducing the total time to completion.\n",
            "*   **Inappropriate Agent for Synthesis:** The final step, `agent_search, Summarize the overall findings...`, is a significant flaw in the plan's logic. **`agent_search` is a retrieval agent, not a synthesis or writer agent.** Its job is to find information, not to read, understand, integrate, and create a new, cohesive narrative in a \"witty format.\" This is like asking a librarian to not only find the books but also write the book report. The execution followed the flawed instruction, but the chosen tool is wrong for the job.\n",
            "\n",
            "---\n",
            "\n",
            "### Suggestions for Overall System Improvement\n",
            "\n",
            "The current system acts as a good \"Task Follower.\" To evolve, it needs to become a \"Project Manager.\"\n",
            "\n",
            "1.  **Implement Parallel Execution:**\n",
            "    *   The system should analyze the plan's dependency graph. It should identify that steps 1-9 are independent (\"embarrassingly parallel\") and execute them concurrently. Step 10 is the only one that depends on the completion of the previous steps. This single change would yield the most significant performance improvement.\n",
            "\n",
            "2.  **Introduce a Specialized Synthesis Agent:**\n",
            "    *   A new agent, let's call it `agent_writer` or `agent_curator`, should be created. Its core capability would be to take multiple text inputs (the findings from the other agents) and a set of instructions (e.g., \"witty format,\" \"newsletter structure\") to generate the final artifact.\n",
            "    *   The final step of the plan should be: `agent_writer, [Inputs from steps 1-9], Synthesize all findings into a witty newsletter for the centennial edition of Agentville.`.\n",
            "\n",
            "3.  **Establish a Shared Memory/Context:**\n",
            "    *   Instead of each agent operating in a vacuum, the system should maintain a shared \"workspace\" or \"context object\" (e.g., a JSON object).\n",
            "    *   As each search agent completes its task, it doesn't just return a block of text; it populates a structured field in this workspace. For example:\n",
            "        ```json\n",
            "        {\n",
            "          \"style_examples\": [\"link1\", \"link2\"],\n",
            "          \"historical_milestones\": [{\"year\": 1956, \"event\": \"Dartmouth Workshop\"}, ...],\n",
            "          \"state_of_the_art\": [{\"name\": \"Devin\", \"description\": \"...\"}, ...],\n",
            "          \"ethical_concerns\": [\"concern1_summary\", \"concern2_summary\"]\n",
            "        }\n",
            "        ```\n",
            "    *   This structured data is vastly easier for the `agent_writer` to parse and use than a collection of ten disconnected documents.\n",
            "\n",
            "4.  **Incorporate a \"Critique\" or \"Review\" Step:**\n",
            "    *   A robust system would not execute a plan blindly. After the data-gathering phase (steps 1-9), a \"Critique Agent\" could check the results.\n",
            "    *   **Example:** If `agent_search` for witty newsletters returned only dry academic papers, the Critique Agent could flag this mismatch and trigger a new search with a modified prompt (`\"Find examples from sources like 'Morning Brew' or 'The Verge'\"`), creating a dynamic, self-correcting loop.\n",
            "\n",
            "---\n",
            "\n",
            "### Suggestions for Individual Agent Improvement\n",
            "\n",
            "**`agent_search`:**\n",
            "\n",
            "*   **Beyond Links:** Instead of just returning links or raw page content, it should be upgraded to perform **summary and extraction**. The prompt `Find case studies...` should result in the agent returning a list of concise summaries of those case studies, not just the articles themselves.\n",
            "*   **Source Diversification:** The agent should be able to query multiple types of sources beyond a standard web search, including news APIs, specific blog platforms (like Medium), and social media (like Twitter/X) for expert opinions.\n",
            "*   **Confidence Scoring:** The agent could provide a confidence or relevance score for each finding, helping the system prioritize the most valuable information.\n",
            "\n",
            "**`agent_arxiv`:**\n",
            "\n",
            "*   **Deep Content Analysis:** The current agent likely just searches titles and abstracts. An advanced version should be able to **parse the full PDF text** to answer more specific questions. For instance, it could extract the \"Future Work\" section from papers when asked about grand challenges.\n",
            "*   **Citation Context:** When finding a \"highly-cited\" paper, an improved agent could analyze the papers that cite it. Are they building on it, or are they refuting it? This provides crucial context that a simple citation count misses.\n",
            "*   **Structured Output:** Like `agent_search`, it should return structured data. For a survey paper, it could extract the main sections, key definitions, and the primary conclusion into a more digestible format.\n",
            "\n",
            "### Final Verdict\n",
            "\n",
            "The system demonstrates a solid foundation in faithfully executing a predefined plan. Its failure is not in the *execution* itself, but in the lack of intelligence *around* the execution.\n",
            "\n",
            "By implementing parallel processing, introducing a specialized synthesis agent, and making the agents themselves smarter at structuring their output, the system can transition from a simple task-doer to a genuinely effective and collaborative autonomous workforce.\n"
          ]
        }
      ],
      "source": [
        "print (critic_response)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OZu5htAmuYZI"
      },
      "source": [
        "# Bringing everything together: Autonomous Agentic Module"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SlKPvcCuw3rc"
      },
      "source": [
        "Autonomous Agentic System Simulation\n",
        "This function simulates an autonomous agentic system that solves problems through a structured, multi-agent workflow. The process is designed to be iterative, incorporating feedback for continuous improvement.\n",
        "\n",
        "###Core Workflow\n",
        "\n",
        "1.Problem Input\n",
        "\n",
        "The process begins when a user provides a specific problem or query to the system.\n",
        "\n",
        "2.Planning Phase\n",
        "\n",
        "A central Planner agent analyzes the problem and formulates a strategic, step-by-step plan to address it.\n",
        "\n",
        "3.Delegation to Sub-agents\n",
        "\n",
        "The Planner delegates individual steps of the plan to specialized Sub-agents, each designed to handle a specific type of task (e.g., data retrieval, analysis, code execution).\n",
        "\n",
        "4.Execution and Synthesis\n",
        "\n",
        "The sub-agents execute their assigned tasks and return their findings to the Planner.\n",
        "\n",
        "5.The Planner collects all responses and synthesizes the distributed information into a single, cohesive solution.\n",
        "\n",
        "6.Final Report and Feedback Loop\n",
        "\n",
        "A final, comprehensive report is generated based on the synthesized findings.\n",
        "\n",
        "A Critic agent reviews the report to provide constructive feedback on its quality and accuracy.\n",
        "\n",
        "This feedback is then fed back into the system to improve its output quality for the next iteration, creating a continuous learning loop."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "id": "MdW3DdYYUv-c"
      },
      "outputs": [],
      "source": [
        "def autonomous_newsletter_generation(problem):\n",
        "  plan = model_response(f'''You are a planning agent inside an autonomous multi-agent system.\n",
        "Your job is to take a user's goal:{problem} and break it into a structured to-do list of clear steps.\n",
        "You have access to Search and Google Drive retrieval tools.\n",
        "\n",
        "Instructions:\n",
        "1. Understand the user’s goal.\n",
        "2. Break it down into the smallest actionable steps needed to achieve it. You are not supposed to come up with\n",
        "the final answer to the problem.\n",
        "3. Each step must be atomic (can be completed by a single specialized agent).\n",
        "4. Order the steps logically. Outline which agent among search and gdrive needs to be used to tackle each step.\n",
        "5.Format of the step: Tool name, step description. Available tool names are agent_search and agent_gdrive\n",
        "6.Separate each step with a --\n",
        "7. Include a final step to \"summarize the overall findings\" once all tasks are done.''',"gemini-2.5-pro")\n",
        "  print (\"Plan is\",plan)\n",
        "  plan_steps = plan.split('--')\n",
        "  memory = {}\n",
        "  for i in range(1,len(plan_steps)+1):\n",
        "     print (f\"{plan_steps[i-1]}\")\n",
        "     if \"agent_search\" in plan_steps[i-1]:\n",
        "        agent_response = handle_search(memory, plan_steps[i-1])\n",
        "     elif \"agent_gdrive\" in plan_steps[i-1]:\n",
        "        agent_response = handle_gdrive(memory, plan_steps[i-1])\n",
        "     else:\n",
        "        agent_response = handle_default(memory, plan_steps[i-1])\n",
        "     memory[plan_steps[i-1]] = agent_response\n",
        "\n",
        "  agent_report = model_response(f'''Render the response:{memory} in the form of a detailed report in markdown format with proper indentation.\n",
        "Preserve the hyperlinks to the documents and links cited.''','gemini-2.5-flash')\n",
        "  critic_response = model_response(f'''For the given problem:{problem}, a bunch of agents worked together to curate the response: {memory}. Your\n",
        "job is to analyze how well the original plan: {plan} was executed and suggest improvements for the overall system and individual agents involved.''',"gemini-2.5-pro")\n",
        "  return agent_report, critic_response\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "9op0bzUqvcol",
        "outputId": "ca6d5e81-fe61-4a5f-c483-d7fc0b271822"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Plan is agent_search, Search for foundational concepts of memory in autonomous AI agents, explaining the difference between short-term (working) memory and long-term memory.\n",
            "--\n",
            "agent_search, Research the role and limitations of short-term memory in LLM-based agents, focusing on the concept of context windows.\n",
            "--\n",
            "agent_search, Investigate common techniques for implementing long-term memory in agentic systems, such as vector databases and retrieval-augmented generation (RAG).\n",
            "--\n",
            "agent_arxiv, Search for recent research papers on novel memory architectures for autonomous agents. Use keywords like \"agent memory,\" \"long-term memory autonomous agents,\" and \"memory-augmented neural networks.\"\n",
            "--\n",
            "agent_search, Find information on hybrid memory approaches that combine different techniques (e.g., context windows with vector databases) to create more effective memory systems for agents.\n",
            "--\n",
            "agent_search, Identify practical applications and case studies of autonomous agents using advanced memory techniques in real-world scenarios (e.g., personalized assistants, complex problem-solving).\n",
            "--\n",
            "agent_search, Research the current challenges and future directions for memory in autonomous agents, such as scalability, information retrieval accuracy, and managing or \"forgetting\" irrelevant information.\n",
            "--\n",
            "Summarize the overall findings from all previous steps to create a cohesive overview for the newsletter.\n",
            "agent_search, Search for foundational concepts of memory in autonomous AI agents, explaining the difference between short-term (working) memory and long-term memory.\n",
            "\n",
            "\n",
            "agent_search, Research the role and limitations of short-term memory in LLM-based agents, focusing on the concept of context windows.\n",
            "\n",
            "\n",
            "agent_search, Investigate common techniques for implementing long-term memory in agentic systems, such as vector databases and retrieval-augmented generation (RAG).\n",
            "\n",
            "\n",
            "agent_arxiv, Search for recent research papers on novel memory architectures for autonomous agents. Use keywords like \"agent memory,\" \"long-term memory autonomous agents,\" and \"memory-augmented neural networks.\"\n",
            "\n",
            "\n",
            "agent_search, Find information on hybrid memory approaches that combine different techniques (e.g., context windows with vector databases) to create more effective memory systems for agents.\n",
            "\n",
            "\n",
            "agent_search, Identify practical applications and case studies of autonomous agents using advanced memory techniques in real-world scenarios (e.g., personalized assistants, complex problem-solving).\n",
            "\n",
            "\n",
            "agent_search, Research the current challenges and future directions for memory in autonomous agents, such as scalability, information retrieval accuracy, and managing or \"forgetting\" irrelevant information.\n",
            "\n",
            "\n",
            "Summarize the overall findings from all previous steps to create a cohesive overview for the newsletter.\n"
          ]
        }
      ],
      "source": [
        "report, analysis = autonomous_newsletter_generation('''Generate a newsletter around memory techniques used for\n",
        "autonomous agentic systems''')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PCUNozpJv_z4"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "agents",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.13.5"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
