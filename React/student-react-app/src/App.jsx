
import { useState } from "react";
import "./App.css";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [course, setCourse] = useState("");
  const [student, setStudent] = useState(null);

  function handleSubmit(e) {
    e.preventDefault();
    setStudent({ name, email, course });
  }

  return (
    <div className="container">
      <h1>Student Registration Form</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Student Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Course"
          value={course}
          onChange={(e) => setCourse(e.target.value)}
          required
        />

        <button type="submit">Submit</button>
      </form>

      {student && (
        <div className="details">
          <h2>Student Details</h2>
          <p>Name: {student.name}</p>
          <p>Email: {student.email}</p>
          <p>Course: {student.course}</p>
        </div>
      )}
    </div>
  );
}

export default App;
