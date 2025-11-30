# Resume Bot

This is a simple chatbot that acts as a personal assistant, answering questions based on a resume and a summary file. It's built using Python, Gradio for the UI, and OpenAI for the language model.

## Setup

This project uses `uv` for package management. Check the `pyproject.toml` file for the dependencies. Install UV first. Then run,

1.  **Install dependencies:**
    ```bash
    uv sync
    ```

2.  **Create a `.env` file:**
    This project requires a `.env` file in the `resume_bot` directory with the following secrets:

    ```
    OPENAI_API_KEY="your_openai_api_key"
    MAILJET_API_KEY="your_mailjet_api_key"
    MAILJET_API_SECRET="your_mailjet_api_secret"
    ```

3.  **Add your personal data:**
    - Place your resume in PDF format at `me/Resume_Md_Imtiaz_Hossain.pdf`.
    - Add a text summary of your background in `me/summary.txt`.

## Running the Application

To start the chatbot, run the following command:

```bash
python app.py
```

This will launch a Gradio web interface where you can interact with the bot.
