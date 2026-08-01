function Message({ role, text }) {
  const isUser = role === "user";

  return (
    <div className={`message-row ${isUser ? "user-row" : "assistant-row"}`}>
      <div className={`message ${isUser ? "user-message" : "assistant-message"}`}>
        <div className="message-label">
          {isUser ? "You" : "IronStore AI"}
        </div>

        <div className="message-text">
          {text}
        </div>
      </div>
    </div>
  );
}

export default Message;