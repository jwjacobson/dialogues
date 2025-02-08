# dialogues - philosophical dialogues between LLM agents
This app will generate Platonic-style dialogues between two LLM agents.

At present it runs locally using ollama. You can plug in any ollama model you wish.

Eventually there will be a web interface!

### Installation
1. Install [ollama](https://ollama.com/)
2. Start ollama in a separate terminal: ```ollama serve``` (required for all ollama operations)
3. [Install uv](https://docs.astral.sh/uv/getting-started/installation/).
4. Clone this repository.
5. Navigate to the 'dialogues' directory.
6. Copy the contents of the .env-template file to a file named .env. You will need to fill in a value for MODEL; use ollama list to see the names of locally available models.
7. Run the sample query: ```uv run logos``` — you should see a definition of justice!
  A. If you get a ModuleNotFoundError, try adding the current directory to your Python path: export ```PYTHONPATH=$PYTHONPATH:/path/to/dialogues``` (replace '/path/to/dialogues' with the actual path to the dialogues directory)
  B. If it's taking a really long time, you might want to use a smaller model. [tinyllama](https://ollama.com/library/tinyllama) is a good choice; get it with ```ollama pull tinyllama```

### License
Dialogues is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute dialogues subject to the [stipulations](https://github.com/jwjacobson/dialogues/blob/main/LICENSE) of that license.
