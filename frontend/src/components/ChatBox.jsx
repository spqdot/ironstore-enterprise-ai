import { useState } from "react";
import { sendQuestion } from "../services/api";
import Message from "./Message";
import SourceList from "./SourceList";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    const currentQuestion = question.trim();

    if (!currentQuestion || loading) return;

    // Add user's question to chat history
    const userMessage = {
      role: "user",
      text: currentQuestion,
      sources: [],
    };

    setMessages((previousMessages) => [
      ...previousMessages,
      userMessage,
    ]);

    // Clear textarea
    setQuestion("");

    setLoading(true);

    try {
      const response = await sendQuestion(currentQuestion);

      // Add AI response to chat history
      const assistantMessage = {
        role: "assistant",
        text: response.answer,
        sources: response.sources || [],
      };

      setMessages((previousMessages) => [
        ...previousMessages,
        assistantMessage,
      ]);
    } catch (error) {
      const errorMessage = {
        role: "assistant",
        text: "Unable to connect to the AI Assistant.",
        sources: [],
      };

      setMessages((previousMessages) => [
        ...previousMessages,
        errorMessage,
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="chat-container">

      <h1>🤖 IronStore Enterprise AI Assistant</h1>

      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index}>
            <Message
              role={message.role}
              text={message.text}
            />

            {message.role === "assistant" && (
              <SourceList sources={message.sources} />
            )}
          </div>
        ))}

        {loading && (
          <Message
            role="assistant"
            text="Thinking..."
          />
        )}
      </div>

      <div className="chat-input-area">

        <textarea
          rows="3"
          placeholder="Ask a question about company policies..."
          value={question}
          onChange={(event) => setQuestion(event.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
        />

        <button
          onClick={handleSubmit}
          disabled={loading || !question.trim()}
        >
          {loading ? "Thinking..." : "Ask AI"}
        </button>

      </div>

    </div>
  );
}

export default ChatBox;