function SourceList({ sources }) {
  if (!sources || sources.length === 0) {
    return null;
  }

  const getFileName = (path) => {
    if (!path) return "Unknown document";

    return path.split(/[/\\]/).pop();
  };

  return (
    <div className="sources-container">
      <h3>Sources</h3>

      <div className="sources-list">
        {sources.map((source, index) => (
          <div className="source-card" key={index}>
            <div className="source-icon">
              📄
            </div>

            <div>
              <div className="source-name">
                {getFileName(source.source)}
              </div>

              <div className="source-page">
                Page {source.page}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SourceList;