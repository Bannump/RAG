# My Personal Agent 🤖

A sophisticated RAG (Retrieval-Augmented Generation) application that serves as your personal AI assistant for daily tasks, from vehicle diagnostics to resume optimization.

## 🌟 Features

### 1. **Vehicle Diagnostics & Assistance**
- Upload dashboard pictures or car images
- AI-powered analysis of vehicle issues
- Actionable solutions with contact information (e.g., AAA roadside assistance)
- Step-by-step troubleshooting guides

### 2. **Resume Analysis & ATS Optimization**
- Compare your resume against job descriptions
- Detailed review with specific improvement suggestions
- ATS (Applicant Tracking System) compatibility scoring
- Automated resume modification to match job requirements

### 3. **Intelligent Resume Builder**
- Generate optimized resumes from your experiences, skills, and portfolio
- ATS-friendly formatting and keyword optimization
- Multiple output formats (PDF, DOCX, TXT)
- Industry-specific templates

## 🏗️ Architecture

```
My Personal Agent
├── Core RAG Engine (Vector DB + LLM Integration)
├── Image Analysis Module (Vision AI)
├── Resume Processing Module (ATS Optimization)
├── Authentication System
└── User Interface (CLI/Web)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- OpenAI API key (or Anthropic/other LLM provider)
- ChromaDB or Pinecone for vector storage (optional)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd RAG

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Configuration

Create a `.env` file with:
```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key  # Optional
VECTOR_DB_PATH=./data/vector_db
SECRET_KEY=your_secret_key_for_auth
DATABASE_PATH=./data/users.db
```

### Usage

```bash
# Run the application
python src/main.py

# Or use the CLI interface
python -m src.my_personal_agent.cli
```

## 📁 Project Structure

```
RAG/
├── src/
│   ├── my_personal_agent/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── rag_engine.py      # Core RAG implementation
│   │   │   ├── vector_store.py    # Vector database management
│   │   │   └── llm_client.py      # LLM API client abstraction
│   │   ├── modules/
│   │   │   ├── __init__.py
│   │   │   ├── vehicle_diagnostics.py  # Vehicle analysis module
│   │   │   ├── resume_analyzer.py      # Resume analysis & ATS
│   │   │   └── resume_builder.py       # Resume generation
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── user_manager.py    # User authentication
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── file_handler.py    # File operations
│   │   │   ├── image_processor.py # Image preprocessing
│   │   │   └── text_processor.py  # Text preprocessing
│   │   └── cli.py                 # CLI interface
│   └── main.py                    # Main entry point
├── tests/
│   ├── test_rag_engine.py
│   ├── test_resume_analyzer.py
│   └── test_vehicle_diagnostics.py
├── docs/
│   ├── architecture.md
│   └── api_reference.md
├── data/
│   ├── vector_db/                 # Vector database storage
│   └── users.db                   # User database
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🔧 Core Components

### 1. RAG Engine
- **Vector Store**: ChromaDB for embedding storage and similarity search
- **LLM Integration**: OpenAI GPT-4/Vision, Anthropic Claude, etc.
- **Context Retrieval**: Semantic search with re-ranking

### 2. Image Analysis
- Vision AI integration (GPT-4 Vision, Claude Vision)
- Image preprocessing and feature extraction
- Context-aware response generation

### 3. Resume Processing
- PDF/DOCX parsing
- ATS keyword extraction and matching
- Resume scoring and gap analysis
- Automated content enhancement

### 4. Authentication
- Secure user management
- Session handling
- API key management per user

## 📊 Technology Stack

- **Python 3.9+**
- **Vector Database**: ChromaDB (local) or Pinecone (cloud)
- **LLM Providers**: OpenAI, Anthropic
- **Embeddings**: OpenAI text-embedding-3-small
- **Document Processing**: PyPDF2, python-docx, pdfplumber
- **Image Processing**: PIL/Pillow, OpenCV
- **Web Framework** (Optional): FastAPI, Streamlit
- **Database**: SQLite (or PostgreSQL for production)

## 🤝 Contributing

This is a personal project, but contributions and suggestions are welcome!

## 📝 License

MIT License - feel free to use and modify for your own projects.

## 🙏 Acknowledgments

Built with OpenAI, Anthropic, and the open-source community.

Try it yourself:

My Personal Agent - Your AI-powered personal assistant

positional arguments:
  {vehicle,analyze-resume,build-resume,auth}
                        Available commands
    vehicle             Diagnose vehicle issues from images
    analyze-resume      Analyze resume against job description
    build-resume        Build optimized resume from data
    auth                User authentication

options:
  -h, --help            show this help message and exit

Examples:
  # Vehicle diagnostics
  python -m src.my_personal_agent.cli vehicle --image car_dashboard.jpg --description "Car won't start"

  # Resume analysis
  python -m src.my_personal_agent.cli analyze-resume --resume my_resume.pdf --job-description "Software Engineer position..."

  # Build resume
  python -m src.my_personal_agent.cli build-resume --input-file resume_data.json