import React, { useState } from "react";
import axios from "axios";

function App() {
  const [bookId, setBookId] = useState("");
  const [book, setBook] = useState(null);
  const [error, setError] = useState("");

  const fetchBook = async () => {
    try {
      const resp = await axios.get(`/books/${bookId}`);
      setBook(resp.data);
      setError("");
    } catch (e) {
      setError(e.response?.data?.detail || "Error fetching book");
      setBook(null);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Book Lookup Demo</h1>
      <input type="number" value={bookId} onChange={e => setBookId(e.target.value)} placeholder="Book ID" />
      <button onClick={fetchBook}>Fetch</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {book && (
        <div>
          <h2>{book.title}</h2>
          <p><strong>Author:</strong> {book.author}</p>
          <p>{book.description}</p>
        </div>
      )}
    </div>
  );
}

export default App;
