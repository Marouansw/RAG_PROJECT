from langflow.load import run_flow_from_json
TWEAKS = {
  "ParseData-vbC5D": {},
  "Prompt-rdrAA": {},
  "ChatOutput-11YKq": {},
  "File-UXst9": {},
  "note-T57FJ": {},
  "note-Kaz0A": {},
  "note-3mQAM": {},
  "FAISS-0lj4S": {},
  "FAISS-aSqP1": {},
  "TextInput-fdkDG": {},
  "OllamaEmbeddings-2uOII": {},
  "OllamaEmbeddings-mMX3V": {},
  "LanguageRecursiveTextSplitter-p80MR": {},
  "GoogleGenerativeAIModel-KiBvW": {},
  "ChatInput-ibmYO": {}
}

result = run_flow_from_json(flow="Vector_Store_RAG_(Gemini).json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)