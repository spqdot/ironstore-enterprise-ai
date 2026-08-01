import { useState } from "react";
import { sendQuestion } from "../services/api";
import Message from "./Message";
import SourceList from "./SourceList";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");
    setSources([]);

    try {
      const response = await sendQuestion(question);

      setAnswer(response.answer);
      setSources(response.sources);
    } catch (error) {
      setAnswer("Something went wrong.");
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">

      <h1>🤖 IronStore Enterprise AI Assistant</h1>

      <textarea
        rows="4"
        placeholder="Ask a question about company policies..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      {question && (
        <Message
          role="user"
          text={question}
        />
      )}

      {answer && (
        <Message
          role="assistant"
          text={answer}
        />
      )}

      <SourceList sources={sources} />

    </div>
  );
}

export default ChatBox;