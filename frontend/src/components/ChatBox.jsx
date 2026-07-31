import { useState } from "react";
import { sendQuestion } from "../services/api";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);

  const handleSubmit = async () => {
    if (!question.trim()) return;

    const response = await sendQuestion(question);

    setAnswer(response.answer);
    setSources(response.sources);
  };

  return (
    <div>
      <h1>IronStore Enterprise AI Assistant</h1>

      <textarea
        rows="4"
        cols="60"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <br />
      <br />

      <button onClick={handleSubmit}>
        Ask AI
      </button>

      <hr />

      <h2>Answer</h2>

      <p>{answer}</p>

      <h2>Sources</h2>

      <ul>
        {sources.map((item, index) => (
          <li key={index}>
            {item.source} (Page {item.page})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ChatBox;