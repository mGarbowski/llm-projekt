import React, { useCallback, useMemo, useState } from "react";

type Role = "user" | "assistant";
type Source = {
  id: string;
  content: string;
  course: string;
  title: string;
  filename: string;
};
type ApiResponse = {
  answer: string;
  sources: Source[];
};

const API_BASE: string = "http://localhost:8000";

type ChatMessage = {
  role: Role;
  content: string;
  sources?: Source[];
};

export const App: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const canSend = useMemo(() => input.trim().length > 0 && !loading, [input, loading]);

  const sendQuestion = useCallback(
    async (question: string) => {
      setError(null);
      setLoading(true);
      try {
        const res = await fetch(`${API_BASE}/completion`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question,
            top_k: 4,
            max_new_tokens: 256,
            temperature: 0.7,
          }),
        });
        if (!res.ok) {
          const text = await res.text().catch(() => "");
          throw new Error(text || `HTTP ${res.status}`);
        }
        const data: ApiResponse = await res.json();
        setMessages((prev) => [
          ...prev,
          { role: "assistant", content: data.answer ?? "", sources: data.sources ?? [] },
        ]);
      } catch (e: any) {
        setError(e?.message || "Request failed");
      } finally {
        setLoading(false);
      }
    },
    []
  );

  const onSubmit = useCallback(
    async (e: React.FormEvent) => {
      e.preventDefault();
      if (!canSend) return;
      const question = input.trim();
      setMessages((prev) => [...prev, { role: "user", content: question }]);
      setInput("");
      await sendQuestion(question);
    },
    [canSend, input, sendQuestion]
  );

  const onKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        if (canSend) {
          const form = (e.currentTarget.closest("form") as HTMLFormElement | null);
          form?.dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }));
        }
      }
    },
    [canSend]
  );

  return (
    <div style={{ maxWidth: 820, margin: "0 auto", padding: 16, fontFamily: "system-ui, sans-serif" }}>
      <h1 style={{ marginBottom: 12 }}>RAG Chat</h1>

      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: 8,
          padding: 12,
          height: 480,
          overflowY: "auto",
          background: "#fafafa",
        }}
      >
        {messages.length === 0 && (
          <div style={{ color: "#666" }}>Ask a question to start the conversation.</div>
        )}
        {messages.map((m, idx) => (
          <div key={idx} style={{ marginBottom: 14 }}>
            <div style={{ fontSize: 12, color: "#666", marginBottom: 4 }}>
              {m.role === "user" ? "You" : "Assistant"}
            </div>
            <div
              style={{
                whiteSpace: "pre-wrap",
                background: m.role === "user" ? "#e9f2ff" : "#fff",
                border: "1px solid #e5e5e5",
                borderRadius: 6,
                padding: 10,
              }}
            >
              {m.content}
            </div>
            {m.role === "assistant" && m.sources && m.sources.length > 0 && (
              <div style={{ marginTop: 6 }}>
                <div style={{ fontSize: 12, color: "#888", marginBottom: 4 }}>Sources:</div>
                <ul style={{ margin: 0, paddingLeft: 18 }}>
                  {m.sources.map((s, i) => (
                    <li key={s.id ?? i} style={{ fontSize: 13 }}>
                      <span style={{ color: "#333" }}>
                        [{i + 1}] {s.title ?? s.id ?? "source"}
                      </span>
                      <div style={{ color: "#666" }}>
                        {s.content.length > 220 ? `${s.content.slice(0, 220)}…` : s.content}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div style={{ color: "#666" }}>Generating…</div>
        )}
        {error && (
          <div style={{ color: "crimson" }}>Error: {error}</div>
        )}
      </div>

      <form onSubmit={onSubmit} style={{ marginTop: 12, display: "grid", gap: 8 }}>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          rows={3}
          placeholder="Type your question…"
          style={{
            resize: "vertical",
            padding: 10,
            borderRadius: 6,
            border: "1px solid #ccc",
            fontFamily: "inherit",
            fontSize: 14,
          }}
        />
        <div style={{ display: "flex", justifyContent: "flex-end", gap: 8 }}>
          <button
            type="submit"
            disabled={!canSend}
            style={{
              padding: "8px 14px",
              borderRadius: 6,
              border: "1px solid #0a66c2",
              background: canSend ? "#0a66c2" : "#9cbfe3",
              color: "#fff",
              cursor: canSend ? "pointer" : "not-allowed",
            }}
          >
            Send
          </button>
        </div>
      </form>

      <div style={{ marginTop: 8, fontSize: 12, color: "#777" }}>
        Using API: {API_BASE || "/completion (same-origin)"}
      </div>
    </div>
  );
};
