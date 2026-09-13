# Simple ML framework for learning from psychology questions
# Uses TF-IDF + Naive Bayes style classification (pure Python, no external deps)
# Associates user questions with core MD documents and historical psychologists

import re
import math
from collections import defaultdict, Counter

# Core knowledge base loaded from MD files (summarized for matching)
KNOWLEDGE_BASE = {
    "behavioral-psychology.md": {
        "topics": ["classical conditioning", "operant conditioning", "reinforcement", "punishment", "shaping", "extinction", "stimulus", "response", "habit", "behaviorism", "skinner", "pavlov", "watson", "thorndike"],
        "researchers": ["Ivan Pavlov", "B.F. Skinner", "John B. Watson", "Edward Thorndike", "Clark Hull"],
        "summary": "Behavior is shaped by environmental consequences. Classical conditioning (Pavlov) pairs stimuli. Operant conditioning (Skinner) uses reinforcement and punishment to increase or decrease behavior."
    },
    "cognitive-psychology.md": {
        "topics": ["memory", "attention", "perception", "decision making", "problem solving", "language", "information processing", "schema", "cognitive load", "working memory", "long-term memory", "piaget", "ebbinghaus", "bartlett"],
        "researchers": ["Jean Piaget", "Hermann Ebbinghaus", "Frederic Bartlett", "Ulric Neisser", "George Miller"],
        "summary": "Studies mental processes: how we perceive, remember, think, and decide. Treats the mind as an information processor."
    },
    "key-concepts.md": {
        "topics": ["reinforcement", "punishment", "conditioning", "memory", "attention", "perception", "schema", "cognitive dissonance", "habit formation", "extinction"],
        "researchers": [],
        "summary": "Core concepts bridging behavioral and cognitive approaches."
    },
    "key-researchers.md": {
        "topics": ["pavlov", "skinner", "watson", "piaget", "ebbinghaus", "wundt", "james", "freud", "jung", "tolman"],
        "researchers": ["Wilhelm Wundt", "William James", "Sigmund Freud", "Carl Jung", "Edward Tolman"],
        "summary": "Historical figures who shaped the fields."
    }
}

class PsychologyLearner:
    """Lightweight classifier that maps questions to relevant docs and researchers."""
    def __init__(self):
        self.vocab = set()
        self.doc_vectors = {}
        self.researcher_index = defaultdict(list)
        self._build_index()

    def _tokenize(self, text):
        return re.findall(r"[a-z]+", text.lower())

    def _build_index(self):
        for doc, data in KNOWLEDGE_BASE.items():
            tokens = []
            for t in data["topics"]:
                tokens.extend(self._tokenize(t))
            for r in data["researchers"]:
                tokens.extend(self._tokenize(r))
            tokens.extend(self._tokenize(data["summary"]))
            self.vocab.update(tokens)
            self.doc_vectors[doc] = Counter(tokens)
            for r in data["researchers"]:
                self.researcher_index[r].append(doc)

    def classify(self, question):
        q_tokens = self._tokenize(question)
        q_counter = Counter(q_tokens)
        scores = {}
        for doc, vec in self.doc_vectors.items():
            score = 0.0
            for term, qf in q_counter.items():
                if term in vec:
                    # simple TF-IDF-ish: term frequency in doc * presence in query
                    score += vec[term] * qf
            scores[doc] = score
        # top doc
        top_doc = max(scores, key=scores.get) if scores else None
        # relevant researchers
        relevant = []
        for term in q_tokens:
            for r, docs in self.researcher_index.items():
                if term in self._tokenize(r) and r not in relevant:
                    relevant.append(r)
        return {
            "top_document": top_doc,
            "scores": scores,
            "relevant_researchers": relevant[:5],
            "matched_topics": [t for t in KNOWLEDGE_BASE.get(top_doc, {}).get("topics", []) if t in question.lower()]
        }

    def log_question(self, question, response_note=""):
        """Record a question for future cross-referencing."""
        result = self.classify(question)
        entry = {
            "question": question,
            "classification": result,
            "note": response_note
        }
        # In a real system this would append to a JSONL log file
        return entry

# Example usage
if __name__ == "__main__":
    learner = PsychologyLearner()
    print(learner.classify("How does reinforcement shape habits?"))
    print(learner.classify("What did Piaget say about cognitive development?"))